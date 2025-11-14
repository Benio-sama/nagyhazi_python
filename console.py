def main_menu():
    from recipe_console import recipe_main_menu

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
            recipe_main_menu()
        elif choice == '2':
            pantry_menu()
        elif choice == '3':
            menu_menu()
        elif choice == '4':
            shopping_list_menu()
        elif choice == '5':
            print("Adatok mentése / betöltése")
        elif choice == '6':
            print("Adatok exportálása")
        else:
            print("Érvénytelen választás. Próbáld újra.")
            main_menu()
            choice = input("Válassz egy opciót: ")
    exit()

def pantry_menu():
    print("Kamra kezelése")
    print("1. Hozzávaló hozzáadása")
    print("2. Hozzávaló módosítása")
    print("3. Hozzávaló törlése")
    print("4. Kamra tartalmának listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu()

def menu_menu():
    print("Menü kezelése")
    print("1. Napi menü hozzáadása")
    print("2. Napi menü módosítása")
    print("3. Napi menü törlése")
    print("4. Napi menük listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu()

def shopping_list_menu():
    print("Bevásárlólista kezelése")
    print("1. Bevásárlólista generálása")
    print("2. Bevásárlólista megtekintése")
    print("3. Bevásárlólista optimalizálása")
    print("4. Bevásárlólista törlése")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu()

def main():
    main_menu()

main()