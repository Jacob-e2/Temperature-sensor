# Temperature-sensor

This is the code and log files for my computer science NEA.

The main.py and weather.py files should be stored on desktop and are designed to work on any devices. 
The boot.py, settings.txt and code.py files should be stored on the microcontroller used and have been configured to work on a raspberry pi pico with circuitpython installed

The only configuration needed before running this code is that the file pathway for the temperature log needs to be set
By default this has been set to D:/Temperature.txt as this should be the pathway for most users
If however you have a system drive as your D drive you should check what drive the microcontroller is set to and change the pathway accordingly.

There are a numebr of libraries that you will have to have instaleld should you wish to use this program these are:

- Ipinfo (which should install automatically)
- Tkinter - https://www.tutorialspoint.com/how-to-install-tkinter-in-python
- Matplotlib - https://matplotlib.org/stable/users/installing/index.html
- Requests - https://pypi.org/project/requests/

Each link should contain information as to how to dowload the package. All credit goes to the authors.

It should also be noted that by default the user is unable to edit files which are stored on the microcontroller due to the code stored within the boot.py file.
If you do wish to make any changes to the data stored on the microcontroller instructions onhow to do this can be found at the following website

https://learn.adafruit.com/cpu-temperature-logging-with-circuit-python/writing-to-the-filesystem

Once again all credit goes to the author

This code will only work with a temperature sensor that is compatible with the I2C protocol, it should be noted that the SDA and SCL have been set to pins 1 and 0 respectively,
but this can be changed in the code.py file. Most I2C tmeprature sensors also have a power and ground connection but this can be connected to any appropriate pin.
