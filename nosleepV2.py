# Created by Mr-Competent
# This Program will make sure your Screen doesn't go in SLEEP Mode.

import os
import pyautogui
import threading
import keyboard

pyautogui.FAILSAFE = False
screen_size = list(pyautogui.size())

def mouse_control():
    pyautogui.moveTo(screen_size[0],screen_size[1],0)
    while True:
        pyautogui.moveTo(screen_size[0], screen_size[1], duration = 60*4.5)

def check_input_space():
    keyboard.wait('space')
    print_In_Cyan("Thank You for using a script created by Mr-Competent!!!\n")
    os._exit(0)

def check_input_escape():
    keyboard.wait('esc')
    print_In_Cyan("Thank You for using a script created by Mr-Competent!!!\n")
    os._exit(0)

def print_In_Red(skk): print("\033[91m {}\033[00m" .format(skk)) 
def print_In_Green(skk): print("\033[92m {}\033[00m" .format(skk)) 
def print_In_Cyan(skk): print("\033[96m {}\033[00m" .format(skk)) 

mouse_control_thread = threading.Thread(target=mouse_control)
input_space_thread = threading.Thread(target=check_input_space)
input_escape_thread = threading.Thread(target=check_input_escape)

print("\n\033[92m *************************************************")
print_In_Cyan("\033[1m*********** Created by Mr-Competent ***********")
print("\033[92m *************************************************")
print("\nCheck out my Git repo here: \033[96m https://github.com/Mr-Competent/")
print_In_Red("\n***WARNING:This program will block mouse movement.\n")
print_In_Green("To STOP this program enter SPACE or ESCAPE.\n")

mouse_control_thread.start()
input_space_thread.start()
input_escape_thread.start()




