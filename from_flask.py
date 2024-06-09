from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

data_history = {'labels': [], 'Voltage': [], 'Current': []}

@app.route('/api/update-dht-data', methods=['POST'])
def update_dht_data():
    global data_history

    data = request.json
    Voltage = data.get('Voltage')
    Current = data.get('Current')

    if Voltage is not None and Current is not None:
        data_history['labels'].append(len(data_history['Voltage']))
        data_history['Voltage'].append(Voltage)
        data_history['Current'].append(Current)

    return "Data received successfully!", 200

@app.route('/')
def index():
    return render_template('graph.html')

@app.route('/api/get-graph-data', methods=['GET'])
def get_graph_data():
    data = {"labels": data_history['labels'], "Voltage": data_history['Voltage'], "Current": data_history['Current']}
    print("Data Received Successfully")
    return jsonify(data)