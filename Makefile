
pythonPath=/path/to/python/env # put here the path to python env 

all: install run

run:
	$(pythonPath) /usr/bin/pyshared/lock_status.py

install:
	echo "Installing dependencies pynput and notify-py..."
	$(pythonPath) -m pip install --upgrade pynput notify-py
	sudo mkdir -p /usr/bin/pyshared/ && sudo cp ./lock_status.py /usr/bin/pyshared/lock_status.py


uninstall:
	sudo rm -f /usr/bin/pyshared/lock_status.py
	$(pythonPath) -m pip uninstall pynput notify-py
	echo "Done"