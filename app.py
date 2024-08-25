from flask import Flask, request, render_template, jsonify
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
import joblib  # For loading scikit-learn models
from skimage.feature import graycomatrix, graycoprops

app = Flask(__name__, template_folder='C:/Users/NANDEESH/Desktop/Image processing/Project/fracture Project/fracture Project')
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Load your model
model = joblib.load('random_forest_model.pkl')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            prediction = process_and_predict(file_path)
            return jsonify({'prediction': prediction})
    return render_template('upload.html')

def process_and_predict(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 512))  # Resize as your model expects
    features = extract_features(img)  # Adjust feature extraction to your training process
    prediction = model.predict([features])
    return int(prediction[0])

def extract_features(image):
    # GLCM feature extraction as used in the training process
    properties = ['energy', 'correlation', 'dissimilarity', 'homogeneity', 'contrast']
    glcm = graycomatrix(image, distances=[1, 3, 5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4])
    features = [graycoprops(glcm, prop).ravel()[0] for prop in properties]
    return np.array(features)

if __name__ == '__main__':
    app.run(debug=True)
