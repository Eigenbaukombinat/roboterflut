import RPi.GPIO as GPIO
import struct
import time
import socket

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


UDP_IP = "192.168.0.98"
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))



A1A = 17
A1B = 27

B1A = 22
B1B = 23

GPIO.cleanup()

def init_motors():
    GPIO.setup(A1A, GPIO.OUT)
    GPIO.output(A1A, GPIO.LOW)
    GPIO.setup(A1B, GPIO.OUT)
    GPIO.output(A1B, GPIO.LOW)
    GPIO.setup(B1A, GPIO.OUT)
    GPIO.output(B1A, GPIO.LOW)
    GPIO.setup(B1B, GPIO.OUT)
    GPIO.output(B1B, GPIO.LOW)

def test_motors():
    print("Forward")
    #links
    GPIO.output(A1A,GPIO.HIGH)
    GPIO.output(A1B,GPIO.LOW)
    #rechts
    GPIO.output(B1A,GPIO.LOW)
    GPIO.output(B1B,GPIO.HIGH)
    time.sleep(2)
    print("Backward")
    #links
    GPIO.output(A1A,GPIO.LOW)
    GPIO.output(A1B,GPIO.HIGH)
    #rechts
    GPIO.output(B1A,GPIO.HIGH)
    GPIO.output(B1B,GPIO.LOW)
    time.sleep(2)

def left_fwd():
    GPIO.output(A1A,GPIO.HIGH)
    GPIO.output(A1B,GPIO.LOW)


def left_stop():
    GPIO.output(A1A,GPIO.LOW)
    GPIO.output(A1B,GPIO.LOW)

def left_bck():
    GPIO.output(A1A,GPIO.LOW)
    GPIO.output(A1B,GPIO.HIGH)

def right_fwd():
    GPIO.output(B1A,GPIO.LOW)
    GPIO.output(B1B,GPIO.HIGH)

def right_stop():
    GPIO.output(B1A,GPIO.LOW)
    GPIO.output(B1B,GPIO.LOW)

def right_bck():
    GPIO.output(B1A,GPIO.HIGH)
    GPIO.output(B1B,GPIO.LOW)


def quit():
    GPIO.cleanup()
    quit()



init_motors()
left_stop()
right_stop()



while True:
    throttle = 0
    direct = 'center'
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print ("received message:")
    mode, value = struct.unpack('ii', data)
    print((mode, value))
    if mode == 1:
        #throttle
        if value > 95:
            throttle = -1
        elif value < 85:
            throttle = 1
        else:
            throttle = 0
    elif mode == 2:
        if value < 70:
            direct = 'left'
        elif value > 110:
            direct = 'right'

    if throttle == 1:
        if direct == 'left':
            left_fwd()
            right_stop()
        elif direct == 'right':
            left_stop()
            right_fwd()
        else:
            left_fwd()
            right_fwd()
    elif throttle == 0:
        if direct == 'right':
            left_fwd()
            right_bck()
        elif direct == 'left':
            left_bck()
            right_fwd()
        else:
            left_stop()
            right_stop()
    elif throttle == -1:
        if direct == 'right':
            left_bck()
            right_stop()
        elif direct == 'left':
            left_stop()
            right_bck()
        else:
            left_bck()
            right_bck()



