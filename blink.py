from machine import Pin
import time
count = 0
sum = {}
led = Pin(25, Pin.OUT)
button = Pin(14, Pin.IN)
led_state = False

while True:
    if button.value():
        time.sleep(0.2)  # Debounce
        led_state = not led_state
        led.value(led_state)
        count = count + 1
        sum.update({'led_state': led_state, 'count': count})
        print(sum)
        while button.value():  # Wait until release
            time.sleep(0.01)
