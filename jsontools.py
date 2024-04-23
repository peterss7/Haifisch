import json
import os
from datetime import datetime

MAX_HISTORY = 50
DATA_FILE = 'sensor_data.json'

def save_data(temperature, humidity):
    
    data = load_data()
    
    data.append({'temperature': temperature, 'humidity': humidity})

    data = data[-MAX_HISTORY:]

    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as file:
            json.dump([], file)
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    return data
