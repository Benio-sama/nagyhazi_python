from functions import clear_console, conversion, modify_header, modify_quantity, save_to_json, special_round
from shopping_list import ShoppingList, ShoppingList_Item
import time

def shopping_list_menu(s_choice, menus, pantry, shopping_list):

    save_to_json(shopping_list.items, 'shopping_list.json')
    if s_choice == '1':
        clear_console()
        print("Bevásárlólista generálása/frissítése...")
        new_shopping_list = generate_shopping_list(menus, pantry, shopping_list)
        time.sleep(1)
        print("Bevásárlólista optimalizálása...")
        shopping_list = shopping_list_optimize(new_shopping_list, shopping_list)
        time.sleep(1)
        print("Bevásárlólista optimalizálva.")
    elif s_choice == '2':
        clear_console()
        list_shopping_list(shopping_list)
    elif s_choice == '3':
        clear_console()
        shopping_list = delete_shopping_list(shopping_list)
    elif s_choice == '4':
        clear_console()
        shopping_list = convert_shopping_list_item_units(shopping_list)
    elif s_choice == '5':
        clear_console()
        shopping_list = add_shopping_list_item(shopping_list)
    elif s_choice == '6':
        shopping_list = modify_shopping_list_item(shopping_list)
    elif s_choice == '7':
        clear_console()
        shopping_list = delete_shopping_list_item(shopping_list)

def generate_shopping_list(menus, pantry):
    new_shopping_list = ShoppingList()
    for menu in menus:
        for recipe in menu.recipes:
            for ing in recipe.ingredients:
                found = False
                for pantry_item in pantry:
                    if ing.name == pantry_item.name:
                        found = True
                        converted_ing_quantity = conversion(ing, pantry_item.unit)
                        needed_quantity = converted_ing_quantity - pantry_item.quantity
                        if needed_quantity > 0:
                            new_shopping_list.items.append(ShoppingList_Item(len(new_shopping_list.items), ing.name, needed_quantity, pantry_item.unit))
                            if pantry_item.quantity != 0:
                                pantry_item.remove_quantity(converted_ing_quantity - needed_quantity)
                        else:
                            pantry_item.remove_quantity(converted_ing_quantity)
                        break
                if not found:
                    new_shopping_list.items.append(ShoppingList_Item(len(new_shopping_list.items), ing.name, ing.quantity, ing.unit))  
    save_to_json(pantry, 'pantry.json')
    new_shopping_list.items.sort(key=lambda x: x.name)
    save_to_json(new_shopping_list.items, 'shopping_list.json')
    print("Bevásárlólista generálva és elmentve shopping_list.json fájlba.")
    return new_shopping_list

def shopping_list_optimize(new_shopping_list, shopping_list):
    new_list = ShoppingList()
    for item in new_shopping_list.items:
        found = False
        for new_item in new_list.items:
            if item.name == new_item.name:
                if item.unit == new_item.unit:
                    new_item.add_quantity(item)
                else:
                    converted_quantity = special_round(conversion(item, new_item.unit), False, False)
                    if converted_quantity is not None and converted_quantity is not False:
                        new_item.add_quantity(ShoppingList_Item(item.id, item.name, converted_quantity, new_item.unit))
                    elif converted_quantity is False:
                        new_list.items.append(item)
                found = True
                break
        if not found:
            new_list.items.append(item)
    for i in shopping_list.items:
        found = False
        for item in new_list.items:
            if i.name == item.name:
                if i.unit == item.unit:
                    item.add_quantity(i)
                else:
                    converted_quantity = special_round(conversion(i, item.unit), False, False)
                    if converted_quantity is not None and converted_quantity is not False:
                        item.add_quantity(ShoppingList_Item(i.id, i.name, converted_quantity, item.unit))
                    elif converted_quantity is False:
                        new_shopping_list.items.append(i)
                found = True
                break
        if not found:
            max = new_list.items[0].id if len(new_list.items) > 0 else 0
            for mitem in new_list.items:
                if mitem.id > max:
                    max = mitem.id
            new_list.items.append(ShoppingList_Item(max+1, i.name, i.quantity, i.unit))
    save_to_json(new_list.items, 'shopping_list.json')
    return new_list

