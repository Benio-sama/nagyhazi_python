from recipes import read_recipe_from_file
from menu import read_menu_from_file
from functions import clear_console, exit_if_0

def menu_menu(recipes, menus):
    from console import main_menu
    print("Menü kezelése")
    print("1. Napi menü hozzáadása")
    print("2. Napi menü módosítása")
    print("3. Napi menü törlése")
    print("4. Napi menük listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu()
    elif choice == '1':
        print("Napi menü hozzáadása")
    elif choice == '2':
        print("Napi menü módosítása")
    elif choice == '3':
        print("Napi menü törlése")
    elif choice == '4':
        print("Napi menük listázása")

def add_menu(recipes, menus):
    print("Napi menü hozzáadása")
    print("0. Mégse")
    for d in menus:
        print(d.id+1, d.day)
    nap = int(input("Add meg a nap számát: "))-1
    exit_if_0(nap, menu_menu, (recipes, menus))
    print("Elérhető receptek:")
    for r in recipes:
        print(r.id+1, r.name)
    selected_recipes = []
    recepe_ids = input("Add meg a receptek számait szóközzel elválasztva: ").split(" ")
    exit_if_0(recepe_ids, menu_menu, (recipes, menus))
    for rid in recepe_ids:
        if rid.isdigit():
            rid_int = int(rid)-1
            if 0 <= rid_int < len(recipes):
                selected_recipes.append(recipes[rid_int])
    for i in menus:
        if i.id == nap:
            for sr in selected_recipes:
                i.add_meal(sr)


def menu_main():
    recipes = read_recipe_from_file('jsons/recipes.json')
    menus = read_menu_from_file('jsons/menu.json')
    menu_menu(recipes, menus)