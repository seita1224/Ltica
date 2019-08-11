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