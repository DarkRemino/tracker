# Fryon's Universal Package Tracker

## What is this?

A web application written in Flask used to track deliveries from many different vendors around the globe.

## How do I run it?

You'll need a Python environment with all the requirements in requirements.txt installed

#### Note to self
The MariaDB Connector/Python works in mysterious ways and thus, it
needs to be installed as separate versions for Windows and Linux.
This happens because of a compatability issue between the newest 
C++ build tools for Visual Studio and the older version that most Linux
distros currently support (matter of fact, Fedora 40 is the only one that
supports the newest versions (>=1.1.0) of the Python connector).
Because of this, the version listed in requirements.txt will be the OLDER
one, since this is a service meant to run flawlessly on a Linux machine.
if you have problems after installing the requirements on Windows, just run
``` pip install --upgrade mariadb``` and it should fix the issue.