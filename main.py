#!/usr/bin/env python3
import serial 
import json
import mariadb
import sys
from datetime import datetime

Temparature = 0.0
Humidity = 0.0
Pump = 0
Water = 1


if __name__ == '__main__':
	
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
	
	ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	
	
	while True:
		
		if ser.in_waiting >0:
			line = ser.readline().decode('utf-8').rstrip()
			print(line)
			try:
				jsonObj = json.loads(line)
				Temperature = jsonObj.get('temp')
				Humidity = jsonObj.get('humidity')
				Pump  = jsonObj.get('pump')
				Water  = jsonObj.get('water')
				print("Temperature ", Temperature)
				print("Humidity ", Humidity)
				print("Pump ", Pump)
				print("Water ", Water)
				print(datetime.now().strftime("%H:%M:%S"))
				print(jsonObj)
				cur.execute("INSERT INTO pump_data (Temperature, Humidity, Pump, Water, Time) VALUES (?,?,?,?,?)", (float(Temperature), float(Humidity), int(Pump), int(Water), datetime.now().strftime("%H:%M:%S")))
				conn.commit()
				ser.reset_input_buffer()
			except:
				print("Error")
			
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
	
	cur.execute("SELECT Temperature, Humidity, Pump, Water, Time FROM pump_data")
	
	dict = {"Temperature":[],"Humidity":[],"Pump":[],"Water":[],"Time":[]}
	
	for (Temperature, Humidity, Pump, Water, Time) in cur:
		dict["Temperature"].append(Temperature)
		dict["Humidity"].append(Humidity)
		dict["Pump"].append(Pump)
		dict["Water"].append(Water)
		dict["Time"].append(Time)
	print(dict)
	return dict

