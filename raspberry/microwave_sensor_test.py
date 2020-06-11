import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

#초음파를 쏘는 핀!
trig = 2

#돌아오는 초음파를 듣는 핀!
echo = 3

#핀 입출력을 설정해주고!
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
    #무한 루프로 돌려서 계속 층정
    while True:
        GPIO.output(trig, GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(trig , GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trig, GPIO.LOW)

        while GPIO.input(echo) == GPIO.LOW:
            pulse_start = time.time()

        while GPIO.input(echo) == GPIO.HIGH:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        print( "distance : " , distance, "cm")

except KeyboardInterrupt:
    GPIO.cleanup()
