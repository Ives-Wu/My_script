#python3

import pyautogui #package for contraol mouse
import keyboard #package for contraol keyboard
import time
import random

time.sleep(6) #set time to get ready

while not keyboard.is_pressed('esc'):
    x = random.uniform(7.5,12.5)
    t = random.uniform(1.500,2.500)
    pyautogui.mouseDown()
    pyautogui.moveRel(x, 0, duration=t)
    pyautogui.mouseUp()
