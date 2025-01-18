from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder=".")

# Serve the frontend HTML
@app.route('/')
def home():
    return render_template('index.html')

# Process data and generate recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    crop = data.get("cropName", "") or data.get("customCrop", "")
    season = data.get("season", "")
    soil_type = data.get("soilType", "")
    state = data.get("state", "").replace("_", " ")

    # Example logic from AI module
    recommendations = f"Based on your inputs for {crop}, we recommend planting in early {season} for optimal yield. " \
                       f"Consider using a balanced NPK fertilizer with a ratio of 30-40-70 for your {soil_type} soil. " \
                       f"For the state of {state}, ensure proper irrigation methods are in place."

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
