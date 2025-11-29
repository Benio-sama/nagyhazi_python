from export_console import export_main
from functions import clear_console

def main_menu(recipes, menus, pantry, shopping_list):
    from recipe_console import recipe_main_menu
    from menu_console import menu_main
    from pantry_console import pantry_main_menu
    from shopping_list_console import shopping_list_main

    clear_console()
    print("Főmenü")
    print("1. Receptek kezelése")
    print("2. Kamra kezelése")
    print("3. Menü kezelése")
    print("4. Bevásárlólista kezelése")
    print("5. Adatok exportálása")
    print("0. Kilépés")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        exit()
    elif choice == '1':
        clear_console()
        recipe_main_menu(recipes, menus, pantry, shopping_list)
    elif choice == '2':
        clear_console()
        pantry_main_menu(recipes, menus, pantry, shopping_list)
    elif choice == '3':
        clear_console()
        menu_main(recipes, menus, pantry, shopping_list)
    elif choice == '4':
        shopping_list_main(recipes, menus, pantry, shopping_list)
    elif choice == '5':
        export_main(recipes, menus, pantry, shopping_list)
    else:
        main_menu(recipes, menus, pantry, shopping_list)

def console_main(recipes, menus, pantry, shopping_list):
    clear_console()
    main_menu(recipes, menus, pantry, shopping_list)
