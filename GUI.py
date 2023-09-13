import tkinter as tk
import time
import TimerScript

# Function to excecute when Startbutton is clicked

def Viewbuttonclick():
    SecondsTime = ST.get()
    MinutesTime = MT.get()
    if int(SecondsTime) < 10:
        TimeDis.config(text=str(MinutesTime) + ":0" + str(SecondsTime))
    else:
        TimeDis.config(text=str(MinutesTime) + ":" + str(SecondsTime))

def Startbuttonclick():
    SecondsTime = ST.get()
    MinutesTime = MT.get()
    if int(SecondsTime) < 10:
        TimeDis.config(text="Starting with " + str(MinutesTime) + ":0" + str(SecondsTime))
        TimerScript.TS(MinutesTime, SecondsTime)
    else:
        TimeDis.config(text="Starting with " + str(MinutesTime) + ":" + str(SecondsTime))
        TimerScript.TS(MinutesTime, SecondsTime)

def MinuteSTimeleft(MT,ST):
    if int(ST) < 10:
        TimeDis.config(text="Starting with " + str(MT) + ":0" + str(ST))
    else:
        TimeDis.config(text="Starting with " + str(MT) + ":" + str(ST))

def SecondSTimeleft(ST):
    if int(ST) < 10:
        TimeDis.config(text="Starting with 0:0" + str(ST))
    else:
        TimeDis.config(text="Starting with 0:" + str(ST))

root = tk.Tk()
root.title("BetterTimer")

MTL = tk.Label(root, text="Minutes")
MTL.pack()

MT = tk.Entry(root)
MT.pack()

STL = tk.Label(root, text="Seconds")
STL.pack()

ST = tk.Entry(root)
ST.pack()

Viewbutton = tk.Button(root, text="View", command=Viewbuttonclick)
Viewbutton.pack()

Startbutton = tk.Button(root, text="Start", command=Startbuttonclick)
Startbutton.pack()

TimeDis = tk.Label(root, text="")
TimeDis.pack()

Timeleft = tk.Label(root, text="")
Timeleft.pack()


root.mainloop()

