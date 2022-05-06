import json
import mariadb
import sys

def reverse_data(data):
	new_data =  list(reversed(data))
	if len(new_data) <= 20:
		return list(reversed(new_data))
	else:
		return list(reversed(new_data[0:20]))


def import_data():
	try:
		conn = mariadb.connect(
			user="root",
			password="root",
			host="localhost",
			database="Details"
		)
	except mariadb.Error as e:
		print("Error connecting: {e}")
		sys.exit(1)
	cur = conn.cursor()
	
	cur.execute("SELECT * FROM pump_data")
	#print(cur.fetchall())
	#dict = {"Temperature":[],"Humidity":[],"Pump":[],"Water":[],"Time":[]}
	
	temp = []
	humid = []
	pump = []
	water = []
	time = []
	for (Temperature, Humidity, Pump, Water, Time) in cur:
		temp.append(Temperature)
		humid.append(Humidity)
		pump.append(Pump)
		water.append(Water)
		time.append(Time)

	temp = reverse_data(temp)
	humid = reverse_data(humid)
	pump = reverse_data(pump)
	water = reverse_data(water)
	time = reverse_data(time)
	dict = {"Temperature":temp,"Humidity":humid,"Pump":pump,"Water":water,"Time":time}
	#print(dict)
	return dict

#Temperature, Humidity, Pump, Water, Time
#import_data()
