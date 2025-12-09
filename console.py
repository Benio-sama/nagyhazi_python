from export_console import export_main
from functions import clear_console
from recipe_console import recipe_main_menu
from menu_console import menu_main
from pantry_console import pantry_main_menu
from shopping_list_console import shopping_list_main

def main_menu(c_choice, recipes, menus, pantry, shopping_list):
    if c_choice == '1':
        clear_console()
        recipes = recipe_main_menu(recipes)
    elif c_choice == '2':
        clear_console()
        pantry = pantry_main_menu(pantry)
    elif c_choice == '3':
        clear_console()
        menus = menu_main(recipes, menus)
    elif c_choice == '4':
        clear_console()
        pantry, shopping_list = shopping_list_main(menus, pantry, shopping_list)
    elif c_choice == '5':
        export_main(recipes, menus, pantry, shopping_list)

def console_main(recipes, menus, pantry, shopping_list):
    clear_console()
    is_not_in_choices = False
    while True:
        if not is_not_in_choices:
            clear_console()
            print("Főmenü")
            print("1. Receptek kezelése")
            print("2. Kamra kezelése")
            print("3. Menü kezelése")
            print("4. Bevásárlólista kezelése")
            print("5. Adatok exportálása")
            print("0. Kilépés")
        c_choice = input("Válassz egy opciót: " if not is_not_in_choices else "Érvénytelen választás. Kérlek, válassz újra: ")
        if c_choice == '0':
            break
        elif c_choice not in ['1', '2', '3', '4', '5']:
            is_not_in_choices = True
            continue
        main_menu(c_choice, recipes, menus, pantry, shopping_list)