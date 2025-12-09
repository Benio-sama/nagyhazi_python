import time
from console import console_main
from functions import clear_console, import_all
from recipes import read_recipe_from_file
from menu import read_menu_from_file
from pantry import read_pantry_from_file
from shopping_list import read_shopping_list_from_file

def main():
    clear_console()
    data = import_all('export.json')
    if len(data) > 0:
        print("Talált exportált adatfájl. Melyik forrást szeretnéd használni?")
        print("1. Helyi adatok")
        print("2. Exportált adatok (Figyelem: az exportált adatok felülírják a helyi adatokat!)")
        print("0. Kilépés")
        is_not_in_choices = False
        while True:
            choice = input("Válassz egy opciót: " if not is_not_in_choices else "Érvénytelen választás. Kérlek, válassz újra: ")
            if choice == '0':
                break
            elif choice == '1':
                recipes = read_recipe_from_file('jsons/recipes.json')
                menus = read_menu_from_file(recipes, 'jsons/menu.json')
                pantry = read_pantry_from_file('jsons/pantry.json')
                shopping_list = read_shopping_list_from_file('jsons/shopping_list.json')
                print("Üdvözöllek a Recept és menütervező, bevásárlólista kezelő alkalmazásban!")
                time.sleep(1.5)
                console_main(recipes, menus, pantry, shopping_list)
                break
            elif choice == '2':
                recipes = read_recipe_from_file(data[0])
                menus = read_menu_from_file(recipes, data[1])
                pantry = read_pantry_from_file(data[2])
                shopping_list = read_shopping_list_from_file(data[3])
                print("Üdvözöllek a Recept és menütervező, bevásárlólista kezelő alkalmazásban!")
                time.sleep(1.5)
                console_main(recipes, menus, pantry, shopping_list)
            else:
                is_not_in_choices = True
                continue
    else:
        recipes = read_recipe_from_file('jsons/recipes.json')
        menus = read_menu_from_file(recipes, 'jsons/menu.json')
        pantry = read_pantry_from_file('jsons/pantry.json')
        shopping_list = read_shopping_list_from_file('jsons/shopping_list.json')
        print("Üdvözöllek a Recept és menütervező, bevásárlólista kezelő alkalmazásban!")
        time.sleep(1.5)
        console_main(recipes, menus, pantry, shopping_list)
    

main()