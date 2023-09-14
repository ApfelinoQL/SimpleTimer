import tkinter as tk
import Secondsscript
import Minutesscript
import time

def Setbuttonclick():
    SecondsTime = ST.get()
    MinutesTime = MT.get()
    try:
        int(SecondsTime)
        int(MinutesTime)
    except ValueError:
        pass
    else:
        if SecondsTime == "" or MinutesTime == "":
            pass
        elif int(SecondsTime) <= -1 or int(MinutesTime) <= -1:
            pass
        elif int(SecondsTime) == 0 and int(MinutesTime) == 0:
            pass

        else:
            if int(SecondsTime) < 10:
                TimeDis.config(text="Timer set with " + str(MinutesTime) + ":0" + str(SecondsTime))
            else:
                TimeDis.config(text="Timer set with " + str(MinutesTime) + ":" + str(SecondsTime))
            while True:
                print(str(MinutesTime) + " " + str(SecondsTime))
                if int(MinutesTime) == 0:
                    print("SSScript starting")
                    root.after(500)
                    ST.delete(0, tk.END)
                    Secondsscript.Countdown(SecondsTime)
                else:
                    print("MSScript starting")
                    root.after(500)
                    ST.delete(0, tk.END)
                    MT.delete(0, tk.END)
                    Minutesscript.Countdown(MinutesTime, SecondsTime)
    print("Invalid values")
    TimeDis.config(text="Invalid values! Try again")

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

Setbutton = tk.Button(root, text="Set Timer", command=Setbuttonclick)
Setbutton.pack()

TimeDis = tk.Label(root, text="")
TimeDis.pack()

root.protocol("WM_DELETE_WINDOW", root.destroy)

root.mainloop()