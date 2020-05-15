Roboterflut command interface and drivers
=========================================


Installation
------------

> git clone url... roboterflut
> cd roboterflut
> python3 -m venv .
> bin/pip install -f requirements.txt


Configuration
-------------

For now, edit wsserver.py and add your bot config(s).


Running
-------


1. Websocket Server

> bin/python wsserver.py


2. Web Frontend

The Web Frontend is just static html. Use a proper webserver or just fire
up a minimal one serving just the "www" directory:

> cd www
> python3 -m http.server -b localhost 8080

Access http://localhost:8080 in your browser.


Writing your own driver
-----------------------

See rc_control.py/udp_control.py for an example. You have to specify a class which implements "steer" and "motor" methods, each with one argument. The Argument is an int ranging from -200 to 200. 

