import datetime
from functions import clear_console, exit_if_0, back_to_menu, save_to_json

def menu_menu(recipes, menus, pantry, shopping_list):
    from console import main_menu
    
    save_to_json(menus, 'menu.json')
    print("Menü kezelése")
    print("1. Napi menü hozzáadása")
    print("2. Napi menü törlése")
    print("3. Heti menü törlése")
    print("4. Menü listázása")
    print("5. A mai menü listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu(recipes, menus, pantry, shopping_list)
    elif choice == '1':
        clear_console()
        menus = add_menu(recipes, menus, pantry, shopping_list)
        back_to_menu(menu_menu, recipes, menus, pantry, shopping_list)
    elif choice == '2':
        clear_console()
        menus = remove_recipe_from_day(recipes, menus, pantry, shopping_list)
    elif choice == '3':
        clear_console()
        delete_weekly_menu(recipes, menus, pantry, shopping_list)
    elif choice == '4':
        clear_console()
        list_menus(menus)
        menu_menu(recipes, menus, pantry, shopping_list)
    elif choice == '5':
        clear_console()
        list_todays_menu(menus)
        menu_menu(recipes, menus, pantry, shopping_list)
    else:
        clear_console()
        menu_menu(recipes, menus, pantry, shopping_list)

def add_menu(recipes, menus, pantry, shopping_list):
    print("Napi menü hozzáadása")
    print("0. Mégse")
    for d in menus:
        print(d.id+1, d.day)
    nap = int(input("Add meg a nap számát: "))
    exit_if_0(nap, menu_menu, recipes, menus, pantry, shopping_list)
    if len(recipes) == 0:
        print("Nincs elérhető recept a menühöz.")
        return menus
    if len(menus[nap-1].recipes) > 0:
        print("Már hozzáadott recept(ek): ")
        for i in menus[nap-1].recipes:
            print(f"\t- {i.name}")
    print("Elérhető receptek:")
    for r in recipes:
        print(r.id+1, r.name)
    selected_recipes = []
    recepe_ids = input("Add meg a receptek számait szóközzel elválasztva: ").split(" ")
    exit_if_0(recepe_ids, menu_menu, recipes, menus, pantry, shopping_list)
    for rid in recepe_ids:
        if rid.isdigit():
            rid_int = int(rid)-1
            if 0 <= rid_int < len(recipes):
                selected_recipes.append(recipes[rid_int])
            else:
                print(f"A {rid} számú recept nem létezik. Figyelmen kívül hagyva.")
    for i in menus:
        if i.id == nap-1:
            for sr in selected_recipes:
                i.add_meal(sr)
            print("Sikeres hozzáadás.")
    save_to_json(menus, 'menu.json')
    return menus

def remove_recipe_from_day(recipes, menus, pantry, shopping_list):
    print("Napi menü törlése")
    print("0. Mégse")
    for d in menus:
        print(d.id+1, d.day)
    nap = int(input("Add meg a nap számát: "))
    exit_if_0(nap, menu_menu, recipes, menus, pantry, shopping_list)
    for i in menus:
        if i.id == nap-1:
            if len(i.recipes) == 0:
                print("Nincs recept a kiválasztott napon.")
                back_to_menu(remove_recipe_from_day, recipes, menus, pantry, shopping_list)
            else:
                for r in i.recipes:
                    print(r.id+1, r.name)
                r_ids = input("Add meg a törlendő recept számát (ha többet törölnél, szóközzel elválasztva): ").split(" ")
                exit_if_0(r_ids, menu_menu, recipes, menus, pantry, shopping_list)
                delete = []
                for rid in r_ids:
                    if rid.isdigit():
                        rid_int = int(rid)-1
                        if 0 <= rid_int < len(recipes):
                            delete.append(recipes[rid_int])
                        else:
                            print(f"A {rid} számú recept nem létezik. Figyelmen kívül hagyva.")
                confirm = input(f"Biztosan törlöd a " + ", ".join([r.name for r in delete]) + " receptet? (i/n): ")
                if confirm.lower() == 'i':
                    for r in delete:
                        i.remove_meal(r)
                    print("Sikeres törlés.")
                    back_to_menu(menu_menu, recipes, menus, pantry, shopping_list)
                else:
                    print("Törlés megszakítva.")
                    back_to_menu(menu_menu, recipes, menus, pantry, shopping_list)
    save_to_json(menus, 'menu.json')

def delete_weekly_menu(recipes, menus, pantry, shopping_list):
    print("Heti menü törlése")
    confirm = input("Biztosan törlöd az egész heti menüt? (i/n): ")
    if confirm.lower() == 'i':
        for m in menus:
            m.recipes.clear()
        print("Heti menü törölve.")
    else:
        print("Törlés megszakítva.")
    save_to_json(menus, 'menu.json')
    back_to_menu(menu_menu, recipes, menus, pantry, shopping_list)

def list_menus(menus):
    print("Napi menük listázása")
    for m in menus:
        print(f"{m.day}:")
        for meal in m.recipes:
            print(f"\t- {meal.name}")

def list_todays_menu(menus):
    print("A mai menü:")
    today_index = datetime.datetime.today().weekday()
    for m in menus:
        if m.id == today_index:
            print(f"{m.day}:")
            if len(m.recipes) == 0:
                print("Nincs hozzárendelt recept.")
            else:
                for meal in m.recipes:
                    print(f"\t- {meal.name}")

def menu_main(recipes, menus, pantry, shopping_list):
    clear_console()
    menu_menu(recipes, menus, pantry, shopping_list)
