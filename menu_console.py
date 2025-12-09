import time
import datetime
from functions import clear_console, save_to_json

def menu_menu(m_choice, recipes, menus):
    if m_choice == '1':
        clear_console()
        menus = add_menu(recipes, menus)
    elif m_choice == '2':
        clear_console()
        menus = remove_recipe_from_day(recipes, menus)
    elif m_choice == '3':
        clear_console()
        menus = delete_weekly_menu(menus)
    elif m_choice == '4':
        clear_console()
        list_menus(menus)
    elif m_choice == '5':
        clear_console()
        list_todays_menu(menus)    

def add_menu(recipes, menus):
    print("Napi menü hozzáadása")
    print("0. Mégse")
    for d in menus:
        print(f"{d.id+1}. {d.day}")
    nap = input("Add meg a nap számát: ")
    while nap not in [str(d.id+1) for d in menus] and nap != '0':
        nap = input("Érvénytelen választás. Kérlek, válassz újra: ")
    if nap == '0':
        clear_console()
        return menus
    if len(recipes) == 0:
        print("Nincs elérhető recept a menühöz.")
        time.sleep(1)
        clear_console()
        return menus
    if len(menus[int(nap)-1].recipes) > 0:
        print("Már hozzáadott recept(ek): ")
        for i in menus[int(nap)-1].recipes:
            print(f"\t- {i.name}")
    print("Elérhető receptek:")
    for r in recipes:
        print(f"{r.id+1}. {r.name}")
    selected_recipes = []
    while True:
        recipe_ids = input("Add meg a receptek számait szóközzel elválasztva (0 = kilép): ").split()
        if "0" in recipe_ids:
            clear_console()
            return menus
        if all(rid.isdigit() and 1 <= int(rid) <= len(recipes) for rid in recipe_ids):
            break
    for rid in recipe_ids:
        if rid.isdigit():
            rid_int = int(rid)-1
            if 0 <= rid_int < len(recipes):
                selected_recipes.append(recipes[rid_int])
            else:
                print(f"A {rid} számú recept nem létezik. Figyelmen kívül hagyva.")
    for i in menus:
        if i.id == int(nap)-1:
            for sr in selected_recipes:
                i.add_meal(sr)
            print("Sikeres hozzáadás.")
            time.sleep(1)
    save_to_json(menus, 'menu.json')
    clear_console()
    return menus

def remove_recipe_from_day(recipes, menus):
    print("Napi menü törlése")
    print("0. Mégse")
    for d in menus:
        print(d.id+1, d.day)
    nap = input("Add meg a nap számát: ")
    while nap not in [str(d.id+1) for d in menus] and nap != '0':
        nap = input("Érvénytelen választás. Kérlek, válassz újra: ")
    if nap == '0':
        clear_console()
        return menus
    for i in menus:
        if i.id == int(nap)-1:
            if len(i.recipes) == 0:
                print("Nincs recept a kiválasztott napon.")
                time.sleep(1)
                clear_console()
                return menus
            else:
                for r in i.recipes:
                    print(f"{r.id+1}. {r.name}")
                while True:
                    r_ids = input("Add meg a törlendő recept számát (ha többet törölnél, szóközzel elválasztva) (0 = kilép): ").split()
                    if "0" in r_ids:
                        clear_console()
                        return menus
                    if all(rid.isdigit() and 1 <= int(rid) <= len(recipes) for rid in r_ids):
                        break
                delete = []
                for rid in r_ids:
                    if rid.isdigit():
                        rid_int = int(rid)-1
                        if 0 <= rid_int < len(recipes):
                            delete.append(recipes[rid_int])
                        else:
                            print(f"A {rid} számú recept nem létezik. Figyelmen kívül hagyva.")
                if len(delete) == 0:
                    print("Nincs törlendő recept kiválasztva.")
                    time.sleep(1)
                    clear_console()
                    return menus
                confirm = input(f"Biztosan törlöd a " + ", ".join([r.name for r in delete]) + (" recepteket? (i/n): " if len(delete) > 1 else " receptet? (i/n): "))
                if confirm.lower() == 'i':
                    for r in delete:
                        i.remove_meal(r)
                    print("Sikeres törlés.")
                    save_to_json(menus, 'menu.json')
                    return menus
                else:
                    print("Törlés megszakítva.")
                    time.sleep(1)
                    clear_console()
                    return menus

def delete_weekly_menu(menus):
    print("Heti menü törlése")
    confirm = input("Biztosan törlöd az egész heti menüt? (i/n): ")
    if confirm.lower() == 'i':
        for m in menus:
            m.recipes.clear()
        print("Heti menü törölve.")
    else:
        print("Törlés megszakítva.")
    time.sleep(1)
    clear_console()
    save_to_json(menus, 'menu.json')
    return menus

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

def menu_main(recipes, menus):
    clear_console()
    is_not_in_choices = False
    while True:
        if not is_not_in_choices:
            print("Menü kezelése")
            print("1. Napi menü hozzáadása")
            print("2. Napi menü törlése")
            print("3. Heti menü törlése")
            print("4. Menü listázása")
            print("5. A mai menü listázása")
            print("0. Vissza a főmenübe")
        m_choice = input("Válassz egy opciót: " if not is_not_in_choices else "Érvénytelen választás. Kérlek, válassz újra: ")
        if m_choice == '0':
            return menus
        elif m_choice not in ['1', '2', '3', '4', '5']:
            is_not_in_choices = True
            continue
        menu_menu(m_choice, recipes, menus)