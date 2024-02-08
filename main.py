import time
from servo_control import initialize_servos, get_camera_servo_angle, rotate_servo
from pump_control import run_pump

# Define GPIO pins for pumps
PUMP_1_PIN = 22
PUMP_2_PIN = 24
PUMP_3_PIN = 26

# Define GPIO pins for servo motors
CAMERA_SERVO_PIN = 16
NOZZLE_SERVO_PIN = 18

# Initialize servo motors
pi = initialize_servos(CAMERA_SERVO_PIN, NOZZLE_SERVO_PIN)

# Move the camera servo to a 45-degree angle
target_angle = 45
rotate_servo(pi, CAMERA_SERVO_PIN, target_angle)
