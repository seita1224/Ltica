import time

compile_lib = ''
try:
    from blinkt import set_pixel, set_brightness, show, clear
    compile_lib = 'blinkt'
except ImportError:
    from compile.blinkt import set_pixel, set_brightness, show, clear
    compile_lib = 'compile.blinkt'

set_brightness(0.5)

clear()
set_pixel(0, 255, 0, 0)
show()

time.sleep(1)


#ここから新ソース
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(25, GPIO.OUT)

GPIO.output(25, GPIO.HIGH)
time.sleep(2) # この間は点灯し続ける

GPIO.cleanup() # <- 消灯
