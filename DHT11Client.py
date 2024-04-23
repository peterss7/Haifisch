import time
import jsontools
import requests

url = 'http://192.168.86.44:80/'

temperature_history = []
humidity_history = []

def fetch_sensor_data():
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperature = data['temperature']
                humidity = data['humidity']

                temperature_history.append(temperature)
                humidity_history.append(humidity)

                jsontools.save_data(temperature, humidity)

                print(f'Temperature: {temperature}, Humidity: {humidity}')

                # for i in range(len(temperature_history)):
                #     print(f'Temperature {i}: {temperature_history[i]}, Humidity{i}: {humidity_history[i]}')

            else:
                print('Error in request, failed to fetch data from Arduino')
        except Exception as e:
            print(f'Error: {e}')
        time.sleep(60)

if __name__ == '__main__':
    fetch_sensor_data()