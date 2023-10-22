#python3

import pyautogui #package for contraol mouse
import keyboard #package for contraol keyboard
import time
import random

time.sleep(6) #set time to get ready

while not keyboard.is_pressed('esc'):
    v = random.randint(-1,1)
    x = random.uniform(6.5,13.5)*v
    v = random.randint(-1,1)
    y = random.uniform(7.5,12.5)*v
    t = random.uniform(2.500,3.500)

    pyautogui.moveRel(x, y, duration=t)