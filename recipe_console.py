import time
from recipes import Ingredient
from recipes import Recipe
from functions import clear_console, exit_if_0, back_to_menu, modify_body, modify_header, save_to_json

def recipe_menu(recipes, menus, pantry):
    from console import main_menu

    save_to_json(recipes, "recipes.json")
    print("Receptek kezelése")
    print("1. Új recept hozzáadása")
    print("2. Recept módosítása")
    print("3. Recept törlése")
    print("4. Receptek listázása")
    print("0. Vissza a főmenübe")

    choice = input("Válassz egy opciót: ")
    if choice == '0':
        main_menu(recipes, menus, pantry)
    elif choice == '1':
        clear_console()
        recipes = add_recipe(recipes, menus, pantry)
        back_to_menu(recipe_menu, recipes, menus, pantry)
    elif choice == '2':
        clear_console()
        modify_recipe_menu(recipes, menus, pantry)
        clear_console()
        recipe_menu(recipes, menus, pantry)
    elif choice == '3':
        clear_console()
        recipes = delete_recipe(recipes)
        back_to_menu(recipe_menu, recipes, menus, pantry)
    elif choice == '4':
        clear_console()
        list_recipes(recipes)
        recipe_menu(recipes, menus, pantry)

def modify_menu():
    print("1. Név módosítása")
    print("2. Kategória módosítása")
    print("3. Adag módosítása")
    print("4. Hozzávalók módosítása")
    print("5. Elkészítési utasítások módosítása")
    print("0. Vissza a receptek kezelése menübe")

def modify_instructions_menu():
    print("Elkészítési utasítások módosítása")
    print("1. Utasítás hozzáadása")
    print("2. Utasítás törlése")
    print("3. Utasítás szerkesztése")
    print("0. Vissza a módosítási menübe")

def modify_ingredients_menu():
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

def add_recipe(recipes, menus, pantry):
    print("Új recept hozzáadása")
    print("0. Mégse")
    name = input("Recept neve: ")
    exit_if_0(name, recipe_menu, recipes, menus, pantry)
    category = input("Kategória: ")
    exit_if_0(category, recipe_menu, recipes, menus, pantry)
    servings = int(input("Adagok száma: "))
    exit_if_0(servings, recipe_menu, recipes, menus, pantry)
    ingredients = []
    ing_name = input("Hozzávaló neve (vagy 'kész' a befejezéshez): ")
    exit_if_0(ing_name, recipe_menu, recipes, menus, pantry)
    while ing_name != 'kesz':
        quantity_input = input("Mennyiség (ha ízlés szerint, hagyd üresen): ")
        quantity = float(quantity_input) if quantity_input else None
        exit_if_0(quantity, recipe_menu, recipes, menus, pantry)
        unit = input("Mértékegység: ")
        exit_if_0(unit, recipe_menu, recipes, menus, pantry)
        ingredients.append(Ingredient(len(ingredients), ing_name, quantity, unit))
        ing_name = input("Hozzávaló neve (vagy 'kész' a befejezéshez): ")
        exit_if_0(ing_name, recipe_menu, recipes, menus, pantry)
    instructions = []
    instr = input("Elkészítési utasítás (vagy 'kész' a befejezéshez): ")
    exit_if_0(instructions, recipe_menu, recipes, menus, pantry)
    while instr != 'kesz':
        instructions.append(instr)
        instr = input("Elkészítési utasítás (vagy 'kész' a befejezéshez): ")
        exit_if_0(instructions, recipe_menu, recipes, menus, pantry)
    recipes.append(Recipe(len(recipes), name, category, servings, ingredients, instructions))
    print(f"{name} hozzáadva.")
    save_to_json(recipes, "recipes.json")
    return recipes

def modify_ingredient(recipe, recipes, menus, pantry):
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
                    modify_body(modify_header, "Név", ing.name, ing._setname, modify_recipe_menu, recipes, menus, pantry)
                case '2':
                    modify_body(modify_header, "Mennyiség", ing.quantity, ing._setquantity, modify_recipe_menu, recipes, menus, pantry)
                case '3':
                    modify_body(modify_header, "Mértékegység", ing.unit, ing._setunit, modify_recipe_menu, recipes, menus, pantry)
    print("Hozzávaló nem található.")
    back_to_menu(modify_recipe_menu, recipes, menus, pantry)


