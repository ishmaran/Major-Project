import time
from servo_control import initialize_servos, camera_angle, rotate_servo, cleanup_servos
from pump_control import run_pump
from camera import capture_image
from inference import inference

# Define GPIO pins for pumps
PUMP_1_PIN = 22
PUMP_2_PIN = 24
PUMP_3_PIN = 26

# Define GPIO pins for servo motors
CAMERA_SERVO_PIN = 16
NOZZLE_SERVO_PIN = 18

# Define angles for the servo to rotate
angles = [45, 90, 135]

# Initialize servo motors
servo_pwm_camera, servo_pwm_nozzle = initialize_servos(CAMERA_SERVO_PIN, NOZZLE_SERVO_PIN)



while True:
    try:
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
                # Aim the nozzle at the area where the disease was detected
                #current_camera_angle = camera_angle(servo_pwm_camera)  
                rotate_servo(servo_pwm_nozzle, angle) 

                # Activate the pump based on the disease class
                run_pump(disease_class)

                # Return nozzle servo to its middle position
                rotate_servo(servo_pwm_nozzle, 90) 

        # 60 second break after completing a cycle of inferences
        print("Taking a 60-second break...") 
        time.sleep(60)

    finally:
        # Ensure servos and GPIO are cleaned up 
        cleanup_servos(servo_pwm_camera, servo_pwm_nozzle) 
