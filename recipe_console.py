import time
from recipes import Ingredient
from recipes import Recipe
from functions import clear_console, modify_header, modify_quantity, save_to_json

def recipe_menu(r_choice, recipes):

    save_to_json(recipes, "recipes.json")
    if r_choice == '1':
        clear_console()
        recipes = add_recipe(recipes)
    elif r_choice == '2':
        clear_console()
        recipes = modify_recipe_menu(recipes)
    elif r_choice == '3':
        clear_console()
        recipes = delete_recipe(recipes)
    elif r_choice == '4':
        clear_console()
        list_recipes(recipes)

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

def add_recipe(recipes):
    print("Új recept hozzáadása")
    print("0. Mégse")
    name = input("Recept neve: ")
    if name == '0':
        clear_console()
        return recipes
    category = input("Kategória: ")
    if category == '0':
        clear_console()
        return recipes
    servings = input("Adagok száma: ")
    while not servings.isdigit():
        print("Kérlek számot adj meg!")
        servings = input("Adagok száma: ")
    if servings == '0':
        clear_console()
        return recipes
    ingredients = []
    ing_name = input("Hozzávaló neve (vagy 'kész' a befejezéshez): ")
    if ing_name == '0':
        clear_console()
        return recipes
    while ing_name != 'kész':
        quantity_input = input("Mennyiség (ha ízlés szerint, hagyd üresen): ")
        if quantity_input:
            while True:
                try:
                    float_quantity = float(quantity_input)
                    break
                except ValueError:
                    print("Kérlek számot adj meg!")
                    quantity_input = input("Mennyiség (ha ízlés szerint, hagyd üresen): ")
        quantity = float_quantity if quantity_input else None
        if quantity == 0:
            clear_console()
            return recipes
        unit = input("Mértékegység: ")
        if unit == '0':
            clear_console()
            return recipes
        ingredients.append(Ingredient(len(ingredients), ing_name, quantity, unit))
        ing_name = input("Hozzávaló neve (vagy 'kész' a befejezéshez): ")
        if ing_name == '0':
            clear_console()
            return recipes
    instructions = []
    instr = input("Elkészítési utasítás (vagy 'kész' a befejezéshez): ")
    if instr == '0':
        clear_console()
        return recipes
    while instr != 'kész':
        instructions.append(instr)
        instr = input("Elkészítési utasítás (vagy 'kész' a befejezéshez): ")
        if instr == '0':
            clear_console()
            return recipes
    recipes.append(Recipe(len(recipes), name, category, int(servings), ingredients, instructions))
    print(f"{name} hozzáadva.")
    save_to_json(recipes, "recipes.json")
    return recipes