def modify_recipe_menu(recipes, menus, pantry):
    print("Recept módosítása")
    for r in recipes:
        print(f"{r.id+1}, {r.name}")
    recipe_id = input("Add meg a módosítandó recept id-jét: ")
    for recipe in recipes:
        if recipe.id == int(recipe_id)-1:
            clear_console()
            print(f"Módosítod a '{recipe.name}' receptet:")
            modify_menu()
            choice = input("Válassz egy opciót: ")
            match choice:
                case '0':
                    clear_console()
                    recipe_menu(recipes, menus, pantry)
                case '1':
                    modify_body(modify_header, "Név", recipe.name, recipe._setname, modify_menu)
                case '2':
                    modify_body(modify_header, "Kategória", recipe.category, recipe._setcategory, modify_menu)
                case '3':
                    modify_body(modify_header, "Adag", recipe.servings, recipe.scale_recipe, modify_menu)
                case '4':
                    clear_console()
                    modify_ingredients_menu()
                    ing_choice = input("Válassz egy opciót: ")
                    match ing_choice:
                        case '0':
                            clear_console()
                            modify_recipe_menu(recipes, menus, pantry)
                        case '1':
                            clear_console()
                            print("Hozzávaló hozzáadása")
                            ing_name = input("Hozzávaló neve: ")
                            quantity = float(input("Mennyiség: "))
                            unit = input("Mértékegység: ")
                            ingredient = Ingredient(len(recipe.ingredients), ing_name, quantity, unit)
                            recipe.add_ingredient(ingredient)
                            print("Hozzávaló hozzáadva.")
                            back_to_menu(modify_recipe_menu, recipes, menus, pantry)
                        case '2':
                            clear_console()
                            print("Hozzávaló törlése")
                            print("Jelenlegi hozzávalók:")
                            for ing in recipe.ingredients:
                                print(f"{ing.id+1}, {ing.name}")
                            id = int(input("Törlendő hozzávaló id-je: "))
                            for ing in recipe.ingredients:
                                if ing.id == id-1:
                                    confirm = input("Biztosan törlöd ezt a hozzávalót? (i/n): ")
                                    if confirm.lower() == 'i':
                                        recipe.remove_ingredient(id-1)
                                        print("Hozzávaló törölve.")
                                    else:
                                        print("Törlés megszakítva.")
                            print("Hozzávaló nem található.")
                            back_to_menu(modify_recipe_menu, recipes, menus, pantry)
                        case '3':
                            modify_ingredient(recipe, recipes, menus, pantry)
                case '5':
                    clear_console()
                    modify_instructions_menu()
                    instr_choice = input("Válassz egy opciót: ")
                    match instr_choice:
                        case '0':
                            clear_console()
                            modify_recipe_menu(recipes, menus, pantry)
                        case '1':
                            clear_console()
                            print("Utasítás hozzáadása")
                            instruction = input("Új utasítás: ")
                            recipe.add_instruction(instruction)
                            print("Utasítás hozzáadva.")
                            back_to_menu(modify_instructions_menu)
                        case '2':
                            clear_console()
                            print("Utasítás törlése")
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
                            back_to_menu(modify_instructions_menu)
                        case '3':
                            clear_console()
                            print("Utasítás módosítása")
                            print("Jelenlegi utasítások:")
                            for i, instr in enumerate(recipe.instructions):
                                print(f"{i+1}. {instr}")
                            index = int(input("Szerkesztendő utasítás sorszáma: ")) - 1
                            new_instruction = input("Új utasítás szövege: ")
                            recipe.instructions[index] = new_instruction
                            print("Utasítás módosítva.")
                            back_to_menu(modify_instructions_menu)
                            

def delete_recipe(recipes):
    print("Recept törlése")
    for r in recipes:
        print(r.id+1, r.name)
    recipe_id = input("Add meg a törlendő recept id-jét: ")
    for recipe in recipes:
        if recipe.id == int(recipe_id)-1:
            confirm = input(f"Biztosan törölni akarod a '{recipe.name}' receptet? (i/n): ")
            if confirm.lower() == 'i':
                recipes.remove(recipe)
                print(f"{recipe.name} törölve.")
                return recipes
            else:
                print("Törlés megszakítva.")
                return recipes
    print("Recept nem található.")
    save_to_json(recipes, "recipes.json")
    return recipes

def list_recipes(recipes):
    print("Receptek listázása")
    for recipe in recipes:
        print(recipe._allinfo())

def recipe_main_menu(recipes, menus, pantry):
    clear_console()
    recipe_menu(recipes, menus, pantry)