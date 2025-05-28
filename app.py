from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILENAME = "timesheet.json"

def load_timesheet():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            return json.load(f)
    return []

def save_timesheet(timesheet):
    with open(FILENAME, 'w') as f:
        json.dump(timesheet, f, indent=2)

@app.route('/entries', methods=['GET'])
def get_entries():
    timesheet = load_timesheet()
    return jsonify(timesheet)

@app.route('/entries', methods=['POST'])
def add_entry():
    data = request.get_json()
    timesheet = load_timesheet()
    entry = {
        "date": data.get("date"),
        "hours": float(data.get("hours")),
        "desc": data.get("desc")
    }
    timesheet.append(entry)
    save_timesheet(timesheet)
    return jsonify({"message": "Entry added", "entry": entry}), 201

@app.route('/entries/<int:index>', methods=['PUT'])
def edit_entry(index):
    timesheet = load_timesheet()
    if 0 <= index < len(timesheet):
        data = request.get_json()
        if "date" in data:
            timesheet[index]["date"] = data["date"]
        if "hours" in data:
            timesheet[index]["hours"] = float(data["hours"])
        if "desc" in data:
            timesheet[index]["desc"] = data["desc"]
        save_timesheet(timesheet)
        return jsonify({"message": "Entry updated", "entry": timesheet[index]})
    else:
        return jsonify({"error": "Entry not found"}), 404

@app.route('/entries/<int:index>', methods=['DELETE'])
def delete_entry(index):
    timesheet = load_timesheet()
    if 0 <= index < len(timesheet):
        removed = timesheet.pop(index)
        save_timesheet(timesheet)
        return jsonify({"message": "Entry deleted", "entry": removed})
    else:
        return jsonify({"error": "Entry not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