def modify_ingredient(recipe, recipes):
    print("Jelenlegi hozzávalók:")
    print("0. Mégse")
    for ing in recipe.ingredients:
        print(f"{ing.id+1}. {ing}")
    edit_id = input("Szerkesztendő hozzávaló száma: ")
    while not edit_id.isdigit() and edit_id != '0':
        edit_id = input("Érvénytelen választás. Kérlek, válassz újra: ")
    if edit_id == '0':
        return recipes
    for ing in recipe.ingredients:
        if ing.id == int(edit_id)-1:
            modify_ingredient_menu()
            ing_mod_choice = input("Válassz egy opciót: ")
            match ing_mod_choice:
                case '0':
                    clear_console()
                    return recipes
                case '1':
                    clear_console()
                    modify_header("Név", ing.name)
                    new_name = input("Új név: ")
                    if new_name == '0':
                        clear_console()
                        return recipes
                    if new_name:
                        ing._setname(new_name)
                        print("Sikeres módosítás.")
                        time.sleep(1)
                        clear_console()
                        save_to_json(recipes, "recipes.json")
                        return recipes
                    return recipes
                case '2':
                    clear_console()
                    modify_header("Mennyiség", ing.quantity)
                    new_quantity = input("Új mennyiség: ")
                    if new_quantity == '0':
                        clear_console()
                        return recipes
                    if new_quantity:
                        while True:
                            try:
                                float_quantity = float(new_quantity)
                                break
                            except ValueError:
                                print("Kérlek számot adj meg!")
                                new_quantity = input("Új mennyiség: ")
                        ing._setquantity(float_quantity)
                        print("Mennyiség módosítva.")
                        time.sleep(1)
                        clear_console()
                        return recipes
                    return recipes
                case '3':
                    print("Módosítod a mértékegységet, vagy konvertálni szeretnéd a mértékegységet?")
                    print("1. Módosítás")
                    print("2. Átváltás")
                    print("0. Mégse")
                    unit_choice = input("Válassz egy opciót: ")
                    if unit_choice == '0':
                        clear_console()
                        return recipes
                    match unit_choice:
                        case '1':
                            clear_console()
                            modify_header("Mennyiség", ing.quantity)
                            new_quantity = input("Új mennyiség: ")
                            if new_quantity == '0':
                                clear_console()
                                return recipes
                            if new_quantity:
                                while True:
                                    try:
                                        float_quantity = float(new_quantity)
                                        break
                                    except ValueError:
                                        print("Kérlek számot adj meg!")
                                        new_quantity = input("Új mennyiség: ")
                                ing._setquantity(float_quantity)
                                print("Mennyiség módosítva.")
                                time.sleep(1)
                                clear_console()
                                return recipes
                            return recipes
                        case '2':
                            modify_quantity(ing)
                            time.sleep(1)
                            clear_console()
                            save_to_json(recipes, "recipes.json")
                            return recipes
    print("Hozzávaló nem található.")
    clear_console()
    time.sleep(1)
    return recipes


