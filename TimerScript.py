import time
import Minutesscript
import Secondsscript
import sys
import os

filler = True

def TS(SMinutesTime, SSecondsTime):
    while True:
        exit_requested = False
        print(SMinutesTime + " " + SSecondsTime)
        MinutesTime = int(SMinutesTime)
        SecondsTime = int(SSecondsTime)
        if MinutesTime >= 0 and SecondsTime >= 0:
            print("Negative values check")

            if MinutesTime == 0 and SecondsTime == 0:
                print("Both 0 check")
                exit_requested = True

            if MinutesTime == 0:
                print("SSScript starting")
                Secondsscript.Countdown(SecondsTime)
                if os.path.exists("SSExit_flag.txt"):
                    print("SS exist")
                    exit_requested = True

            else:
                print("MSScript starting")
                Minutesscript.Countdown(MinutesTime,SecondsTime)
                if os.path.exists("MSExit_flag.txt"):
                    print("MS exist")
                    exit_requested = True

        else:
            print("Negative value.")
            time.sleep(99999)

        if exit_requested:
            print("requested check")
            break

    print("Existing...")





