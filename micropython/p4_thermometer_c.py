from microbit import *

while True:
    reading = pin1.read_analog()
    temp_c = reading * 0.157 - 54
    display.scroll(str(temp_c))
    