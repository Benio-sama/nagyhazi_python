from functions import clear_console,  modify_header, modify_quantity, save_to_json
from pantry import Pantry
import time

def pantry_menu(p_choice, pantry):
    save_to_json(pantry, 'pantry.json')

    if p_choice == '1':
        clear_console()
        pantry = add_new_ingredient(pantry)
    elif p_choice == '2':
        clear_console()
        pantry = modify_ingredient(pantry)
    elif p_choice == '3':
        clear_console()
        pantry = delete_ingredient(pantry)
    elif p_choice == '4':
        clear_console()
        list_pantry(pantry)

def add_new_ingredient(pantry):
    print("Hozzávaló hozzáadása")
    print("0. Mégse")
    name = input("Add meg a hozzávaló nevét: ")
    if name == '0':
        clear_console()
        return pantry
    quantity_input = input("Add meg a mennyiséget: ")
    while not quantity_input.isdigit():
        print("Kérlek számot adj meg!")
        quantity_input = input("Add meg a mennyiséget: ")
    quantity = float(quantity_input)
    if quantity == 0:
        clear_console()
        return pantry
    unit = input("Add meg a mértékegységet: ")
    if unit == '0':
        clear_console()
        return pantry
    pantry.append(Pantry(len(pantry), name, quantity, unit))
    print("Hozzávaló hozzáadva.")
    save_to_json(pantry, 'pantry.json')
    time.sleep(1)
    clear_console()
    return pantry

def modify_ingredient(pantry):
    save_to_json(pantry, 'pantry.json')
    print("Hozzávaló módosítása")
    print("0. Mégse")
    for i in pantry:
        print(f"{i.id+1}. {i.name} : {i.quantity} {i.unit}")
    ing_id = input("Add meg a módosítandó hozzávaló számát: ")
    while ing_id not in [str(i.id+1) for i in pantry] and ing_id != '0':
        ing_id = input("Érvénytelen választás. Kérlek, válassz újra: ")
    if ing_id == '0':
        clear_console()
        return pantry
    print("1. Hozzávaló adatainak módosítása")
    print("2. Mennyiség növelése")
    print("3. Mennyiség csökkentése")
    print("0. Mégse")
    choice = input("Válassz egy opciót: ")
    while choice not in ['0', '1', '2', '3']:
        choice = input("Érvénytelen választás. Kérlek, válassz újra: ")
    match choice:
        case '0':
            clear_console()
            return pantry
        case '1':
            for i in pantry:
                if i.id == int(ing_id)-1:
                    print("1. Név módosítása")
                    print("2. Mennyiség módosítása")
                    print("3. Mértékegység módosítása")
                    print("0. Mégse")
                    mod_choice = input("Válassz egy opciót: ")
                    match mod_choice:
                        case '0':
                            return pantry
                        case '1':
                            clear_console()
                            modify_header("Név", i.name)
                            new_name = input("Új név: ")
                            if new_name == '0':
                                clear_console()
                                return pantry
                            if new_name:
                                i._setname(new_name)
                                print("Név módosítva.")
                                time.sleep(1)
                                clear_console()
                                save_to_json(pantry, 'pantry.json')
                                return pantry
                            return pantry
                        case '2':
                            clear_console()
                            modify_header("Mennyiség", i.quantity)
                            new_quantity = input("Új mennyiség: ")
                            if new_quantity == '0':
                                clear_console()
                                return pantry
                            if new_quantity:
                                while not new_quantity.isdigit():
                                    print("Kérlek számot adj meg!")
                                    new_quantity = input("Új mennyiség: ")
                                i._setquantity(float(new_quantity))
                                print("Mennyiség módosítva.")
                                time.sleep(1)
                                clear_console()
                                save_to_json(pantry, 'pantry.json')
                                return pantry
                            return pantry
                        case '3':
                            print("Módosítod a mértékegységet, vagy konvertálni szeretnéd a mértékegységet?")
                            print("1. Módosítás")
                            print("2. Átváltás")
                            print("0. Mégse")
                            unit_choice = input("Válassz egy opciót: ")
                            while unit_choice not in ['0', '1', '2']:
                                unit_choice = input("Érvénytelen választás. Kérlek, válassz újra: ")
                            match unit_choice:
                                case '0':
                                    clear_console()
                                    return pantry
                                case '1':
                                    clear_console()
                                    modify_header("Mértékegység", i.unit)
                                    new_unit = input("Új mértékegység: ")
                                    if new_unit == '0':
                                        clear_console()
                                        return pantry
                                    if new_unit:
                                        i._setunit(new_unit)
                                        print("Mértékegység módosítva.")
                                        time.sleep(1)
                                        clear_console()
                                        save_to_json(pantry, 'pantry.json')
                                        return pantry
                                    return pantry
                                case '2':
                                    modify_quantity(i)
                                    time.sleep(1)
                                    save_to_json(pantry, 'pantry.json')
                                    clear_console()
                                    return pantry
            print("Hozzávaló nem található.")
            time.sleep(1)
            clear_console()
            return pantry
        case '2':
            for i in pantry:
                if i.id == ing_id-1:
                    a_quantity = input(f"Add meg a növelendő mennyiséget (jelenleg: {i.quantity}): ")
                    if a_quantity == '0':
                        clear_console()
                        return pantry
                    while not a_quantity.isdigit():
                        print("Kérlek számot adj meg!")
                        a_quantity = input(f"Add meg a növelendő mennyiséget (jelenleg: {i.quantity}): ")
                    i.add_quantity(float(a_quantity))
                    print("Mennyiség növelve.")
                    time.sleep(1)
                    save_to_json(pantry, 'pantry.json')
                    clear_console()
                    return pantry
            print("Hozzávaló nem található.")
            time.sleep(1)
            clear_console()
            return pantry
        case '3':
            for i in pantry:
                if i.id == ing_id-1:
                    r_quantity = input(f"Add meg a csökkentendő mennyiséget (jelenleg: {i.quantity}): ")
                    if r_quantity == '0':
                        clear_console()
                        return pantry
                    while not r_quantity.isdigit():
                        print("Kérlek számot adj meg!")
                        r_quantity = input(f"Add meg a csökkentendő mennyiséget (jelenleg: {i.quantity}): ")
                    i.remove_quantity(float(r_quantity))
                    print("Mennyiség csökkentve.")
                    time.sleep(1)
                    save_to_json(pantry, 'pantry.json')
                    clear_console()
                    return pantry
            print("Hozzávaló nem található.")
            time.sleep(1)
            clear_console()
            return pantry
    

