import tensorflow as tf
from tensorflow import keras
import numpy as np
import torch
from PIL import Image

def predict_class(image_path):
    # Load the saved model
    model = keras.models.load_model('Models/detect-disease.h5')

    # Load the image you want to classify
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224, 3))

    # Preprocess the image
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # Make predictions
    predictions = model.predict(image)

    # Get the class with the highest probability
    predicted_class = np.argmax(predictions)

    return predicted_class

def detect_leaf(input_image_path):
    # Load the custom YOLOv5 model
    model = torch.hub.load('yolov5', 'custom', path='Models/detect-leaf.pt', source='local')

    # Load the image you want to detect objects in
    image = Image.open(input_image_path)

    # Make predictions
    results = model(image)

    # Get the bounding box with the highest confidence
    best_bbox = results.xyxy[0][results.xyxy[0][:, 4].argmax()]

    # Extract coordinates and convert to integers
    x_min, y_min, x_max, y_max = map(int, best_bbox[:4])

    # Crop the bounding box
    cropped_image = image.crop((x_min, y_min, x_max, y_max))
    return cropped_image

    # # Save the cropped image
    # cropped_image.save(output_cropped_image_path)

    # # Optionally, display the cropped image
    # cropped_image.show()

    # # Display the results
    # #results.show()

    # # If you want to save the results with bounding boxes
    # results.save(output_results_path)

def inference(image_path):
    x = detect_leaf(image_path)
    y = predict_class(x)
    return y