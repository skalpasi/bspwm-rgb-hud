from pynput.keyboard import Key, Listener
import os
import random

def on_press(key):
    if key:
        random_number1 = random.randint(0,16777215)
        random_number2 = random.randint(0,16777215)
        hex_number1 = str(hex(random_number1))
        hex_number1 = '\#'+ hex_number1[2:]
        hex_number2 = str(hex(random_number2))
        hex_number2 = '\#'+ hex_number2[2:]
        command1 = 'sudo bspc config normal_border_color '+hex_number1
        command2 = 'sudo bspc config focused_border_color '+hex_number2
        os.system(command1)
        os.system(command2)

def on_release(key):
     pass

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

