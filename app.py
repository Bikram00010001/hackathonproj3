from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the trained model
model = load_model('soil_classifier_model.h5')

# Define categories (matching your training dataset)
categories = ['Alluvial soil', 'Black Soil', 'Clay soil', 'Red soil']
IMG_SIZE = 128

# Function to predict soil type
def predict_soil_type(img_path):
    # Load and preprocess the image
    img = cv2.imread(img_path)
    if img is None:
        return None
    
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    
    # Predict the class
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    predicted_soil_type = categories[predicted_class]
    
    return predicted_soil_type

# Route to the homepage (for frontend)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Save the uploaded image temporarily
    img_path = os.path.join('uploads', file.filename)
    file.save(img_path)
    
    # Get prediction from the model
    predicted_soil_type = predict_soil_type(img_path)
    
    if predicted_soil_type:
        return jsonify({'predicted_soil_type': predicted_soil_type})
    else:
        return jsonify({'error': 'Unable to process image'}), 400

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    app.run(debug=True)
