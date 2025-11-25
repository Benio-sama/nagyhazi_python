import datetime
from functions import clear_console, exit_if_0, back_to_menu

def menu_menu(recipes, menus, pantry):
    from console import main_menu
    print("Menü kezelése")
    print("1. Napi menü hozzáadása")
    print("2. Napi menü törlése")
    print("3. Heti menü törlése")
    print("4. Menü listázása")
    print("5. Napi menü listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu(recipes, menus, pantry)
    elif choice == '1':
        clear_console()
        menus = add_menu(recipes, menus, pantry)
        menu_menu(recipes, menus, pantry)
    elif choice == '2':
        clear_console()
        menus = remove_recipe_from_day(recipes, menus, pantry)
    elif choice == '3':
        clear_console()
        delete_weekly_menu(recipes, menus)
    elif choice == '4':
        clear_console()
        list_menus(menus)
        menu_menu(recipes, menus)
    elif choice == '5':
        clear_console()
        list_todays_menu(menus)
        menu_menu(recipes, menus)

def add_menu(recipes, menus, pantry):
    print("Napi menü hozzáadása")
    print("0. Mégse")
    for d in menus:
        print(d.id+1, d.day)
    nap = int(input("Add meg a nap számát: "))-1
    exit_if_0(nap, menu_menu, recipes, menus, pantry)
    print("Elérhető receptek:")
    for r in recipes:
        print(r.id+1, r.name)
    selected_recipes = []
    recepe_ids = input("Add meg a receptek számait szóközzel elválasztva: ").split(" ")
    exit_if_0(recepe_ids, menu_menu, recipes, menus, pantry)
    for rid in recepe_ids:
        if rid.isdigit():
            rid_int = int(rid)-1
            if 0 <= rid_int < len(recipes):
                selected_recipes.append(recipes[rid_int])
    for i in menus:
        if i.id == nap:
            for sr in selected_recipes:
                i.add_meal(sr)
    return menus

def remove_recipe_from_day(recipes, menus, pantry):
    print("Napi menü törlése")
    for d in menus:
        print(d.id+1, d.day)
    nap = int(input("Add meg a nap számát: "))-1
    for i in menus:
        if i.id == nap:
            for r in i.recipes:
                print(r.id+1, r.name)
            r_id = int(input("Add meg a törlendő recept számát: ")) -1
            confirm = input(f"Biztosan törlöd a {r_id}. receptet? (i/n): ")
            if confirm.lower() == 'i':
                i.remove_meal(recipes[r_id])
                print("Sikeres törlés.")
                back_to_menu(menu_menu, recipes, menus, pantry)
            else:
                print("Törlés megszakítva.")
                back_to_menu(menu_menu, recipes, menus, pantry)

def delete_weekly_menu(recipes, menus, pantry):
    print("Heti menü törlése")
    confirm = input("Biztosan törlöd az egész heti menüt? (i/n): ")
    if confirm.lower() == 'i':
        for m in menus:
            m.recipes.clear()
        print("Heti menü törölve.")
    else:
        print("Törlés megszakítva.")
    back_to_menu(menu_menu, recipes, menus, pantry)

def list_menus(menus):
    print("Napi menük listázása")
    for m in menus:
        print(f"{m.day}:")
        for meal in m.recipes:
            print(f" - {meal.name}")

def list_todays_menu(menus):
    print("A mai menü:")
    today_index = datetime.datetime.today().weekday()
    for m in menus:
        if m.id == today_index:
            print(f"{m.day}:")
            for meal in m.recipes:
                print(f" - {meal.name}")

def menu_main(recipes, menus, pantry):
    clear_console()
    menu_menu(recipes, menus, pantry)
