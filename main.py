from weather import ip_address
from weather import ip_location
from weather import weather
import time
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

repeat = False
root = tk.Tk()
root.geometry('800x800')
root.title("Temperature Recording")


def isfloat(input): #Used in user validation, checks if integer
    try:
        float(input)
        return True       #Returns true if an integer
    except ValueError:
        return False

def convert(number, root):
  if isfloat(number):
    print(number)
    global fahrenheit
    fahrenheit.destroy()
    converted = (float(number) * 1.8 + 32)
    print(converted)
    fahrenheit = tk.Label(root, text=str(converted))
    fahrenheit.place(x=50, y=430)
  else:
    tk.messagebox.showwarning(title="Invalid Input", message="The input needs to be a number!")

def help_window():
  help_window = tk.Toplevel()
  help_window.title("Help")
  help_window.geometry('600x400')
  tk.Label(help_window, text="Help").pack(side="top")
  tk.Label(help_window, text="Setup \m").pack(side="top")
  tk.Label(help_window, text="This program has been designed to be as plug and play as possible, however \n occasionally further setup may be required, if your temperature sensor is \n not set as the D: drive you should find the main.py file and change \n the directory to reflect your directory. \n").pack(side="top")
  tk.Label(help_window, text="Troubleshooting \n").pack(side="top")
  tk.Label(help_window, text="Temperature recordings are not updating - Delete temperature \n log from microcontroller, if the microcontrolloer runs out of storage nothing will update \n").pack(side="top")
  tk.Label(help_window, text="Temeprature data does not update - Try restarting the microcontroller \n (unplug it then plug it in again) some microcontrollers will not update the text file automatically.").pack(side="top")
  tk.Label(help_window, text="Multiple lines appear for the weather - This happens \n when the program is restarted and not shut down properly, delete the weather log and the program will automatically remake it").pack(side="top")
  tk.Label(help_window, text="Error message stating 'current' not found - this occurs \n when the API request limit has been reached, in future turn up the recording interval \n").pack(side="top")
  tk.Label(help_window, text="FAQs").pack(side="top")
  tk.Label(help_window, text="Why do sliders and temperature converisons take time to update? - Ensuring \n the graph is updated blocks any other commands from running").pack(side="top")

  
hours = [] #Defines key variables needed for main loop
temp = []
real_temp = []
timestamp = 0

#Code required to define the graph object
figure1 = plt.Figure(figsize=(5, 4), dpi=100)
ax1 = figure1.add_subplot(111)
line1 = ax1.plot(hours, temp , color='red', linestyle="solid", marker="X")
line2 = ax1.plot(hours, real_temp , color='blue', linestyle="solid", marker="X")
plt.show()

#Code to define warning sldiers
upper_warning = tk.Scale(root, from_=20, to=50, showvalue=1, orient="horizontal", tickinterval=10)
upper_warning.set(25)
upper_label = tk.Label(root, text=("Upper Limit"))
lower_warning = tk.Scale(root, from_=0, to=30, showvalue=1, orient="horizontal", tickinterval=10)
lower_warning.set(15)
lower_label = tk.Label(root, text=("Lower Limit"))
upper_warning.pack(anchor = "s")
upper_label.pack()
lower_warning.pack(anchor = "s")
lower_label.pack()

#Code to create interval slider
interval_slider = tk.Scale(root, from_=1, to=60, showvalue=1, orient="horizontal", tickinterval=20)
interval_label = tk.Label(root, text=("Recording Interval (Minutes)"))
interval_slider.pack(anchor = "s")
interval_label.pack()

#Creates conversion tool objects
tk.Label(root, text="Celsius:").place(x=0, y=390)
tk.Label(root, text="Fahrenheit:").place(x=0, y=410)
celsius_box = tk.Entry(root)
celsius_box.place(x=60, y=390)
celsius_box.insert(0,0)
fahrenheit = tk.Label(root, text=(32))
fahrenheit.place(x=80, y=410)

help_button = tk.Button(root, text="Help", command=help_window).place(x=10, y=10)

def graph(hours, temp, real_temp, repeat):
  global figure1
  global ax1
  global line1
  global line2
  
  if repeat == False:      #If the function is ran for the first time
    scatter1 = FigureCanvasTkAgg(figure1, root)
    scatter1.get_tk_widget().place(relx=0.6, rely=0.6, anchor="center")
    ax1.legend(['Outside Temperature','inside temeprature'])
    ax1.set_xlabel('Time')
    ax1.set_title('Temperature')
    
  #Section of code that will always run
  line1 = ax1.plot(hours, temp , color='red', linestyle="solid", marker="X")
  line2 = ax1.plot(hours, real_temp , color='blue', linestyle="solid", marker="X")
  figure1.canvas.draw()
  root.update()
  
while True:              
  ip = ip_address()
  location = ip_location(ip)
  temperature = weather(location)
  
  
  log = open("weather.txt", "a") #Writes temeprature data to log
  log.write(str(temperature) + "," + str(timestamp) + "\n")
  log.close()


  log = open("weather.txt", "r") #Reads weather data from log
  data = log.read()
  lines = data.splitlines()
  log.close()

  temp_log = open("D:\Temperature.txt", "r") #Reads temeprature data from log
  temp_data = temp_log.read()
  temp_lines = temp_data.splitlines()

  hours = []
  temp = []
  real_temp = []

  interval=(interval_slider.get() * 60)

  for e in temp_lines:
    real_temp.append(int(round(float(e)))) #Adds temperature data to array
  
  for i in lines:                   #Adds weather and timestamp data to array
    separate = i.split(",")
    temp.append(int(separate[0]))
    hours.append(int(separate[1]))

  while len(real_temp) < len(temp):  #Runs when weather array is longer than temperature array
    temp.pop()
    hours.pop()

  while len(real_temp) > len(temp):     #Code runs when temperature array is larger than weather array
    if len(real_temp) >= (len(temp) + interval):
      del real_temp[1:interval]
    else:
      real_temp.pop(0)
      

  graph(hours, temp, real_temp, repeat)
  repeat = True

  if real_temp[len(real_temp) - 1] > int(upper_warning.get()): #Code to initiate temperature alerts
    tk.messagebox.showwarning(title="Temperature Warning", message="The recorded temperature is above the specified limit")
  if real_temp[len(real_temp) - 1] < int(lower_warning.get()):
    tk.messagebox.showwarning(title="Temperature Warning", message="The recorded temperature is below the specified limit")
  
  timestamp += 1
  time.sleep(interval)

root.mainloop()



