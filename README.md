# Temperature-sensor

This is the code and log files for my computer science NEA.

The main.py and weather.py files should be stored on desktop and are designed to work on any devices. 
The boot.py and temperature.py files should be stored on the microcontroller used and have been configured to work on a raspberry pi pico with circuitpython installed

The only configuration needed before running this code is that the file pathway for the temperature log needs to be set
By default this has been set to D:/Temperature.txt as this should be the pathway for most users
If however you have a system drive as your D drive you should check what drive the microcontroller is set to and change the pathway accordingly.

There are a numebr of libraries that you will have to have instaleld should you wish to use this program these are:

- Ipinfo (which should install automatically)
- Tkinter - https://www.tutorialspoint.com/how-to-install-tkinter-in-python
- Matplotlib - https://matplotlib.org/stable/users/installing/index.html
- Requests - https://pypi.org/project/requests/

Each link should contain information as to how to dowload the package. All credit goes to the authors.
