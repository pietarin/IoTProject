from flask import Flask, render_template
from fetchdata import *
import json
app = Flask(__name__)

@app.route('/data')
def data():
    dict =  import_data()
    dummydata = {
        "Temperature": dict["Temperature"],
        "Humidity": dict["Humidity"],
        "Pump": dict["Pump"],
        "Water": dict["Water"],
        "Time" : dict["Time"]
    }
    return json.dumps(dict)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)