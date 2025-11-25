from functions import clear_console

def main_menu(recipes, menus, pantry):
    from recipe_console import recipe_main_menu
    from menu_console import menu_main
    from pantry_console import pantry_main_menu

    clear_console()
    print("Főmenü")
    print("1. Receptek kezelése")
    print("2. Kamra kezelése")
    print("3. Menü kezelése")
    print("4. Bevásárlólista kezelése")
    print("5. Adatok mentése / betöltése")
    print("6. Adatok exportálása")
    print("0. Kilépés")

    choice = input("Válassz egy opciót: ")
    while choice != '0':
        if choice == '1':
            recipe_main_menu(recipes, menus, pantry)
        elif choice == '2':
            pantry_main_menu(recipes, menus, pantry)
        elif choice == '3':
            clear_console()
            menu_main(recipes, menus, pantry)
        elif choice == '4':
            shopping_list_menu()
        elif choice == '5':
            print("Adatok mentése / betöltése")
        elif choice == '6':
            print("Adatok exportálása")
        else:
            main_menu(recipes, menus, pantry)
            choice = input("Válassz egy opciót: ")
    exit()


def shopping_list_menu():
    print("Bevásárlólista kezelése")
    print("1. Bevásárlólista generálása")
    print("2. Bevásárlólista megtekintése")
    print("3. Bevásárlólista optimalizálása")
    print("4. Bevásárlólista törlése")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    # if choice == '0':
    #     # main_menu()
    # elif choice == '1':
    #     print("Bevásárlólista generálása")
    # elif choice == '2':
    #     print("Bevásárlólista megtekintése")
    # elif choice == '3':
    #     print("Bevásárlólista optimalizálása")
    # elif choice == '4':
    #     print("Bevásárlólista törlése")

def console_main(recipes, menus, pantry):
    clear_console()
    main_menu(recipes, menus, pantry)
