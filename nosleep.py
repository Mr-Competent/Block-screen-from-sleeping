# Created by Mr-Competent
# This Program will make sure your Screen doesn't go in SLEEP Mode.

import os
import time
import threading
import keyboard

def wakeup():
    while True:
        keyboard.press_and_release('f13')  # f13 key is not assigned to some function by default
        time.sleep(260)
        
def check_input_escape():
    keyboard.wait('esc')
    print_In_Cyan("Thank You for using a script created by Mr-Competent!!!")
    print("\n*************************************************")
    print_In_Cyan("\033[1m*********** Created by Mr-Competent ***********")
    print("*************************************************")
    os._exit(0)


def print_In_Green(skk): print("\033[92m {}\033[00m" .format(skk)) 
def print_In_Cyan(skk): print("\033[96m {}\033[00m" .format(skk)) 

wakeup_thread = threading.Thread(target=wakeup)
input_escape_thread = threading.Thread(target=check_input_escape)

print("\n*************************************************")
print_In_Cyan("\033[1m*********** Created by Mr-Competent ***********")
print("*************************************************")
print_In_Green("To STOP this program press ESCAPE.\n")

wakeup_thread.start()
input_escape_thread.start()