def delete_ingredient(pantry):
    print("Hozzávaló törlése")
    print("0. Mégse")
    if len(pantry) == 0:
        print("Nincs elérhető hozzávaló a kamrában.")
        return pantry
    for i in pantry:
        print(f"{i.id+1}. {i.name}")
    ing_id = input("Add meg a törlendő hozzávaló számát: ")
    while ing_id not in [str(i.id+1) for i in pantry] and ing_id != '0':
        ing_id = input("Érvénytelen választás. Kérlek, válassz újra: ")
    if ing_id == '0':
        clear_console()
        return pantry
    for i in pantry:
        if i.id == int(ing_id)-1:
            confirm = input(f"Biztosan törölni szeretnéd a(z) {i.name} hozzávalót? (i/n): ")
            if confirm.lower() == 'i':
                pantry.remove(i)
                print("Hozzávaló törölve.")
                save_to_json(pantry, 'pantry.json')
                return pantry
            else:
                print("Törlés megszakítva.")
                return pantry
    print("Hozzávaló nem található.")
    return pantry
    

def list_pantry(pantry):
    print("Kamra tartalmának listázása")
    if len(pantry) == 0:
        print("A kamra üres.")
        return
    for item in pantry:
        print(item)

def pantry_main_menu(recipes, menus, pantry, shopping_list):
    from console import console_main

    clear_console()
    is_not_in_choices = False
    while True:
        if not is_not_in_choices:
            print("Kamra kezelése")
            print("1. Hozzávaló hozzáadása")
            print("2. Hozzávaló módosítása")
            print("3. Hozzávaló törlése")
            print("4. Kamra tartalmának listázása")
            print("0. Vissza a főmenübe")   
        p_choice = input("Válassz egy opciót: " if not is_not_in_choices else "Érvénytelen választás. Kérlek, válassz újra: ")
        if p_choice == '0':
            console_main(recipes, menus, pantry, shopping_list)
            break
        elif p_choice not in ['1', '2', '3', '4']:
            is_not_in_choices = True
            continue
        pantry_menu(p_choice, pantry)