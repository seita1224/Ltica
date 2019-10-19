import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(2, GPIO.OUT)

for i in range(10):
    time.sleep(1)  # この間は点灯し続ける
    GPIO.output(2, GPIO.HIGH)
    time.sleep(1) # この間は点灯し続ける
    GPIO.cleanup()  # <- 消灯






