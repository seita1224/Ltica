compile_lib = ''
try:
    from blinkt import set_pixel, set_brightness, show, clear
    compile_lib = 'blinkt'
except ImportError:
    from compile.blinkt import set_pixel, set_brightness, show, clear
    compile_lib = 'compile.blinkt'


clear()
set_pixel(0, 255, 255, 255)
show()
