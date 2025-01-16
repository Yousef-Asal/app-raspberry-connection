from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_controls():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract data from the JSON and assign to variables
        pump = data.get('pump', False)
        mixer = data.get('mixer', False)
        water_valve = data.get('waterValve', False)
        nutrients_valve = data.get('nutrientsValve', False)
        plate1_valve = data.get('plate1Valve', False)
        plate2_valve = data.get('plate2Valve', False)
        fan = data.get('fan', False)

        # Plate controls
        plate1_blue_light = data.get('plate1BlueLight', 0)
        plate1_red_light = data.get('plate1RedLight', 0)
        plate1_heater = data.get('plate1Heater', False)
        plate1_drain_valve = data.get('plate1DrainValve', False)
        
        plate2_blue_light = data.get('plate2BlueLight', 0)
        plate2_red_light = data.get('plate2RedLight', 0)
        plate2_heater = data.get('plate2Heater', False)
        plate2_drain_valve = data.get('plate2DrainValve', False)

        # Print the extracted variables
        print("Pump: ", pump)
        print("Mixer: ", mixer)
        print("Water Valve: ", water_valve)
        print("Nutrients Valve: ", nutrients_valve)
        print("Plate 1 Valve: ", plate1_valve)
        print("Plate 2 Valve: ", plate2_valve)
        print("Fan: ", fan)

        print("Plate 1 Blue Light: ", plate1_blue_light)
        print("Plate 1 Red Light: ", plate1_red_light)
        print("Plate 1 Heater: ", plate1_heater)
        print("Plate 1 Drain Valve: ", plate1_drain_valve)

        print("Plate 2 Blue Light: ", plate2_blue_light)
        print("Plate 2 Red Light: ", plate2_red_light)
        print("Plate 2 Heater: ", plate2_heater)
        print("Plate 2 Drain Valve: ", plate2_drain_valve)

        # Respond back with a success message
        return jsonify({"status": "success", "message": "Control updated successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
