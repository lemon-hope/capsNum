 
"""
    A simple python script to detect the status of lock keys using python keyboard and notify-py modules.
    Tested using Arch Linux 
    author : lemonHope
"""
from pynput import keyboard 
import subprocess
from notifypy import Notify

capsLockKeyStatus = False  
numLockKeyStatus =  False


# handle notififcations
def send_notification(type, status):
    notification = Notify()
    #for caps lock
    if type=="caps lock" and status == True:
        notification.title = "Caps lock event detected"
        notification.message = "Caps lock turned ON"
        notification.icon = "./icons/CapsLock_On.png"
    elif type=="caps lock" and status == False:
        notification.title = "Caps lock event detected"
        notification.message = "Caps lock turned OFF"
        notification.icon = "./icons/CapsLock_Off.png"
    else:
        if type=="num lock" and status == True:
            notification.title = "Num lock event detected"
            notification.message = "Num lock turned ON"
            notification.icon = "./icons/NumLock_On.png"
        elif type=="num lock" and status == False:
            notification.title = "Num lock event detected"
            notification.message = "Num lock turned OFF"
            notification.icon = "./icons/NumLock_Off.png"
        else:
            pass
    
    notification.send()
    return 


def on_press(key):
    # verify the current status
    # 49 -> caps lock
    # 50 -> num lock
    # 51 -> caps lock + num lock   
    led = verify_lock_status()
    if key == keyboard.Key.caps_lock:
        if led == 49 or led == 51:
            capsLockKeyStatus = False
            print("you pressed caps lock key" + " " +str(verify_lock_status()))
            
        else:
            capsLockKeyStatus = False
            print("Caps lock not pressed"+ " " +str(verify_lock_status()))
        send_notification("caps lock", capsLockKeyStatus)
    elif key == keyboard.Key.num_lock:
        if led == 50 or led == 51:
            capsLockKeyStatus = False
            print("you pressed num lock key")
        else:
            apsLockKeyStatus = False
            print("num lock not activated")
        send_notification("num lock", capsLockKeyStatus)

    else:
        print("Not of interst")


def verify_lock_status():
    led = subprocess.check_output('xset q | grep LED', shell=True)[65]
    return led 

# add key listener
with keyboard.Listener(
    on_press=on_press
) as listener:
    try:
        listener.join()
    except :
        pass

