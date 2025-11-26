import json
import math

from functions import is_less_point_five

class Ingredient:
    def __init__(self, id, name: str, quantity: float | None, unit: str):
        self.id = id
        self.name = name
        if unit == 'ízlés szerint':
            self.quantity = None
        else:
            self.quantity = quantity
        self.unit = unit

    def __str__(self):
        if self.quantity is None:
            return f"{self.name}: {self.unit}"
        return f"{self.name}: {self.quantity} {self.unit}"
        
    def _setname(self, new_name: str):
        self.name = new_name
        
    def _setquantity(self, new_quantity: float):
        self.quantity = new_quantity

    def _setunit(self, new_unit: str):
        self.unit = new_unit

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit
        }

class Recipe:
    def __init__(self, id: int, name: str, category: str, servings: int | float, ingredients: list[Ingredient], instructions: list[str]):
        self.id = id
        self.name = name
        self.category = category
        self.servings = servings
        self.ingredients = ingredients
        self.instructions = instructions
    
    def __str__(self):
        return (f"Recept: {self.name}, {self.servings} fő")
    
    def _allinfo(self):
        ingredients_str = "\n\t".join([str(ing) for ing in self.ingredients])
        return (f"\nRecept({self.id}): {self.name}\n"
                f"Kategória: {self.category}\n"
                f"Adagok: {self.servings}\n"
                f"Hozzávalók:\n\t{ingredients_str}\n"
                f"Elkészítési utasítások:\n{'\n'.join(self.instructions)}\n")
    
    def _setname(self, new_name):
        self.name = new_name
    
    def _setcategory(self, new_category):
        self.category = new_category

    def _setinstructions(self, new_instructions):
        self.instructions = new_instructions

    def scale_recipe(self, new_servings):
        factor = new_servings / self.servings
        if new_servings != self.servings:
            for ingredient in self.ingredients:
                if ingredient.quantity is not None and ingredient.unit != 'db' and ingredient.unit != 'fej' and ingredient.unit != 'szem' and ingredient.unit != 'gerezd':
                    if self.servings < new_servings:
                        ingredient.quantity = math.floor(float(ingredient.quantity) * factor) if is_less_point_five(float(ingredient.quantity) * factor) else math.ceil(float(ingredient.quantity) * factor)
                    else:
                        ingredient.quantity = math.ceil(float(ingredient.quantity) * factor)
                elif ingredient.unit == 'db' or ingredient.unit == 'fej' or ingredient.unit == 'szem' or ingredient.unit == 'gerezd':
                    ingredient.quantity = math.ceil(float(ingredient.quantity) * factor)
            self.servings = new_servings

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, id: int):
        self.ingredients = [ing for ing in self.ingredients if ing.id != id]

    def edit_ingredient(self, ingredient_name: str, new_quantity: float, new_unit: str):
        for ing in self.ingredients:
            if ing.name == ingredient_name:
                ing.quantity = new_quantity
                ing.unit = new_unit
                return

    def get_ingredients(self):
            return [ing.name for ing in self.ingredients]
    
    def get_instructions(self):
        return self.instructions
    
    def add_instruction(self, instruction: str):
        self.instructions.append(instruction)

    def remove_instruction(self, index: int):
        if 0 <= index < len(self.instructions):
            self.instructions.pop(index)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'servings': self.servings,
            'ingredients': [ing.to_dict() for ing in self.ingredients],
            'instructions': self.instructions
        }
    

def read_recipe_from_file(file_path: str):
    recipe_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = json.load(file)

    for i in range(len(lines)):
        id = int(lines[i]['id'])
        name = lines[i]['name']
        category = lines[i]['category']
        servings = int(lines[i]['servings'])

        ingredients = []
        for ing in lines[i]['ingredients']:
            ingredients.append(Ingredient(ing['id'], ing['name'], ing['quantity'], ing['unit']))
        
        instructions = []
        for instr in lines[i]['instructions']:
            instructions.append(instr)
        recipe = Recipe(id, name, category, servings, ingredients, instructions)
        recipe_list.append(recipe)
    return recipe_list

read_recipe_from_file('jsons/recipes.json')
