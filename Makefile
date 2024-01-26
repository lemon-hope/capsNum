
pythonPath = /home/lordcaf/.virtualenv-python/dev/bin/python # put here the path to your python env 

all: install run

run:
	$(pythonPath) /usr/bin/pyshared/main.py

install:
	echo "Installing dependencies pynput and notify-py..."
	$(pythonPath) -m pip install --upgrade pynput notify-py
	sudo mkdir -p /usr/bin/pyshared/ && sudo cp ./main.py /usr/bin/pyshared/main.py


uninstall:
	sudo rm -f /usr/bin/pyshared/main.py
	$(pythonPath) -m pip uninstall pynput notify-py
	echo "Done"