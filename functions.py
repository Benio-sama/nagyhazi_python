import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_if_0(value, menu, value_list):
    if value == '0':
        print("Vissza a menübe.")
        time.sleep(1)
        clear_console()
        menu(value_list)
    return 