def convert_shopping_list_item_units(shopping_list):
    print("Bevásárlólista mértékegységeinek konvertálása")
    for i in shopping_list.items:
        print(f"{i.id+1}. {i.name}: {i.quantity} {i.unit}")
    item_id = input("Add meg a konvertálandó tétel számát: ")
    while not item_id.isdigit():
        print("Kérlek számot adj meg!")
        item_id = input("Add meg a konvertálandó tétel számát: ")
    if item_id == '0':
        clear_console()
        return shopping_list
    for i in shopping_list.items:
        if i.id == int(item_id)-1:
            print(f"Jelenlegi mértékegység: {i.unit}")
            new_unit = input(f"Add meg az új mértékegységet: ")
            if new_unit == '0':
                clear_console()
                return shopping_list
            if new_unit == "ízles szerint":
                i.unit = new_unit
                i.quantity = None
            elif i.unit == "ízles szerint":
                print("Nem konvertálható az 'ízles szerint' mértékegységből.")
            else:
                converted_quantity = conversion(i, new_unit)
                if converted_quantity is not False:
                    i.quantity = special_round(converted_quantity, False, False)
                    i.unit = new_unit
                    print(f"Sikeres konvertálás: {i.name} új mennyiség: {i.quantity} {i.unit}")
                    time.sleep(1)
                    clear_console()
                    save_to_json(shopping_list.items, 'shopping_list.json')
                    return shopping_list
                else:
                    print("A konverzió nem lehetséges a megadott mértékegységre.")
                    time.sleep(1)
                    clear_console()
                    return shopping_list
    print("Tétel nem található.")
    return shopping_list

def list_shopping_list(shopping_list):
    print("Bevásárlólista tartalma:")
    if len(shopping_list.items) == 0:
        print("A bevásárlólista üres.")
    else:
        for item in shopping_list.items:
            if item.quantity is None:
                print(f"\t- {item.name}: {item.unit}")
            else:
                print(f"\t- {item.name}: {item.quantity} {item.unit}")

def delete_shopping_list(shopping_list):
    print("Bevásárlólista törlése")
    confirm = input("Biztosan törölni akarod a teljes bevásárlólistát? (i/n): ")
    if confirm.lower() == 'i':
        shopping_list.items.clear()
        save_to_json(shopping_list.items, 'shopping_list.json')
        print("Bevásárlólista törölve.")
    else:
        print("Törlés megszakítva.")
    time.sleep(1)
    clear_console()
    return shopping_list

def add_shopping_list_item(shopping_list):
    print("Tétel hozzáadása")
    print("0. Mégse")
    name = input("Add meg a hozzávaló nevét: ")
    if name == '0':
        clear_console()
        return shopping_list
    quantity_input = input("Add meg a mennyiséget: ")
    while not quantity_input.isdigit():
        print("Kérlek számot adj meg!")
        quantity_input = input("Add meg a mennyiséget: ")
    quantity = float(quantity_input)
    if quantity == 0:
        clear_console()
        return shopping_list
    unit = input("Add meg a mértékegységet: ")
    if unit == '0':
        clear_console()
        return shopping_list
    new_item = ShoppingList_Item(len(shopping_list.items), name, quantity, unit)
    shopping_list.items.append(new_item)
    save_to_json(shopping_list.items, 'shopping_list.json')
    print(f"Sikeres hozzáadás: {new_item.name} {new_item.quantity} {new_item.unit}")
    time.sleep(1)
    clear_console()
    return shopping_list

