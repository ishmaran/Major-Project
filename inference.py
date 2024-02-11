import torch
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import numpy as np

def inference(img_path):
    # Define paths to your models
    leaf_detection_model = 'detect-leaf.pt'   # Your YOLOv5 model path
    disease_detection_model = 'detect-disease.h5'  # Your disease model path

    # Load YOLOv5 leaf detection model
    detect_leaf = torch.hub.load('path-to-yolov5', 'custom', path=leaf_detection_model, source='local')

    # Load disease detection model
    detect_disease = load_model(disease_detection_model) 

    # Read the image
    img = cv2.imread(img_path) 

    # Perform leaf detection using YOLOv5
    results = detect_leaf(img)

    # Extract the cropped leaf image with the highest confidence
    crop = results.crop(save=False)  # Returns a PIL image 
    img_crop = np.array(crop)[:, :, ::-1]  # Convert PIL to OpenCV format (BGR)

    # Preprocessing for disease detection model
    img_resized = cv2.resize(img_crop, (224, 224))  # Resize to 224x224
    img_normalized = img_resized / 255.0  # Normalize pixel values between 0 and 1
    input_image = img_normalized.reshape(1, 224, 224, 3)  # Add batch dimension 

    # Disease prediction
    prediction = detect_disease.predict(input_image)
    disease_class = np.argmax(prediction[0])  # Get the class with the highest probability

    return disease_class 
