from pynput import keyboard, mouse
from pynput.keyboard import Key, Listener as KeyboardListener
import random
import pyautogui
import threading

switch = False

def on_press(key):
    global switch
    if key == keyboard.Key.tab:
        switch = not switch
        start_mouse_movement() if switch else stop_mouse_movement()

def move_mouse():
    while switch:
        x = random.uniform(7.5,12.5)
        y = random.uniform(-0.0001,0.0001) 
        t = random.uniform(1.500,2.500)
        pyautogui.mouseDown()
        pyautogui.moveRel(x, y, duration=t)
        pyautogui.mouseUp()

def start_mouse_movement():
    global switch
    switch = True
    mouse_thread = threading.Thread(target=move_mouse) # Multi-Process
    mouse_thread.start()

def stop_mouse_movement():
    global switch
    switch = False

keyboard_listener = KeyboardListener(on_press=on_press)
keyboard_listener.start()
keyboard_listener.join()