def modify_recipe_menu(recipes):
    save_to_json(recipes, "recipes.json")
    print("Recept módosítása")
    print("0. Mégse")
    for r in recipes:
        print(f"{r.id+1}. {r.name}")
    recipe_id = input("Add meg a módosítandó recept id-jét: ")
    while recipe_id not in [str(r.id+1) for r in recipes] and recipe_id != '0':
        recipe_id = input("Érvénytelen választás. Kérlek, válassz újra: ")
    if recipe_id == '0':
        clear_console()
        return recipes
    for recipe in recipes:
        if recipe.id == int(recipe_id)-1:
            clear_console()
            print(f"Módosítod a '{recipe.name}' receptet:")
            modify_menu()
            choice = input("Válassz egy opciót: ")
            while choice not in ['0', '1', '2', '3', '4', '5']:
                choice = input("Érvénytelen választás. Kérlek, válassz újra: ")
            match choice:
                case '0':
                    clear_console()
                    return recipes
                case '1':
                    clear_console()
                    modify_header("Név", recipe.name)
                    new_name = input("Új név: ")
                    if new_name == '0':
                        clear_console()
                        return recipes
                    if new_name:
                        recipe._setname(new_name)
                        print("Sikeres módosítás.")
                        time.sleep(1)
                        clear_console()
                        save_to_json(recipes, "recipes.json")
                        return recipes
                    return recipes
                case '2':
                    clear_console()
                    modify_header("Kategória", recipe.category)
                    new_category = input("Új kategória: ")
                    if new_category == '0':
                        clear_console()
                        return recipes
                    if new_category:
                        recipe._setcategory(new_category)
                        print("Sikeres módosítás.")
                        time.sleep(1)
                        clear_console()
                        save_to_json(recipes, "recipes.json")
                        return recipes
                    return recipes
                case '3':
                    clear_console()
                    modify_header("Adag", recipe.servings)
                    serving = input("Új adag: ")
                    if serving == '0':
                        clear_console()
                        return recipes
                    if serving:
                        while not serving.isdigit():
                            print("Kérlek számot adj meg!")
                            serving = input("Új adag: ")
                        recipe.scale_recipe(float(serving))
                        print("Adag módosítva.")
                        time.sleep(1)
                        clear_console()
                        return recipes
                    return recipes
                case '4':
                    clear_console()
                    modify_ingredients_menu()
                    ing_choice = input("Válassz egy opciót: ")
                    match ing_choice:
                        case '0':
                            clear_console()
                            return recipes
                        case '1':
                            clear_console()
                            print("Hozzávaló hozzáadása")
                            print("0. Mégse")
                            ing_name = input("Hozzávaló neve: ")
                            if ing_name == '0':
                                clear_console()
                                return recipes
                            quantity_input = input("Mennyiség (ha ízlés szerint, hagyd üresen): ")
                            if quantity_input:
                                while True:
                                    try:
                                        float_quantity = float(quantity_input)
                                        break
                                    except ValueError:
                                        print("Kérlek számot adj meg!")
                                        quantity_input = input("Mennyiség (ha ízlés szerint, hagyd üresen): ")
                            quantity = float_quantity if quantity_input else None
                            if quantity == '0':
                                clear_console()
                                return recipes
                            unit = input("Mértékegység: ")
                            if unit == '0':
                                clear_console()
                                return recipes
                            ingredient = Ingredient(len(recipe.ingredients), ing_name, quantity, unit)
                            recipe.add_ingredient(ingredient)
                            print("Hozzávaló hozzáadva.")
                            time.sleep(1)
                            clear_console()
                            save_to_json(recipes, "recipes.json")
                            return recipes
                        case '2':
                            clear_console()
                            print("Hozzávaló törlése")
                            print("Jelenlegi hozzávalók:")
                            print("0. Mégse")
                            for ing in recipe.ingredients:
                                print(f"{ing.id+1}. {ing.name}")
                            id = input("Törlendő hozzávaló száma: ")
                            while not id.isdigit() and id != '0':
                                id = input("Érvénytelen választás. Kérlek, válassz újra: ")
                            if id == '0':
                                return recipes
                            for ing in recipe.ingredients:
                                if ing.id == int(id)-1:
                                    confirm = input(f"Biztosan törlöd a {ing.name} hozzávalót? (i/n): ")
                                    if confirm.lower() == 'i':
                                        recipe.remove_ingredient(ing.id)
                                        print("Hozzávaló törölve.")
                                        time.sleep(1)
                                        clear_console()
                                        save_to_json(recipes, "recipes.json")
                                        return recipes
                                    else:
                                        print("Törlés megszakítva.")
                                        time.sleep(1)
                                        clear_console()
                                        return recipes
                            print("Hozzávaló nem található.")
                            time.sleep(1)
                            clear_console()
                            save_to_json(recipes, "recipes.json")
                            return recipes
                        case '3':
                            recipes = modify_ingredient(recipe, recipes)
                            return recipes
                case '5':
                    clear_console()
                    modify_instructions_menu()
                    instr_choice = input("Válassz egy opciót: ")
                    while instr_choice not in ['0', '1', '2', '3']:
                        instr_choice = input("Érvénytelen választás. Kérlek, válassz újra: ")
                    match instr_choice:
                        case '0':
                            clear_console()
                            return recipes
                        case '1':
                            clear_console()
                            print("Utasítás hozzáadása")
                            print("0. Mégse")
                            instruction = input("Új utasítás: ")
                            if instruction == '0':
                                return recipes
                            recipe.add_instruction(instruction)
                            print("Utasítás hozzáadva.")
                            time.sleep(1)
                            clear_console()
                            save_to_json(recipes, "recipes.json")
                            return recipes
                        case '2':
                            clear_console()
                            print("Utasítás törlése")
                            print("Jelenlegi utasítások:")
                            print("0. Mégse")
                            for i, instr in enumerate(recipe.instructions):
                                print(f"{i+1}. {instr}")
                            index = input("Törlendő utasítás sorszáma: ")
                            while not index.isdigit() and index != '0':
                                index = input("Érvénytelen választás. Kérlek, válassz újra: ")
                            if index == '0':
                                return recipes
                            if int(index) < 1 or int(index) > len(recipe.instructions):
                                print("Utasítás nem található.")
                                time.sleep(1)
                                clear_console()
                                return recipes
                            confirm = input("Biztosan törlöd ezt az utasítást? (i/n): ")
                            if confirm.lower() == 'i':
                                recipe.remove_instruction(int(index)-1)
                                print("Utasítás törölve.")
                            else:
                                print("Törlés megszakítva.")
                            time.sleep(1)
                            clear_console()
                            save_to_json(recipes, "recipes.json")
                            return recipes
                        case '3':
                            clear_console()
                            print("Utasítás módosítása")
                            print("Jelenlegi utasítások:")
                            print("0. Mégse")
                            for i, instr in enumerate(recipe.instructions):
                                print(f"{i+1}. {instr}")
                            index = input("Szerkesztendő utasítás sorszáma: ")
                            while not index.isdigit() and index != '0':
                                index = input("Érvénytelen választás. Kérlek, válassz újra: ")
                            if index == '0':
                                return recipes
                            if int(index) < 1 or int(index) > len(recipe.instructions):
                                print("Utasítás nem található.")
                                time.sleep(1)
                                clear_console()
                                return recipes
                            new_instruction = input("Új utasítás szövege: ")
                            recipe.instructions[int(index)-1] = new_instruction
                            print("Utasítás módosítva.")
                            time.sleep(1)
                            clear_console()
                            save_to_json(recipes, "recipes.json")
                            return recipes
    print("Recept nem található.")
    return recipes
                            

