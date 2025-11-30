from functions import back_to_menu, clear_console, exit_if_0,  modify_header, modify_body, modify_quantity, save_to_json
from pantry import Pantry

def pantry_menu(recipes, menus, pantry, shopping_list):
    from console import main_menu

    save_to_json(pantry, 'pantry.json')
    print("Kamra kezelése")
    print("1. Hozzávaló hozzáadása")
    print("2. Hozzávaló módosítása")
    print("3. Hozzávaló törlése")
    print("4. Kamra tartalmának listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu(recipes, menus, pantry, shopping_list)
    elif choice == '1':
        clear_console()
        pantry = add_new_ingredient(recipes, menus, pantry, shopping_list)
        back_to_menu(pantry_menu, recipes, menus, pantry, shopping_list)
    elif choice == '2':
        clear_console()
        modify_ingredient(recipes, menus, pantry, shopping_list)
    elif choice == '3':
        clear_console()
        pantry = delete_ingredient(recipes, menus, pantry, shopping_list)
        back_to_menu(pantry_menu, recipes, menus, pantry, shopping_list)
    elif choice == '4':
        clear_console()
        list_pantry(pantry)
        pantry_menu(recipes, menus, pantry, shopping_list)
    else:
        clear_console()
        pantry_menu(recipes, menus, pantry, shopping_list)

def add_new_ingredient(recipes, menus, pantry, shopping_list):
    print("Hozzávaló hozzáadása")
    print("0. Mégse")
    name = input("Add meg a hozzávaló nevét: ")
    exit_if_0(name, pantry_menu, recipes, menus, pantry, shopping_list)
    quantity = float(input("Add meg a mennyiséget: "))
    exit_if_0(quantity, pantry_menu, recipes, menus, pantry, shopping_list)
    unit = input("Add meg a mértékegységet: ")
    exit_if_0(unit, pantry_menu, recipes, menus, pantry, shopping_list)
    pantry.append(Pantry(len(pantry), name, quantity, unit))
    print("Hozzávaló hozzáadva.")
    save_to_json(pantry, 'pantry.json')
    return pantry

def modify_ingredient(recipes, menus, pantry, shopping_list):
    save_to_json(pantry, 'pantry.json')
    print("Hozzávaló módosítása")
    print("0. Mégse")
    for i in pantry:
        print(f"{i.id+1}. {i.name} : {i.quantity} {i.unit}")
    ing_id = int(input("Add meg a módosítandó hozzávaló számát: "))
    exit_if_0(ing_id, pantry_menu, recipes, menus, pantry, shopping_list)
    print("1. Hozzávaló adatainak módosítása")
    print("2. Mennyiség növelése")
    print("3. Mennyiség csökkentése")
    print("0. Mégse")
    choice = input("Válassz egy opciót: ")
    match choice:
        case '0':
            clear_console()
            modify_ingredient(recipes, menus, pantry, shopping_list)
        case '1':
            for i in pantry:
                if i.id == ing_id-1:
                    print("1. Név módosítása")
                    print("2. Mennyiség módosítása")
                    print("3. Mértékegység módosítása")
                    print("0. Mégse")
                    mod_choice = input("Válassz egy opciót: ")
                    match mod_choice:
                        case '0':
                            modify_ingredient(recipes, menus, pantry, shopping_list)
                        case '1':
                            modify_body(modify_header, "Név", i.name, i._setname, modify_ingredient, recipes, menus, pantry, shopping_list)
                        case '2':
                            modify_body(modify_header, "Mennyiség", i.quantity, i._setquantity, modify_ingredient, recipes, menus, pantry, shopping_list)
                        case '3':
                            print("Módosítod a mértékegységet, vagy konvertálni szeretnéd a mértékegységet?")
                            print("1. Módosítás")
                            print("2. Konvertálás")
                            print("0. Mégse")
                            unit_choice = input("Válassz egy opciót: ")
                            match unit_choice:
                                case '0':
                                    modify_ingredient(recipes, menus, pantry, shopping_list)
                                case '1':
                                    modify_body(modify_header, "Mértékegység", i.unit, i._setunit, modify_ingredient, recipes, menus, pantry, shopping_list)
                                case '2':
                                    modify_quantity(i)
                                    back_to_menu(pantry_menu, recipes, menus, pantry, shopping_list)
            print("Hozzávaló nem található.")
            back_to_menu(modify_ingredient, recipes, menus, pantry, shopping_list)
        case '2':
            for i in pantry:
                if i.id == ing_id-1:
                    i.add_quantity(float(input(f"Add meg a növelendő mennyiséget (jelenleg: {i.quantity}): ")))
                    print("Mennyiség növelve.")
                    back_to_menu(modify_ingredient, recipes, menus, pantry, shopping_list)
            print("Hozzávaló nem található.")
            back_to_menu(modify_ingredient, recipes, menus, pantry, shopping_list)
        case '3':
            for i in pantry:
                if i.id == ing_id-1:
                    i.remove_quantity(float(input(f"Add meg a csökkentendő mennyiséget (jelenleg: {i.quantity}): ")))
                    print("Mennyiség csökkentve.")
                    back_to_menu(modify_ingredient, recipes, menus, pantry, shopping_list)
            print("Hozzávaló nem található.")
            back_to_menu(modify_ingredient, recipes, menus, pantry, shopping_list)
    

def delete_ingredient(recipes, menus, pantry, shopping_list):
    print("Hozzávaló törlése")
    print("0. Mégse")
    for i in pantry:
        print(f"{i.id+1}. {i.name}")
    ing_id = int(input("Add meg a törlendő hozzávaló számát: "))
    exit_if_0(ing_id, pantry_menu, recipes, menus, pantry, shopping_list)
    for i in pantry:
        if i.id == ing_id-1:
            confirm = input(f"Biztosan törölni szeretnéd a(z) {i.name} hozzávalót? (i/n): ")
            if confirm.lower() == 'i':
                pantry.remove(i)
                print("Hozzávaló törölve.")
                return pantry
            else:
                print("Törlés megszakítva.")
                return pantry
    print("Hozzávaló nem található.")
    save_to_json(pantry, 'pantry.json')
    return pantry
    

def list_pantry(pantry):
    print("Kamra tartalmának listázása")
    for item in pantry:
        print(item)
    print()

def pantry_main_menu(recipes, menus, pantry, shopping_list):
    pantry_menu(recipes, menus, pantry, shopping_list)