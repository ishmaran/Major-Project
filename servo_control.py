import RPi.GPIO as GPIO
import time

def initialize_servos(camera_servo_pin, nozzle_servo_pin):
    """Initializes servo motors on the specified GPIO pins.

    Args:
        camera_servo_pin: The GPIO pin connected to the camera servo.
        nozzle_servo_pin: The GPIO pin connected to the nozzle servo.

    Returns:
        A tuple containing the PWM objects for the camera and nozzle servos.
    """

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(camera_servo_pin, GPIO.OUT)
    GPIO.setup(nozzle_servo_pin, GPIO.OUT)

    servo_pwm_camera = GPIO.PWM(camera_servo_pin, 50)  # 50 Hz frequency
    servo_pwm_nozzle = GPIO.PWM(nozzle_servo_pin, 50)  

    servo_pwm_camera.start(7.5)  # Initial position (assuming 90 degrees)
    servo_pwm_nozzle.start(7.5)  

    time.sleep(2)  # Delay for servos to reach initial position

    return servo_pwm_camera, servo_pwm_nozzle

def rotate_servo(servo_pwm, target_angle):
    """Rotates a servo motor to a specified angle.

    Args:
        servo_pwm: The PWM object controlling the servo.
        target_angle: The desired angle in degrees (0-180).
    """

    if 0 <= target_angle <= 180:
        duty_cycle = target_angle / 18 + 2
        servo_pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(2)  # Adjust this delay as needed 
    else:
        print("Invalid angle. Servo angles must be between 0 and 180 degrees.")

def camera_angle(servo_pwm):
    """Calculates the current angle of a servo.

    Args:
        servo_pwm: The PWM object controlling the servo.

    Returns:
        The current servo angle in degrees.
    """

    current_duty_cycle = servo_pwm.get_duty_cycle()
    angle = ((current_duty_cycle - 2) * 18) / 1 + 2
    return angle

def cleanup_servos(servo_pwm_camera, servo_pwm_nozzle):
    """Stops the servo motors and cleans up GPIO resources."""

    servo_pwm_camera.stop()
    servo_pwm_nozzle.stop()
    GPIO.cleanup() 