def delete_recipe(recipes):
    print("Recept törlése")
    print("0. Mégse")
    if len(recipes) == 0:
        print("Nincs elérhető recept a törléshez.")
        return recipes
    for r in recipes:
        print(f"{r.id+1}. {r.name}")
    recipe_id = input("Add meg a törlendő recept id-jét: ")
    while recipe_id not in [str(r.id+1) for r in recipes] and recipe_id != '0':
        recipe_id = input("Érvénytelen választás. Kérlek, válassz újra: ")
    if recipe_id == '0':
        return recipes
    for recipe in recipes:
        if recipe.id == int(recipe_id)-1:
            confirm = input(f"Biztosan törölni akarod a '{recipe.name}' receptet? (i/n): ")
            if confirm.lower() == 'i':
                recipes.remove(recipe)
                print(f"{recipe.name} törölve.")
                time.sleep(1)
                save_to_json(recipes, "recipes.json")
                clear_console()
                return recipes
            else:
                print("Törlés megszakítva.")
                time.sleep(1)
                clear_console()
                return recipes
    print("Recept nem található.")
    save_to_json(recipes, "recipes.json")
    clear_console()
    time.sleep(1)
    return recipes

def list_recipes(recipes):
    print("Receptek listázása")
    if len(recipes) == 0:
        print("Nincs elérhető recept.")
        return
    for recipe in recipes:
        print(recipe._allinfo())

def recipe_main_menu(recipes):
    clear_console()
    is_not_in_choices = False
    while True:
        if not is_not_in_choices:
            print("Receptek kezelése")
            print("1. Új recept hozzáadása")
            print("2. Recept módosítása")
            print("3. Recept törlése")
            print("4. Receptek listázása")
            print("0. Vissza a főmenübe")
        r_choice = input("Válassz egy opciót: " if not is_not_in_choices else "Érvénytelen választás. Kérlek, válassz újra: ")
        if r_choice == '0':
            return recipes
        elif r_choice not in ['1', '2', '3', '4']:
            is_not_in_choices = True
            continue
        recipe_menu(r_choice, recipes)