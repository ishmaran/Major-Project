import RPi.GPIO as GPIO
import pigpio
import time

#Initialize the servo to 90 degree
def initialize_servos(camera_servo_pin, nozzle_servo_pin):
    pi = pigpio.pi()
    pi.set_mode(camera_servo_pin, pigpio.OUTPUT)
    pi.set_mode(nozzle_servo_pin, pigpio.OUTPUT)
    
    # Set servo to the middle position
    pi.set_servo_pulsewidth(camera_servo_pin, 1500)
    pi.set_servo_pulsewidth(nozzle_servo_pin, 1500)
    
    time.sleep(2)  # Allow time for the servo to reach the middle position
    return pi

def get_camera_servo_angle(pi, camera_servo_pin):
    pulse_width = pi.get_servo_pulsewidth(camera_servo_pin)
    angle = ((pulse_width - 1000) / 1000) * 180
    return angle

def rotate_servo(pi, servo_pin, angle):
    pulse_width = int(((angle / 180) * 1000) + 1000)
    pi.set_servo_pulsewidth(servo_pin, pulse_width)
    time.sleep(1)  # Adjust this sleep time as needed
