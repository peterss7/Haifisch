import matplotlib.pyplot as plt
import numpy as np
import itertools   
import warnings
import io
from flask import send_file, Flask, request
import jsontools
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

temperature_history = []
humidity_history = []

def load_data():
    data = jsontools.load_data()
    for entry in data:
        temperature_history.append(entry['temperature'])
        humidity_history.append(entry['humidity'])

def generate_plot_image():

    load_data()

    N = 50
    nums = np.arange(1, N+1)    

    temps = np.array(temperature_history)
    humids = np.array(humidity_history)

    temps.resize(N)
    humids.resize(N)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6), facecolor='black')

    for i, data, label, color, title in zip([0, 1], [temps, humids], ['Temperature', 'Humidity'], ['#ff4500', '#00bfff'], ['Temperature', 'Humidity']):
        ax[i].set_facecolor('black')
        ax[i].plot(nums, data, color=color, label=label, marker='o', markersize=4)
        ax[i].set_xlabel('Time', color='white', fontsize=16)
        ax[i].set_ylabel(label, color='white', fontsize=16)
        ax[i].set_title(title, color='white', fontsize=24)
        ax[i].legend(loc='best', title='Legend')
        ax[i].spines['bottom'].set_color('white')
        ax[i].spines['top'].set_color('white')
        ax[i].spines['right'].set_color('white')
        ax[i].spines['left'].set_color('white')
        ax[i].yaxis.label.set_color('white')
        ax[i].xaxis.label.set_color('white')
        ax[i].title.set_color('white')
        ax[i].tick_params(axis='x', colors='white')
        ax[i].tick_params(axis='y', colors='white')
        ax[i].invert_yaxis()

    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    return output.getvalue()

@app.route('/plot')
def get_chart():
    print('Generating plot')
    return send_file(io.BytesIO(generate_plot_image()), mimetype='image/png')    


if __name__ == '__main__':
    app.run(host='xxxxxxxxx', port=5501)
