from flask import Flask, request, render_template, redirect, flash, session
import joblib
import pandas as pd
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generates a random secret key for session management

# Load model and artifacts
data = joblib.load("real_estate_model.pkl")
model = data['model']
location_encoding_map = data['location_encoding_map']
location_names = data['location_names']

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

        # Check if location is valid
        if location not in location_encoding_map:
            flash("❌ Selected location is not in the model's training data.")
            return redirect('/')

        # Encode location and calculate price per sqft
        location_encoded = location_encoding_map[location]
        price_per_sqrft = location_encoded / carpet_area

        input_data = pd.DataFrame([{
            "property_type": property_type,
            "furnish_status": furnish_status,
            "bedrooms": bedrooms,
            "carpet_area": carpet_area,
            "bathrooms": bathrooms,
            "balconies": balconies,
            "price_per_sqrft": price_per_sqrft,
            "location_encoded": location_encoded
        }])

        # Make prediction
        prediction = model.predict(input_data)[0]
        return render_template('result.html', prediction=round(prediction, 2), location=location)

    except Exception as e:
        flash("❌ Something went wrong. Please try again.")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
