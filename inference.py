import cv2
import numpy as np
import tensorflow as tf
from yolov5_model import YOLOv5Model  # Assuming you have a YOLOv5 model class

# Load the YOLOv5 model
yolov5_model = YOLOv5Model()  # Replace with the actual YOLOv5 model loading code

# Load the TensorFlow model
tensorflow_model = tf.keras.models.load_model("your_tensorflow_model.h5")  # Replace with the actual TensorFlow model loading code

def preprocess_yolov5(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Resize the image to 640x640
    resized_image = cv2.resize(image, (640, 640))
    
    # Normalize the image values to the range [0, 1]
    normalized_image = resized_image / 255.0
    
    # YOLOv5 expects the image in the format (height, width, channels)
    normalized_image = np.expand_dims(normalized_image, axis=0)
    
    return normalized_image



def preprocess_tensorflow(image):
    # Resize the image to 224x224
    resized_image = cv2.resize(image, (224, 224))
    
    # Normalize the pixel values to the range [0, 1]
    normalized_image = resized_image / 255.0
      
    return normalized_image


def inference_yolov5(image_path):
    image = cv2.imread(image_path)
    preprocessed_image = preprocess_yolov5(image)
    
    # Perform inference with YOLOv5
    yolov5_output = yolov5_model.inference(preprocessed_image)  # Replace with your actual inference code
    
    return yolov5_output

def inference_tensorflow(yolov5_output):
    # Assuming yolov5_output contains bounding boxes or relevant information
    # Extract necessary information and preprocess for TensorFlow model input
    tensorflow_input = process_yolov5_output(yolov5_output)  # Implement process_yolov5_output function
    
    # Perform inference with TensorFlow model
    tensorflow_output = tensorflow_model.predict(tensorflow_input)  # Replace with your actual inference code
    
    return tensorflow_output

if __name__ == "__main__":
    # Replace "your_image.jpg" with the actual image path
    image_path = "your_image.jpg"
    
    # Perform YOLOv5 inference
    yolov5_output = inference_yolov5(image_path)
    
    # Perform TensorFlow inference using YOLOv5 output
    tensorflow_output = inference_tensorflow(yolov5_output)
    
    # Optionally, print or use the final output
    print("TensorFlow Model Output:", tensorflow_output)
