from tkinter import *
from tkinter import ttk
import psutil 
from psutil._common import BatteryTime
import datetime
import time

root = Tk()
root.geometry('500x250')
root.config(bg="black")
root.overrideredirect(True)
style = ttk.Style(root)
style.layout('ProgressiveBarStyle',
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side':'right','sticky':'ns'})],
                'sticky':'nsnew'}),
              ('Horizontal.Progressbar.label',{'stick':'ns'})])
bar=ttk.Progressbar(root, maximum=100, style='ProgressiveBarStyle')
bar.place(relx=0.5, rely=0.2, anchor=CENTER)


battery_life = Label(root, font = 'arial 15 bold', bg ='black', fg="white")
battery_life.place(relx=0.5,rely=0.5, anchor=CENTER)

def convertTime(seconds):
    get_time = time.gmtime(seconds)
    time_remain = time.strftime("%H:%M:%S",get_time )
    return time_remain

def getBatteryLife():
    battery = psutil.sensors_battery()
    bar['value'] = battery.percent
    style.configure('ProgressiveBarStyle', text=str(battery.percent)+' %')
    battery_left= convertTime(battery.secsleft)
    if battery.secsleft == BatteryTime.POWER_TIME_UNLIMITED:
        battery_life['text']='Unplug the battery'
    elif battery.secsleft == BatteryTime.POWER_TIME_UNKNOWN:
        battery_life['text']='Battery life not detected.'
    else:
        battery_life['text'] = "Battery Life: "+battery_left
        root.after(1000, getBatteryLife)
getBatteryLife()

root.mainloop()



