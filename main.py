import time
from servo_control import initialize_servos, camera_angle, rotate_servo, cleanup_servos
from pump_control import run_pump, initialize_pumps
from camera import capture_image
from inference import inference
import RPi.GPIO as GPIO
from database import initialize_database, close_database_connection, insert_record

# Define GPIO pins for servo motors
CAMERA_SERVO_PIN = 16
NOZZLE_SERVO_PIN = 18

# Define LED pins
led_status = 17  # LED pin to indicate the program is running
led_disease = 19  # LED pin to indicate the disease is detected

GPIO.setup(led_status, GPIO.OUT)
GPIO.setup(led_disease, GPIO.OUT)

# Define angles for the servo to rotate
angles = [45, 90, 135]

# Initialize the database
conn, cursor = initialize_database()

# Initialize servo motors
servo_pwm_camera, servo_pwm_nozzle = initialize_servos(CAMERA_SERVO_PIN, NOZZLE_SERVO_PIN)
initialize_pumps()

try:
    while True:
        # Turn on led when program is running
        GPIO.output(led_status, GPIO.HIGH)

        for angle in angles:
            # Rotate camera servo to the desired angle
            rotate_servo(servo_pwm_camera, angle)
            time.sleep(2)  # Adjust this delay if needed

            # Capture an image
            image_path = capture_image()

            # Perform disease inference
            disease_class = inference(image_path)

            # Handle healthy plants (assuming 0 represents healthy)
            if disease_class != 2:
                # Flash the led when disease is detected
                GPIO.output(led_disease, GPIO.HIGH)
                # Aim the nozzle at the area where the disease was detected
                # current_camera_angle = camera_angle(servo_pwm_camera)
                rotate_servo(servo_pwm_nozzle, angle)

                # Activate the pump based on the disease class
                run_pump(disease_class)

                # Record data in the database
                plant_id = angles.index(angle) + 1
                insert_record(cursor, plant_id, disease_class)

                # Return nozzle servo to its middle position
                rotate_servo(servo_pwm_nozzle, 90)
                GPIO.output(led_disease, GPIO.LOW)

        GPIO.output(led_status, GPIO.LOW)

        # 60-second break after completing a cycle of inferences
        print("Taking a 60-second break...")
        time.sleep(60)

except KeyboardInterrupt:
    # Clean up servos and GPIO on program interruption (Ctrl+C)
    cleanup_servos(servo_pwm_camera, servo_pwm_nozzle)
    GPIO.cleanup()
    close_database_connection(conn)

finally:
    # Close the database connection on script termination
    close_database_connection(conn)
