from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize control states (used for both GET and POST requests)
control_states = {
    'pump': False,
    'mixer': False,
    'waterValve': False,
    'nutrientsValve': False,
    'plate1Valve': False,
    'plate2Valve': False,
    'fan': False,
    'plate1BlueLight': 0,
    'plate1RedLight': 0,
    'plate1Heater': False,
    'plate1DrainValve': False,
    'plate2BlueLight': 0,
    'plate2RedLight': 0,
    'plate2Heater': False,
    'plate2DrainValve': False
}

@app.route('/update', methods=['POST'])
def update_controls():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract data from the JSON and assign to variables
        control_states['pump'] = data.get('pump', False)
        control_states['mixer'] = data.get('mixer', False)
        control_states['waterValve'] = data.get('waterValve', False)
        control_states['nutrientsValve'] = data.get('nutrientsValve', False)
        control_states['plate1Valve'] = data.get('plate1Valve', False)
        control_states['plate2Valve'] = data.get('plate2Valve', False)
        control_states['fan'] = data.get('fan', False)

        # Plate controls
        control_states['plate1BlueLight'] = data.get('plate1BlueLight', 0)
        control_states['plate1RedLight'] = data.get('plate1RedLight', 0)
        control_states['plate1Heater'] = data.get('plate1Heater', False)
        control_states['plate1DrainValve'] = data.get('plate1DrainValve', False)
        
        control_states['plate2BlueLight'] = data.get('plate2BlueLight', 0)
        control_states['plate2RedLight'] = data.get('plate2RedLight', 0)
        control_states['plate2Heater'] = data.get('plate2Heater', False)
        control_states['plate2DrainValve'] = data.get('plate2DrainValve', False)

        # Print the extracted variables (optional for debugging)
        print("Control States Updated:")
        for key, value in control_states.items():
            print(f"{key}: {value}")

        # Respond back with a success message
        return jsonify({"status": "success", "message": "Control updated successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/get_state', methods=['GET'])
def get_state():
    try:
        # Return the current state as JSON
        return jsonify(control_states), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
