# RealVision

This project implements a face recognition pipeline using machine learning techniques. It detects faces in images, crops and normalizes them, then applies dimensionality reduction and a support vector machine (SVM) classifier for recognition.

## Features

- Detects faces in images using Haar cascade classifier.
- Normalizes and preprocesses face images.
- Utilizes Principal Component Analysis (PCA) for dimensionality reduction.
- Applies SVM for classification.
- Provides probability scores for classification results.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dhahlan3890/RealVision.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have Python installed.
2. Run the `face_recognition.py` script with the image file path:

   ```bash
   python face_recognition.py path/to/image.jpg
   ```

## Models and Data

- `./model`: Contains the pre-trained SVM model, PCA model, and mean face array for face recognition.
- `./FEA_model`: Contains additional pre-trained models for feature extraction and classification.
- `./model/haarcascade_frontalface_default.xml`: Haar cascade classifier for face detection.

## Results

The pipeline produces images with detected faces and their respective classifications and confidence scores overlaid.

## Contributing

Contributions are welcome! Please create a pull request with your changes.

## Acknowledgments

- This project utilizes OpenCV, NumPy, and scikit-learn libraries.

