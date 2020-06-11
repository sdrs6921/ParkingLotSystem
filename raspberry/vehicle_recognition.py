#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time, socket, threading

GPIO.setmode(GPIO.BCM)

trig=3
echo=2

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
isEmpty = True

HOST = '192.168.22.97'
PORT = 9999

"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("connect!")
client.sendall("1\n".encode())
"""

#print("loop start")
while 1:
    try:
        GPIO.output(trig, False)
        time.sleep(3)
        
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        
        while GPIO.input(echo) == 0:
            pulse_start = time.time()
            
        while GPIO.input(echo) == 1:
            pulse_end = time.time()
            
        distance = (pulse_end - pulse_start) * 17000
        distance = round(distance, 2)
        
        if isEmpty and distance < 30:
            #car in
            isEmpty = False
            #client.sendall("A1:37가 1234\n".encode('utf-8'))
            print("Car in")
        elif not isEmpty and distance > 30:
            #car out
            isEmpty = True
            #client.sendall("A1:NULL\n".encode())
            print("Car out")
#        if distance < 30:
#            client.sendall("A1:37가 1234\n".encode('utf-8'))
#            print(str(distance) + "cm")
#        else:
#           client.sendall("A1:NULL\n".encode())
        
    except Exception as e:
        print(e)
        #GPIO.cleanup()
        break
        
GPIO.cleanup()
