import math
import os
import time
import json

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_if_0(value, menu, *args):
    if (isinstance(value, list) and '0' in value) or (isinstance(value, float) and value == 0) or value == '0' or value == 0:
        print("Vissza a menübe.")
        time.sleep(1)
        clear_console()
        menu(*args)
    return 

def back_to_menu(menu, *args):
    time.sleep(1)
    clear_console()
    menu(*args)

def conversion(item, new_unit: str):
    conversions = {
        ('g', 'kg'): 0.001,
        ('g', 'dkg'): 0.1,
        ('dkg', 'g'): 10,
        ('dkg', 'kg'): 0.01,
        ('kg', 'g'): 1000,
        ('kg', 'dkg'): 100,
        ('ml', 'l'): 0.001,
        ('ml', 'dl'): 0.01,
        ('dl', 'ml'): 100,
        ('dl', 'l'): 0.1,
        ('l', 'dl'): 10,
        ('l', 'ml'): 1000,
        ('db', 'db'): 1,
        ('fej', 'fej'): 1,
        ('szem', 'szem'): 1,
        ('gerezd', 'gerezd'): 1,
        ('ízlés szerint', 'ízlés szerint'): 1,
        ('szál', 'szál'): 1,
        ('csokor', 'csokor'): 1,
        ('szelet', 'szelet'): 1,
        ('késhegynyi', 'késhegynyi'): 1,
        ('tk', 'ek'): 3,
        ('ek', 'tk'): 1/3,
        ('kk', 'ek'): 1/6,
        ('ek', 'kk'): 6,
        ('kk', 'tk'): 1/2,
        ('tk', 'kk'): 2,
        ('cup', 'ml'): 240,
        ('ml', 'cup'): 1/240, 
        ('ml', 'tk'): 0.2,
        ('tk', 'ml'): 5,
        ('ml', 'ek'): 1/15,
        ('ek', 'ml'): 15,
        ('ml', 'kk'): 1/2.5,
        ('kk', 'ml'): 2.5,
        ('ek', 'l'): 0.015,
        ('l', 'ek'): 66.6667,
        ('tk', 'l'): 0.005,
        ('l', 'tk'): 200,
        ('kk', 'l'): 0.0025,
        ('l', 'kk'): 400,
        ('ek', 'dl'): 0.15,
        ('dl', 'ek'): 6.6666667,
        ('tk', 'dl'): 0.05,
        ('dl', 'tk'): 20,
        ('kk', 'dl'): 0.025,
        ('dl', 'kk'): 40,
        ('l', 'cup'): 4.167,
        ('cup', 'l'): 0.24,
    }

    spoon_ml = {
        'ek': 15,
        'tk': 5,
        'kk': 2.5,
    }
    
    volume = {
        'cukor': 0.85,
        'kristálycukor': 0.85,
        'porcukor': 0.56,
        'barna cukor': 0.72,
        'nádcukor': 0.80,
        'vaníliás cukor': 0.60,
        'finomliszt': 0.53,
        'rétesliszt': 0.50,
        'teljes kiőrlésű liszt': 0.60,
        'rizsliszt': 0.55,
        'kukoricaliszt': 0.58,
        'burgonyaliszt': 0.70,
        'mandulaliszt': 0.45,
        'kókuszliszt': 0.40,
        'búzadara': 0.60,
        'kukoricakeményítő': 0.55,
        'burgonyakeményítő': 0.80,
        'olaj': 0.92,
        'olívaolaj': 0.91,
        'vaj': 0.96,
        'margarin': 0.95,
        'zsír': 0.92,
        'sertészsír': 0.92,
        'kókuszolaj': 0.92,
        'tej': 1.03,
        'tejszín': 1.01,
        'habtejszín': 1.01,
        'sűrített_tejszín': 1.20,
        'joghurt': 1.04,
        'görög joghurt': 1.10,
        'kefír': 1.03,
        'tejföl': 1.00,
        'krémsajt': 1.05,
        'víz': 1.00,
        'almaecet': 1.01,
        'borecet': 1.01,
        'méz': 1.40,
        'juharszirup': 1.32,
        'agávészirup': 1.33,
        'darált dió': 0.45,
        'darált mák': 0.60,
        'darált mandula': 0.45,
        'darált mogyoró': 0.50,
        'kókuszreszelék': 0.37,
        'rizs': 0.85,
        'bulgur': 0.60,
        'kuszkusz': 0.60,
        'zabpehely': 0.40,
        'kakaópor': 0.50,
        'cukrozatlan kakaópor': 0.45,
        'csokoládé reszelék': 0.55,
        'só': 1.20,
        'szódabikarbóna': 1.00,
        'sütőpor': 0.90,
        'zselatin por': 0.80,
        'almapüré': 1.05,
        'banánpüré': 1.10,
        'kókuszkrém': 1.05,
        'paradicsompüré': 1.06,
        'paradicsomszósz': 1.02,
        'csicseriborsó püré': 1.10,
        'babpüré': 1.15,
        'avokádó püré': 1.10,
        'tökhús püré': 1.00,
        'burgonyapüré': 0.85,
        'eperpüré': 1.00,
        'mangópüré': 1.12,
        'szilvapüré': 1.05,
        'körtépüré': 1.03,
        'fahéj': 0.56,
        'őrölt fahéj': 0.52,
        'őrölt gyömbér': 0.55,
        'őrölt szegfűszeg': 0.53,
        'őrölt szerecsendió': 0.56,
        'kurkuma': 0.54,
        'őrölt kömény': 0.52,
        'őrölt paprika': 0.54,
        'füstölt paprika': 0.50,
        'chili por': 0.45,
        'cayenne': 0.45,
        'fokhagymapor': 0.72,
        'hagymapor': 0.56,
        'vaníliapor': 0.45,
        'szárított oregánó': 0.20,
        'szárított bazsalikom': 0.15,
        'szárított petrezselyem': 0.10,
        'szárított majoranna': 0.12,
        'szárított kakukkfű': 0.18,
        'szárított rozmaring': 0.20,
        'oregánó': 0.6,
        'bazsalikom': 0.4,
        'petrezselyem': 0.3,
        'majoranna': 0.5,
        'kakukkfű': 0.7,    
        'rozmaring': 0.8,
        'kapor': 0.3,
        'menta': 0.4,
        'snidling': 0.3,
        'metélőhagyma': 0.3,
        'koriander': 0.4,
        'zsálya': 0.5,
        'zúzott fokhagyma': 0.8,
        'aprított vöröshagyma': 0.6,
        'reszelt hagyma': 0.75,
        'reszelt gyömbér': 0.6,
        'aprított erőspaprika': 0.55,
        'aprított chili': 0.50,
        'majonéz': 0.95,
        'mustár': 1.14,
        'ketchup': 1.10,
        'bbq_szósz': 1.20,
        'tartármártás': 0.98,
        'fokhagymás_szósz': 1.05,
        'csípős_szósz': 1.00,
        'majonézalapú_szósz': 0.95,
        'joghurtos_szósz': 1.04,
        'csiliszósz': 1.12,
        'édes-savanyú_szósz': 1.15,
        'szójaszósz': 1.20,
        'teriyaki_szósz': 1.17,
        'halmártás': 1.20,
        'balzsamecet krém': 1.33,  
    }

    if item.unit == new_unit:
        return item.quantity
    if item.unit in ('kk', 'ek', 'tk') and new_unit in ('g', 'dkg', 'kg'):
        if item.name not in volume:
            print(f"Nincs sűrűségi adat ehhez a hozzávalóhoz: {item.name}")
            return False
        ml = item.quantity * spoon_ml[item.unit]
        gramm = ml * volume[item.name]
        if new_unit == 'g':
            return gramm
        if new_unit == 'dkg':
            return gramm / 10
        if new_unit == 'kg':
            return gramm / 1000

    if item.unit in ('g', 'dkg', 'kg') and new_unit in ('kk', 'ek', 'tk'):
        if item.name not in volume:
            print(f"Nincs sűrűségi adat ehhez a hozzávalóhoz: {item.name}")
            return False
        gramm = item.quantity
        if item.unit == 'dkg':
            gramm *= 10
        if item.unit == 'kg':
            gramm *= 1000
        ml = gramm / volume[item.name]
        return ml / spoon_ml[new_unit]
    
    if item.unit == "ízlés szerint" or new_unit == "ízlés szerint":
        return False

    key = (item.unit, new_unit)
    if key in conversions:
        return item.quantity * conversions[key]
    else:
        print(f"Nincs konverzió {item.unit} és {new_unit} között.")
        return False

        
