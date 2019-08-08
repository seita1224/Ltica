import gpiozero
import time

let = gpiozero.LED(4)
let.on()
time.sleep(3)
let.off()
