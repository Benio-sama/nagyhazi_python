from functions import back_to_menu, clear_console, exit_if_0,  modify_header, modify_body
from pantry import Pantry

def pantry_menu(recipes, menus, pantry):
    from console import main_menu
    print("Kamra kezelése")
    print("1. Hozzávaló hozzáadása")
    print("2. Hozzávaló módosítása")
    print("3. Hozzávaló törlése")
    print("4. Kamra tartalmának listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu(recipes, menus, pantry)
    elif choice == '1':
        clear_console()
        pantry = add_new_ingredient(recipes, menus, pantry)
        back_to_menu(pantry_menu, recipes, menus, pantry)
    elif choice == '2':
        clear_console()
        modify_ingredient(recipes, menus, pantry)
    elif choice == '3':
        pantry = delete_ingredient(recipes, menus, pantry)
        back_to_menu(pantry_menu, recipes, menus, pantry)
    elif choice == '4':
        clear_console()
        list_pantry(pantry)

def add_new_ingredient(recipes, menus, pantry):
    print("Hozzávaló hozzáadása")
    print("0. Mégse")
    name = input("Add meg a hozzávaló nevét: ")
    exit_if_0(name, pantry_menu, recipes, menus, pantry)
    quantity = float(input("Add meg a mennyiséget: "))
    exit_if_0(quantity, pantry_menu, recipes, menus, pantry)
    unit = input("Add meg a mértékegységet: ")
    exit_if_0(unit, pantry_menu, recipes, menus, pantry)
    pantry.append(Pantry(len(pantry), name, quantity, unit))
    print("Hozzávaló hozzáadva.")
    return pantry

def modify_ingredient(recipes, menus, pantry):
    print("Hozzávaló módosítása")
    print("0. Mégse")
    for i in pantry:
        print(i.id+1, f"{i.name} : {i.quantity} {i.unit}")
    ing_id = int(input("Add meg a módosítandó hozzávaló számát: "))
    exit_if_0(ing_id, pantry_menu, recipes, menus, pantry)
    for i in pantry:
        if i.id == ing_id-1:
            print("1. Név módosítása")
            print("2. Mennyiség módosítása")
            print("3. Mértékegység módosítása")
            choice = input("Mit szeretnél módosítani? ")
            if choice == '1':
                modify_body(modify_header, "Név", i.name, i._setname, pantry_menu, recipes, menus, pantry)
            elif choice == '2':
                modify_body(modify_header, "Mennyiség", i.quantity, i._setquantity, pantry_menu, recipes, menus, pantry)
            elif choice == '3':
                modify_body(modify_header, "Mértékegység", i.unit, i._setunit, pantry_menu, recipes, menus, pantry)
    print("Hozzávaló nem található.")

def delete_ingredient(pantry):
    print("Hozzávaló törlése")
    for i in pantry:
        print(i.id+1, i.name)
    ing_id = int(input("Add meg a törlendő hozzávaló számát: "))-1
    for i in pantry:
        if i.id == ing_id:
            confirm = input(f"Biztosan törölni szeretnéd a(z) {pantry[ing_id].name} hozzávalót? (i/n): ")
            if confirm.lower() == 'i':
                pantry.remove(i)
                print("Hozzávaló törölve.")
                return pantry
            else:
                print("Törlés megszakítva.")
                return pantry
        else:
            print("Hozzávaló nem található.")
            return pantry
    

def list_pantry(pantry):
    print("Kamra tartalmának listázása")
    print(len(pantry))
    for item in pantry:
        print(item)

def pantry_main_menu(recipes, menus, pantry):
    clear_console()
    pantry_menu(recipes, menus, pantry)