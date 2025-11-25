import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_if_0(value, menu, *args):
    if (isinstance(value, list) and '0' in value) or (isinstance(value, float) and value == 0) or value == '0':
        print("Vissza a menübe.")
        time.sleep(1)
        clear_console()
        menu(*args)
    return 

def back_to_menu(menu, *args):
    time.sleep(1)
    clear_console()
    menu(*args)

def conversion(item, new_unit: str) -> float:
        conversions = {
            ('g', 'kg'): 0.001,
            ('g', 'dkg'): 0.1,
            ('dkg', 'g'): 10,
            ('dkg', 'kg'): 0.01,
            ('kg', 'g'): 1000,
            ('kg', 'dkg'): 100,
            ('ml', 'l'): 0.001,
            ('ml', 'dl'): 0.1,
            ('dl', 'ml'): 10,
            ('dl', 'l'): 0.1,
            ('l', 'dl'): 10,
            ('l', 'ml'): 1000,
            ('db', 'db'): 1,
            ('fej', 'fej'): 1,
            ('szem', 'szem'): 1,
            ('gerezd', 'gerezd'): 1,
            ('ízlés szerint', 'ízlés szerint'): 1,
            ('tk', 'ml'): 5,
            ('ek', 'ml'): 15,
            ('cup', 'ml'): 240,
            ('ml', 'tk'): 0.2,
            ('ml', 'ek'): 1/15,
            ('ml', 'cup'): 1/240,
            ('l', 'cup'): 4.167,
            ('cup', 'l'): 0.24,
        }
        key = (item.unit, new_unit)
        if key in conversions:
            return item.quantity * conversions[key]
        else:
            raise ValueError(f"Átváltás {item.unit}-ból/ből {new_unit}-ba/be nem támogatott.")
        
def modify_body(headerfunc, s, value, setter, menufunc, *args):
    headerfunc(s, value)
    new_value = input(f"Új {s.lower()}: ")
    if new_value:
        setter(int(new_value) if s == "Adag" else new_value)
        print("Sikeres módosítás.")
        back_to_menu(menufunc, *args)
    else:
        menufunc()

def modify_header(name, value):
    print(f"{name} módosítása")
    print(f"Jelenlegi {name}:", value)
    print("0. Mégse")