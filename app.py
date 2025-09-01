from flask import Flask, request, render_template, redirect, flash, session
import joblib
import pandas as pd
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generates a random secret key for session management

# Load model and artifacts
data = joblib.load("model.pkl")
model = data['model']
location_names = data['location_names']
location_encoding_map = data['location_encoding_map']

@app.route('/')
def home():
    return render_template("index.html", locations=location_names)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
 
    try:
        # Check for missing fields
        required_fields = ['property_type', 'furnish_status', 'bedrooms', 'carpet_area', 'bathrooms', 'balconies', 'location']
        for field in required_fields:
            if not data.get(field):
                flash("⚠️ Please fill out all the details before submitting.")
                return redirect('/')

        # Parse form values
        property_type = int(data['property_type'])
        furnish_status = int(data['furnish_status'])
        bedrooms = int(data['bedrooms'])
        carpet_area = float(data['carpet_area'])
        bathrooms = int(data['bathrooms'])
        balconies = int(data['balconies'])
        location = data['location'].strip()

        # Generating area per bedroom internally
        area_per_bedroom = carpet_area / bedrooms
        # Encoding location name 
        location_encoded = location_encoding_map[location]

        input_data = pd.DataFrame([{
            "property_type": property_type,
            "furnish_status": furnish_status,
            "bedrooms": bedrooms,
            "carpet_area": carpet_area,
            "bathrooms": bathrooms,
            "balconies": balconies,
            "location_encoded": location_encoded,
            "area_per_bedroom": area_per_bedroom

        }])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Convert into lakhs
        prediction_lakhs = round(prediction / 1e5, 2)

        return render_template(
            'result.html',
            prediction=prediction_lakhs,
            location=location
        )

    except Exception as e:
        flash("❌ Something went wrong. Please try again.")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
