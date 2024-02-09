import time
from servo_control import initialize_servos, get_camera_servo_angle, rotate_servo
from pump_control import run_pump
from camera import capture_image
from inference

# Define GPIO pins for pumps
PUMP_1_PIN = 22
PUMP_2_PIN = 24
PUMP_3_PIN = 26

# Define GPIO pins for servo motors
CAMERA_SERVO_PIN = 16
NOZZLE_SERVO_PIN = 18

# Define angles for the servo to rotate
angle = [45, 90, 135]

# Initialize servo motors
pi = initialize_servos(CAMERA_SERVO_PIN, NOZZLE_SERVO_PIN)




rotate_servo(pi, CAMERA_SERVO_PIN, target_angle)


