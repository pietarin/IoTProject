from flask import Flask, render_template
app = Flask(__name__)

@app.route('/data')
def data():
    dummydata = {
        "Temperature": [25, 26, 27, 26, 28],
        "Moisture": [75, 77, 76, 77, 76],
        "Pump": 1,
        "Water": 1
    }
    return dummydata

@app.route('/')
def home():
    dummydata = data()
    keys = list(dummydata.keys())
    legend = ['Moisture', 'Temperature']
    labels = [keys[0], keys[1]]
    temperature = dummydata.get("Temperature")
    moisture = dummydata.get("Moisture")
    pump = dummydata.get("Pump")
    water = dummydata.get("Water")
    return render_template('index.html', temperature=temperature, moisture=moisture, pump=pump, water=water, labels=labels, legend=legend)

if __name__ == '__main__':
    app.run(debug=True)