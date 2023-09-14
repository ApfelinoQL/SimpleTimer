import sys
import time
import tkinter as tk
from tkinter import messagebox

def Countdown(Time):
    def exit_program():
        if messagebox.askokcancel("Exit", "Do you really want to exit the Timer?"):
            root.destroy()
    def start_program(Time):
        Time = int(Time)
        while Time > -1:
            if Time >= 10:
                root.update()
                LTime.config(text="0:" + str(Time))
                print("0:" + str(Time))
                Time -= 1
                root.after(1000)
            else:
                root.update()
                LTime.config(text="0:0" + str(Time))
                print("0:0" + str(Time))
                Time -= 1
                root.after(1000)
        while True:
            print("Time Over!")
            LTime.config(text="Time Over!")
            break
    print(Time)
    root = tk.Tk()
    root.title("Timer")

    s_button = tk.Button(root, text="Start", command=lambda: start_program(Time))
    s_button.pack(padx=20, pady=5)

    LTime = tk.Label(root, text="Start Timer")
    LTime.pack(padx=20, pady=5)

    root.protocol("WM_DELETE_WINDOW", exit_program)

    root.mainloop()

