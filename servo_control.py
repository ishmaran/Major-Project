import RPi.GPIO as GPIO
import time

def initialize_servos(camera_servo_pin, nozzle_servo_pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(camera_servo_pin, GPIO.OUT)
    GPIO.setup(nozzle_servo_pin, GPIO.OUT)
    
    servo_pwm_1 = GPIO.PWM(camera_servo_pin, 50)  # 50 Hz frequency
    servo_pwm_2 = GPIO.PWM(nozzle_servo_pin, 50)  # 50 Hz frequency
    
    servo_pwm_1.start(7.5)  # Initial position for 90 degrees
    servo_pwm_2.start(7.5)  # Initial position for 90 degrees
    
    time.sleep(2)  # Allow time for the servos to reach the initial position
    
    return servo_pwm_1, servo_pwm_2

def rotate_servo(servo_pwm, angle):
    duty_cycle = angle / 18 + 2
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(2)  # Adjust this sleep time as needed

def get_camera_servo_angle(servo_pwm):
    current_duty_cycle = servo_pwm.get_duty_cycle()
    angle = ((current_duty_cycle - 2) * 18) / 1 + 2
    return angle

def cleanup_servos(servo_pwm_1, servo_pwm_2):
    servo_pwm_1.stop()
    servo_pwm_2.stop()
    GPIO.cleanup() 