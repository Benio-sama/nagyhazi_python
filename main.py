from console import console_main
from recipes import read_recipe_from_file
from menu import read_menu_from_file
from pantry import read_pantry_from_file

def main():
    recipes = read_recipe_from_file('jsons/recipes.json')
    menus = read_menu_from_file('jsons/menu.json')
    pantry = read_pantry_from_file('jsons/pantry.json')
    console_main(recipes, menus, pantry)

main()