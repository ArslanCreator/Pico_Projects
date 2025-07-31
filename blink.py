from machine import Pin 
import time 
led = Pin(25, Pin.OUT)

for i in range (10):
    led.value(1)
    print ("led on")
    time.sleep(0.2)
    led.value(0)
    print ("led off")
    time.sleep(0.2)




