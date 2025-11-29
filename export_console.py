import json
from functions import back_to_menu

def export_all(recipes, menus, pantry, shopping_list, filename):
    data = {
        "recipes": [item.to_dict() for item in recipes],
        "menus": [item.to_dict() for item in menus],
        "pantry": [item.to_dict() for item in pantry],
        "shopping_list": [item.to_dict() for item in shopping_list.items],
    }

    with open(f"jsons/{filename}", "wt", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def export_main(recipes, menus, pantry, shopping_list):
    from console import main_menu
    
    export_all(recipes, menus, pantry, shopping_list, "export.json")
    print("Adatok exportálva export.json fájlba.")
    back_to_menu(main_menu, recipes, menus, pantry, shopping_list)