##open web browser
##ctrl + C in shell window to stop program

import webbrowser
import time

total_break = 3
break_count = 0

print("This program started on " + time.ctime())  ##ctime shows the recent computer time
while (break_count < total_break):
    time.sleep(10)  ##number in seconds
    webbrowser.open("https://www.youtube.com/watch?v=8-VZKL4EBKs")
    break_count = break_count + 1
