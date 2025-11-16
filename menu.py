import json
from recipes import read_recipe_from_file
from recipes import Recipe

class Menu:
    def __init__(self, id: int, day, recipes: list[Recipe] = []):
        self.id = id
        self.day = day
        self.recipes = recipes

    def __str__(self):
        recipes_str = "\n".join([str(rec) for rec in self.recipes])
        return (f"Nap: {self.day}\n"
                f"Receptek:\n{recipes_str if recipes_str else '[]'}")

    def add_meal(self, recipe: Recipe):
        self.recipes.append(recipe)

    def remove_meal(self, recipe: Recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)

    def get_meals(self):
        return self.recipes

def read_menu_from_file(file_path: str):
    recipes = read_recipe_from_file('jsons/recipes.json')
    menu_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = json.load(file)
    
    for i in range(len(lines)):
        id = int(lines[i]['id'])
        day = lines[i]['day']
        rs = lines[i]['recipes']
        recipes_in_menu = []
        if len(rs) > 0:
            for r in rs:
                for i in recipes:
                    if i.name == r:
                        recipes_in_menu.append(i)
        menu_item = Menu(id, day, recipes_in_menu)
        menu_list.append(menu_item)  

    return menu_list

menu_list = read_menu_from_file('jsons/menu.json')

print(*menu_list, sep="\n")