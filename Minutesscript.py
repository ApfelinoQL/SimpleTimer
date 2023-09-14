import sys
import time
import tkinter as tk
from tkinter import messagebox

def Countdown(MT, ST):
    def exit_program():
        if messagebox.askokcancel("Exit", "Do you really want to exit the Timer?"):
            root.destroy()
    def start_program(MT, ST):
        MT = int(MT)
        ST = int(ST)
        while MT > -1:
            if ST >= 10:
                LTime.config(text=str(MT) + ":" + str(ST))
                print(str(MT) + ":" + str(ST))
                ST -= 1
                root.update()
                root.after(1000)
            else:
                LTime.config(text=str(MT) + ":0" + str(ST))
                print(str(MT) + ":0" + str(ST))
                ST -= 1
                if ST == -1:
                    MT -= 1
                    ST = 59
                root.update()
                root.after(1000)
        while True:
            print("Time Over!")
            LTime.config(text="Time Over!")
            break
    print(str(MT) + ":" + str(ST))
    root = tk.Tk()
    root.title("Timer")

    s_button = tk.Button(root, text="Start", command=lambda: start_program(MT, ST))
    s_button.pack(padx=20, pady=5)

    LTime = tk.Label(root, text="Start Timer")
    LTime.pack(padx=20, pady=5)

    root.protocol("WM_DELETE_WINDOW", exit_program)

    root.mainloop()

