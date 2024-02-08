import RPi.GPIO as GPIO
import time

# Define pump pins
PUMP_1_PIN = 22
PUMP_2_PIN = 24
PUMP_3_PIN = 26

def run_pump(class_index):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PUMP_1_PIN, GPIO.OUT)
    GPIO.setup(PUMP_2_PIN, GPIO.OUT)
    GPIO.setup(PUMP_3_PIN, GPIO.OUT)

    # Turn off all pumps initially
    GPIO.output(PUMP_1_PIN, GPIO.HIGH)
    GPIO.output(PUMP_2_PIN, GPIO.HIGH)
    GPIO.output(PUMP_3_PIN, GPIO.HIGH)

    # Run the corresponding pump based on the class
    if class_index in [0, 1]:  # Class 0: Tomato Bacterial spot, Class 1: Tomato Early blight
        print("Running Pump 1 for Tomato Bacterial spot or Early blight")
        GPIO.output(PUMP_1_PIN, GPIO.LOW)
    elif class_index in [3, 4, 6, 8]:  # Class 3, 4, 6, 8: Tomato Late blight, Tomato Leaf Mold, Tomato Septoria leaf spot, Tomato Target Spot
        print("Running Pump 2 for Late blight, Leaf Mold, Septoria, or Target Spot")
        GPIO.output(PUMP_2_PIN, GPIO.LOW)
    elif class_index in [5, 7, 9]:  # Class 5, 7, 9: Tomato Spider mites, Tomato Yellow Leaf Curl Virus, Tomato Mosaic virus
        print("Running Pump 3 for Spider mites, Yellow Leaf Curl Virus, or Mosaic virus")
        GPIO.output(PUMP_3_PIN, GPIO.LOW)

    # Run the pump for a certain duration (adjust as needed)
    time.sleep(5)

    # Turn off all pumps
    GPIO.output(PUMP_1_PIN, GPIO.HIGH)
    GPIO.output(PUMP_2_PIN, GPIO.HIGH)
    GPIO.output(PUMP_3_PIN, GPIO.HIGH)

    # Cleanup GPIO to release resources
    GPIO.cleanup()

# Example usage:
run_pump(1)  # Run pump for class 1
