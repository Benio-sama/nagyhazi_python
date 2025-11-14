import json

class Ingredient:
    def __init__(self, id, name: str, quantity: float, unit: str):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def _conversion(self, new_unit: str) -> float:
        conversions = {
            ('g', 'kg'): 0.001,
            ('dkg', 'g'): 10,
            ('g', 'dkg'): 0.1,
            ('kg', 'g'): 1000,
            ('kg', 'dkg'): 100,
            ('dkg', 'kg'): 0.01,
            ('ml', 'l'): 0.001,
            ('ml', 'dl'): 0.1,
            ('dl', 'ml'): 10,
            ('l', 'dl'): 10,
            ('dl', 'l'): 0.1,
            ('l', 'ml'): 1000,
            ('db', 'db'): 1,
            ('tk', 'ml'): 5,
            ('ek', 'ml'): 15,
            ('cup', 'ml'): 240,
            ('ml', 'tk'): 0.2,
            ('ml', 'ek'): 1/15,
            ('ml', 'cup'): 1/240,
            ('l', 'cup'): 4.167,
            ('cup', 'l'): 0.24,
        }
        key = (self.unit, new_unit)
        if key in conversions:
            return self.quantity * conversions[key]
        else:
            raise ValueError(f"Átváltás {self.unit}-ból/ből {new_unit}-ba/be nem támogatott.")
        
    def _setname(self, new_name: str):
        self.name = new_name
        
    def _setquantity(self, new_quantity: float):
        self.quantity = new_quantity

    def _setunit(self, new_unit: str):
        self.unit = new_unit

class Recipe:
    def __init__(self, id: int, name: str, category: str, servings: int, ingredients: list[Ingredient], instructions: str):
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
        return (f"\nRecipe({self.id}): {self.name}\n"
                f"Category: {self.category}\n"
                f"Servings: {self.servings}\n"
                f"Ingredients:\n{ingredients_str}\n"
                f"Instructions:\n{self.instructions}\n")
    
    def _setname(self, new_name):
        self.name = new_name
    
    def _setcategory(self, new_category):
        self.category = new_category

    def scale_recipe(self, new_servings):
        factor = new_servings / self.servings
        for ingredient in self.ingredients:
            ingredient.quantity *= factor
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
            ingredients.append(Ingredient(ing['name'], ing['quantity'], ing['unit']))

        instructions = lines[i]['instructions']
        recipe = Recipe(id, name, category, servings, ingredients, instructions)
        recipe_list.append(recipe)
    return recipe_list

read_recipe_from_file('jsons/recipes.json')
