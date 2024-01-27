
"""
    A simple python script to detect the status of lock keys(Caps lock and num lock) using python keyboard and notify-py modules.
    Tested using Arch Linux with KDE plasma 
    author : lemonHope
"""
from pynput import keyboard 
import subprocess
from notifypy import Notify
import logging


capsLockKeyStatus = False
numLockKeyStatus = False

# logger configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

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
    
    logging.info('Sending notification')
    notification.send()


def on_press(key):
    # verify the current status
    # 49 -> caps lock
    # 50 -> num lock
    # 51 -> caps lock + num lock
    logging.warn('Key event detected ')   
    global capsLockKeyStatus, numLockKeyStatus 
    if key == keyboard.Key.caps_lock:
        if capsLockKeyStatus == False :
            capsLockKeyStatus = True
            logging.info('Caps lock turned on')
            
        else:
            capsLockKeyStatus = False
            logging.info('Caps lock turned off')
        send_notification("caps lock", capsLockKeyStatus)
    if key == keyboard.Key.num_lock:
        if  numLockKeyStatus == False:
            numLockKeyStatus = True
            logging.info('Num lock turned on')
        else:
            numLockKeyStatus  = False
            logging.info('Num lock turned on')
        send_notification("num lock", numLockKeyStatus )


def get_lock_status():
    led = subprocess.check_output('xset q | grep LED', shell=True)[65]
    return led 

def set_lock_status(led):
    if led == 49:
        capsLockKeyStatus = True
        numLockKeyStatus = False
    elif led == 50:
        numLockKeyStatus = True
        capsLockKeyStatus = False
    elif led==51:
        numLockKeyStatus = True
        capsLockKeyStatus = True
    else:
        numLockKeyStatus = False
        capsLockKeyStatus = False  

led = get_lock_status()

set_lock_status(led)

# add key listener
with keyboard.Listener(
    on_press=on_press
) as listener:
    try:
        listener.join()
    except Exception as error :
        logging.error('Error occured with the listener', exc_info=error)


