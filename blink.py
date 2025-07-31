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
<<<<<<< HEAD
print("blink finished ! ")
=======
print("blink finished !")

>>>>>>> 20aba34d9b889a6e5c7cafd4e16c4ceff0616144