def modify_body(headerfunc, s, value, setter, menufunc, *args):
    clear_console()
    headerfunc(s, value)
    new_value = input(f"Új {s.lower()}: ")
    exit_if_0(new_value, menufunc, *args)
    if new_value:
        setter(int(new_value) if s == "Adag" else new_value)
        print("Sikeres módosítás.")
        back_to_menu(menufunc, *args)
    else:
        menufunc()

def modify_header(name, value):
    print(f"{name} módosítása")
    print(f"Jelenlegi {name}:", value)
    print("0. Mégse")


def save_to_json(list, filename):
    data = [item.to_dict() for item in list]
    with open(f"jsons/{filename}", "wt", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def special_round(x, spec, down):
    whole = math.floor(x)
    decimal = x - whole
    if decimal == 0:
        return x
    elif decimal > 0.5:
        if spec == False:
            return math.ceil(x) 
        else:
            return math.floor(x)
    elif decimal < 0.5:
        if spec == False:
            return whole + 0.5 if down == False else math.floor(x)
        else:
            if whole == 0:
                return whole + 0.5
            return math.floor(x)
    else:
        if spec == False:
            return x 
        else:
            return math.ceil(x)
        
def modify_quantity(item):
    print(f"Jelenlegi mértékegység: {item.unit}")
    new_unit = input(f"Add meg az új mértékegységet: ")
    converted_quantity = conversion(item, new_unit)
    item.unit = new_unit
    if converted_quantity is not False:
        item.quantity = special_round(converted_quantity, False, False)
        print(f"Sikeres konvertálás!")
    else:
        print("A konverzió nem lehetséges a megadott mértékegységre.")

def import_all(filename):
    with open(f"jsons/{filename}", "rt", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    return (
        data.get("recipes", []),
        data.get("menus", []),
        data.get("pantry", []),
        data.get("shopping_list", [])
    )

def import_from_files():
    from menu import read_menu_from_file
    from pantry import read_pantry_from_file
    from recipes import read_recipe_from_file
    from shopping_list import read_shopping_list_from_file
    
    recipes = read_recipe_from_file('jsons/recipes.json')
    menus = read_menu_from_file(recipes, 'jsons/menu.json')
    pantry = read_pantry_from_file('jsons/pantry.json')
    shopping_list = read_shopping_list_from_file('jsons/shopping_list.json')

    return recipes, menus, pantry, shopping_list