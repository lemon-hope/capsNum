# CAPSNUM

My computer doesn't have a way to see the current status of **Lock  keys (Caps lock and Num lock)** so I decided to build this python script to do the job.


## How to install and run  

First, make sure  that you have a running python venv and set the  path to it as a value of the variable `pythonPath` in the **Makefile** .
To set up and run, you can use `make install && make run` that will install all required dependencies and run the script. Or you can install the dependencies `pynput and notify-py` by your self then run the script using python.


## Screenshots
![Alt text](./images/image_1.png)  

![Alt text](./images/image_2.png)


## Known bugs/limitations

This script uses a threading.Thread listener to listen for keyboard events, and it should not be used as a keylogger.

## Extra

Create a job to automatically run the script at startup with systemd.
Create a file `sudo touch /etc/systemd/system/lockkeys.service` and add the following lines :



```
[Unit]
Description=Track lock key status with python

[Service]
ExecStart=/path/to/virtualenv/ /path/to/script.py

[Install]
WantedBy=multi-user.target 

```




