import cv2
import time

def capture_image(camera_index=0, resolution=(640, 480)):
    # Initialize the USB camera
    cap = cv2.VideoCapture(camera_index)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    # Allow the camera to warm up
    time.sleep(2)

    # Capture a single frame
    ret, frame = cap.read()

    # Resize the frame to the specified resolution
    if ret:
        frame_resized = cv2.resize(frame, resolution)
        timestamp = time.strftime("%Y%m%d%H%M%S")
        image_filename = f"captured_image_{timestamp}.jpg"
        cv2.imwrite(image_filename, frame_resized)
        print(f"Image captured, resized, and saved as {image_filename}")
        return image_filename
    else:
        print("Error: Could not capture image.")

    # Release the camera
    cap.release()

