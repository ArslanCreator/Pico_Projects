from machine import Pin
from time import sleep
led = Pin(25, Pin.OUT)
button = Pin(14,Pin.IN,Pin.PULL_DOWN)
while True:
    user_input = input("Enter the value :") 
    if (user_input == "1"):
        led.value(1)
        print(f"Led state{user_input} ")
    elif (user_input == "0" ):
        led.value(0)
        print(f"Led state{user_input}")
    else: 
        print(f"Input invalde ! {user_input}") 