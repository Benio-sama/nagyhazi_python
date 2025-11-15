import time
from recipes import Ingredient
from recipes import Recipe
from recipes import read_recipe_from_file
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def recipe_menu(recipes):
    from console import main_menu
    print("Receptek kezelése")
    print("1. Új recept hozzáadása")
    print("2. Recept módosítása")
    print("3. Recept törlése")
    print("4. Receptek listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu()
    elif choice == '1':
        recipes = add_recipe(recipes)
        recipe_menu(recipes)
    elif choice == '2':
        modify_recipe_menu(recipes)
        recipe_menu(recipes)
    elif choice == '3':
        recipes = delete_recipe(recipes)
        recipe_menu(recipes)
    elif choice == '4':
        list_recipes(recipes)
        recipe_menu(recipes)

def modify_menu():
    # clear_console()
    print("1. Név módosítása")
    print("2. Kategória módosítása")
    print("3. Adag módosítása")
    print("4. Hozzávalók módosítása")
    print("5. Elkészítési utasítások módosítása")
    print("0. Vissza a receptek kezelése menübe")

def modify_instructions_menu():
    # clear_console()
    print("Elkészítési utasítások módosítása")
    print("1. Utasítás hozzáadása")
    print("2. Utasítás törlése")
    print("3. Utasítás szerkesztése")
    print("0. Vissza a módosítási menübe")

def modify_ingredients_menu():
    # clear_console()
    print("Hozzávalók módosítása")
    print("1. Hozzávaló hozzáadása")
    print("2. Hozzávaló törlése")
    print("3. Hozzávaló szerkesztése")
    print("0. Vissza a módosítási menübe")

def modify_ingredient_menu():
    print("Hozzávaló módosítása")
    print("1. Név módosítása")
    print("2. Mennyiség módosítása")
    print("3. Mértékegység módosítása")
    print("0. Vissza a hozzávalók módosítása menübe")

def modify_header(name, category):
    print(f"{name} módosítása")
    print(f"Jelenlegi {name}:", category)
    print("0. Mégse")

def modify_ingredient_header(name, ingredient):
    print(f"{name} módosítása")
    print(f"Jelenlegi {name}:", ingredient)
    print("0. Mégse")

def back_to_menu(menu):
    time.sleep(1)
    menu()

def exit_if_0(value, recipes):
    if value == '0':
        print("Vissza a menübe.")
        time.sleep(1)
        recipe_menu(recipes)
    return 

def modify_body(headerfunc, s, value, setter, menufunc):
    headerfunc(s, value)
    new_value = input(f"Új {s.lower()}: ")
    if new_value:
        setter(int(new_value) if s == "Adag" else new_value)
        print("Sikeres módosítás.")
        back_to_menu(menufunc)
    else:
        menufunc()

def add_recipe(recipes):
    print("Új recept hozzáadása")
    print("0. Mégse")
    name = input("Recept neve: ")
    exit_if_0(name, recipes)
    category = input("Kategória: ")
    exit_if_0(category, recipes)
    servings = int(input("Adagok száma: "))
    exit_if_0(servings, recipes)
    ingredients = []
    ing_name = input("Hozzávaló neve (vagy 'kész' a befejezéshez): ")
    exit_if_0(ing_name, recipes)
    while ing_name != 'kesz':
        quantity_input = input("Mennyiség (ha ízlés szerint, hagyd üresen): ")
        quantity = float(quantity_input) if quantity_input else None
        exit_if_0(quantity, recipes)
        unit = input("Mértékegység: ")
        exit_if_0(unit, recipes)
        ingredients.append(Ingredient(len(ingredients), ing_name, quantity, unit))
        ing_name = input("Hozzávaló neve (vagy 'kész' a befejezéshez): ")
        exit_if_0(ing_name, recipes)
    instructions = []
    instr = input("Elkészítési utasítás (vagy 'kész' a befejezéshez): ")
    exit_if_0(instructions, recipes)
    while instr != 'kesz':
        instructions.append(instr)
        instr = input("Elkészítési utasítás (vagy 'kész' a befejezéshez): ")
        exit_if_0(instructions, recipes)
    recipes.append(Recipe(len(recipes), name, category, servings, ingredients, instructions))
    print(f"{name} hozzáadva.")
    return recipes

def modify_ingredient(recipe):
    print("Jelenlegi hozzávalók:")
    for ing in recipe.ingredients:
        print(f"{ing.id+1}, {ing}")
        edit_id = int(input("Szerkesztendő hozzávaló id-je: "))
        for ing in recipe.ingredients:
            if ing.id == edit_id-1:
                modify_ingredient_menu()
                ing_mod_choice = input("Válassz egy opciót: ")
                match ing_mod_choice:
                    case '0':
                        modify_ingredients_menu()
                    case '1':
                        modify_body(modify_ingredient_header, "Név", ing.name, ing._setname, modify_ingredient_menu)
                    case '2':
                        modify_body(modify_ingredient_header, "Mennyiség", ing.quantity, ing._setquantity, modify_ingredient_menu)
                    case '3':
                        modify_body(modify_ingredient_header, "Mértékegység", ing.unit, ing._setunit, modify_ingredient_menu)
            else:
                print("Hozzávaló nem található.")


def modify_recipe_menu(recipes):
    from console import main_menu
    print("Recept módosítása")
    for r in recipes:
        print(f"{r.id}, {r.name}")
    recipe_id = input("Add meg a módosítandó recept id-jét: ")
    for recipe in recipes:
        if recipe.id == int(recipe_id):
            print(f"Módosítod a '{recipe.name}' receptet:")
            modify_menu()
            choice = input("Válassz egy opciót: ")
            match choice:
                case '0':
                    main_menu()
                case '1':
                    modify_body(modify_header, "Név", recipe.name, recipe._setname, modify_menu)
                case '2':
                    modify_body(modify_header, "Kategória", recipe.category, recipe._setcategory, modify_menu)
                case '3':
                    modify_body(modify_header, "Adag", recipe.servings, recipe.scale_recipe, modify_menu)
                case '4':
                    modify_ingredients_menu()
                    ing_choice = input("Válassz egy opciót: ")
                    match ing_choice:
                        case '0':
                            modify_recipe_menu(recipes)
                        case '1':
                            ing_name = input("Hozzávaló neve: ")
                            quantity = float(input("Mennyiség: "))
                            unit = input("Mértékegység: ")
                            ingredient = Ingredient(len(recipe.ingredients), ing_name, quantity, unit)
                            recipe.add_ingredient(ingredient)
                            print("Hozzávaló hozzáadva.")
                            modify_recipe_menu(recipes)
                        case '2':
                            print("Jelenlegi hozzávalók:")
                            for ing in recipe.ingredients:
                                print(f"{ing.id+1}, {ing.name}")
                            id = int(input("Törlendő hozzávaló id-je: "))
                            confirm = input("Biztosan törlöd ezt a hozzávalót? (i/n): ")
                            if confirm.lower() == 'i':
                                recipe.remove_ingredient(id-1)
                                print("Hozzávaló törölve.")
                            else:
                                print("Törlés megszakítva.")
                            modify_recipe_menu(recipes)
                        case '3':
                            print("Jelenlegi hozzávalók:")
                            for ing in recipe.ingredients:
                                print(f"{ing.id+1}, {ing}")
                            edit_id = int(input("Szerkesztendő hozzávaló id-je: "))
                            for ing in recipe.ingredients:
                                if ing.id == edit_id-1:
                                    modify_ingredient_menu()
                                    ing_mod_choice = input("Válassz egy opciót: ")
                                    match ing_mod_choice:
                                        case '0':
                                            modify_ingredients_menu()
                                        case '1':
                                            modify_body(modify_ingredient_header, "Név", ing.name, ing._setname, modify_ingredient_menu)
                                        case '2':
                                            modify_body(modify_ingredient_header, "Mennyiség", ing.quantity, ing._setquantity, modify_ingredient_menu)
                                        case '3':
                                            modify_body(modify_ingredient_header, "Mértékegység", ing.unit, ing._setunit, modify_ingredient_menu)
                                else:
                                    print("Hozzávaló nem található.")
                            modify_recipe_menu(recipes)
                case '5':
                    modify_instructions_menu()
                    instr_choice = input("Válassz egy opciót: ")
                    match instr_choice:
                        case '0':
                            modify_recipe_menu(recipes)
                        case '1':
                            instruction = input("Új utasítás: ")
                            recipe.add_instruction(instruction)
                            print("Utasítás hozzáadva.")
                            modify_recipe_menu(recipes)
                        case '2':
                            print("Jelenlegi utasítások:")
                            for i, instr in enumerate(recipe.instructions):
                                print(f"{i+1}. {instr}")
                            index = int(input("Törlendő utasítás sorszáma: ")) - 1
                            confirm = input("Biztosan törlöd ezt az utasítást? (i/n): ")
                            if confirm.lower() == 'i':
                                recipe.remove_instruction(index)
                                print("Utasítás törölve.")
                            else:
                                print("Törlés megszakítva.")
                            modify_recipe_menu(recipes)
                        case '3':
                            print("Jelenlegi utasítások:")
                            for i, instr in enumerate(recipe.instructions):
                                print(f"{i+1}. {instr}")
                            index = int(input("Szerkesztendő utasítás sorszáma: ")) - 1
                            new_instruction = input("Új utasítás szövege: ")
                            recipe.instructions[index] = new_instruction
                            print("Utasítás módosítva.")
                            modify_recipe_menu(recipes)

def delete_recipe(recipes):
    print("Recept törlése")
    for r in recipes:
        print(r.id, r.name)
    recipe_id = input("Add meg a törlendő recept id-jét: ")
    for recipe in recipes:
        if recipe.id == int(recipe_id):
            confirm = input(f"Biztosan törölni akarod a '{recipe.name}' receptet? (i/n): ")
            if confirm.lower() == 'i':
                recipes.remove(recipe)
                print(f"Recept '{recipe.name}' törölve.")
                return recipes
            else:
                print("Törlés megszakítva.")
                return recipes
    print("Recept nem található.")
    return recipes

def list_recipes(recipes):
    print("Receptek listázása")
    for recipe in recipes:
        print(recipe._allinfo())

def recipe_main_menu():
    recipes = read_recipe_from_file('jsons/recipes.json')
    print("recipe main menu")
    recipe_menu(recipes)


# recipe_main_menu()