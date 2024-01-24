 
"""
    A simple python script to detect the status of lock keys using python keyboard and notify-py modules.
    Tested using Arch Linux 
    author : lemonHope
"""
from pynput import keyboard 
import subprocess

capsLockKeyStatus = False  
numLockKeyStatus =  False

class 
def on_pressed(key):
    # verify the current status
    # 49 -> caps lock
    # 50 -> num lock
    # 51 -> caps lock + num lock   
    led = verify_lock_status()
    if key == keyboard.Key.caps_lock:
        if led == 49 or led == 51:
            capsLockKeyStatus = True
            print("you pressed caps lock key")
        else:
            print("Caps lock not pressed")
    elif key == keyboard.Key.num_lock:
        if led == 50 or led == 51:
            capsLockKeyStatus = False
            print("you pressed num lock key")
        else:
            apsLockKeyStatus = False
            print("num lock not activated")

    else:
        print("Not of interst")


def verify_lock_status():
    led = subprocess.check_output('xset q | grep LED', shell=True)[65]
    return led 

# add key listener
with keyboard.Listener(
    on_press=on_pressed
) as listener:
    try:
        listener.join()
    except :
        pass