def modify_shopping_list_item(shopping_list):
    save_to_json(shopping_list.items, 'shopping_list.json')
    clear_console()
    print("Tétel módosítása")
    print("0. Mégse")
    for item in shopping_list.items:
        print(f"{item.id+1}. {item.name}: {item.quantity} {item.unit}")
    item_id = input("Add meg a módosítandó tétel számát: ")
    while not item_id.isdigit():
        print("Kérlek számot adj meg!")
        item_id = input("Add meg a módosítandó tétel számát: ")
    if item_id == '0':
        clear_console()
        return shopping_list
    for item in shopping_list.items:
        if item.id == int(item_id)-1:
            print("1. Név módosítása")
            print("2. Mennyiség módosítása")
            print("3. Mértékegység módosítása")
            print("0. Mégse")
            mod_choice = input("Válassz egy opciót: ")
            while mod_choice not in ['0', '1', '2', '3']:
                mod_choice = input("Érvénytelen választás. Kérlek, válassz újra: ")
            match mod_choice:
                case '0':
                    clear_console()
                    return shopping_list
                case '1':
                    clear_console()
                    modify_header("Név", item.name)
                    new_name = input("Új név: ")
                    if new_name == '0':
                        clear_console()
                        return shopping_list
                    if new_name:
                        item._setname(new_name)
                        print("Név módosítva.")
                        time.sleep(1)
                        clear_console()
                        save_to_json(shopping_list.items, 'shopping_list.json')
                        return shopping_list
                    return shopping_list
                case '2':
                    clear_console()
                    modify_header("Mennyiség", item.quantity)
                    new_quantity = input("Új mennyiség: ")
                    if new_quantity == '0':
                        clear_console()
                        return shopping_list
                    if new_quantity:
                        while not new_quantity.isdigit():
                            print("Kérlek számot adj meg!")
                            new_quantity = input("Új mennyiség: ")
                        item._setquantity(float(new_quantity))
                        print("Mennyiség módosítva.")
                        time.sleep(1)
                        clear_console()
                        save_to_json(shopping_list.items, 'shopping_list.json')
                        return shopping_list
                    return shopping_list
                case '3':
                    print("Módosítod a mértékegységet, vagy konvertálni szeretnéd a mértékegységet?")
                    print("1. Módosítás")
                    print("2. Átváltás")
                    print("0. Mégse")
                    unit_choice = input("Válassz egy opciót: ")
                    while unit_choice not in ['0', '1', '2']:
                        unit_choice = input("Érvénytelen választás. Kérlek, válassz újra: ")
                    match unit_choice:
                        case '0':
                            clear_console()
                            return shopping_list
                        case '1':
                            clear_console()
                            modify_header("Mértékegység", item.unit)
                            new_unit = input("Új mértékegység: ")
                            if new_unit == '0':
                                clear_console()
                                return shopping_list
                            if new_unit:
                                item._setunit(new_unit)
                                print("Mértékegység módosítva.")
                                time.sleep(1)
                                clear_console()
                                save_to_json(shopping_list.items, 'shopping_list.json')
                                return shopping_list
                            return shopping_list
                        case '2':
                            modify_quantity(item)
                            time.sleep(1)
                            save_to_json(shopping_list.items, 'shopping_list.json')
                            clear_console()
                            return shopping_list
    save_to_json(shopping_list.items, 'shopping_list.json')
    return shopping_list

def delete_shopping_list_item(shopping_list):
    print("Tétel törlése")
    print("0. Mégse")
    for item in shopping_list.items:
        if item.quantity is None:
            print(f"{item.id+1}. {item.name}: {item.unit}")
        else:
            print(f"{item.id+1}. {item.name}: {item.quantity} {item.unit}")
    item_id = input("Add meg a törlendő tétel számát: ")
    while not item_id.isdigit():
        print("Kérlek számot adj meg!")
        item_id = input("Add meg a törlendő tétel számát: ")
    if item_id == '0':
        return shopping_list
    for item in shopping_list.items:
        if item.id == int(item_id)-1:
            confirm = input(f"Biztosan törlöd a(z) {item.name} tételt? (i/n): ")
            if confirm.lower() == 'i':
                shopping_list.items.remove(item)
                print("Tétel törölve.")
                save_to_json(shopping_list.items, 'shopping_list.json')
                time.sleep(1)
                clear_console()
                return shopping_list
            else:
                print("Törlés megszakítva.")
                time.sleep(1)
                clear_console()
                return shopping_list
    print("Tétel nem található.")
    time.sleep(1)
    clear_console()
    return shopping_list

def shopping_list_main(recipes, menus, pantry, shopping_list):
    from console import console_main

    clear_console()
    is_not_in_choices = False
    while True:
        if not is_not_in_choices:
            print("Bevásárlólista kezelése")
            print("1. Bevásárlólista generálása/frissítése")
            print("2. Bevásárlólista megtekintése")
            print("3. Bevásárlólista törlése")
            print("4. Mértékegységek konvertálása")
            print("5. Tétel hozzáadása")
            print("6. Tétel módosítása")
            print("7. Tétel törlése")
            print("0. Vissza a főmenübe")
        s_choice = input("Válassz egy opciót: " if not is_not_in_choices else "Érvénytelen választás. Kérlek, válassz újra: ")
        if s_choice == '0':
            console_main(recipes, menus, pantry, shopping_list)
        elif s_choice in ['1', '2', '3', '4', '5', '6', '7']:
            is_not_in_choices = True
            continue
        shopping_list_menu(recipes, menus, pantry, shopping_list)