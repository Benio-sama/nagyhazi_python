import json

class ShoppingList_Item():
    def __init__(self, id, name, quantity, unit):
        self.id = id
        self.name = name
        if quantity is not None:
            self.quantity = float(quantity)
        else:
            self.quantity = None
        self.unit = unit

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'unit': self.unit
        }
    
    def add_quantity(self, item):
        if (item.quantity is not None and self.quantity is not None):
            self.quantity += item.quantity
        elif item.quantity is not None and self.quantity is None:
            self.quantity = item.quantity
            self.unit = item.unit
        else:
            pass

    def _setname(self, new_name: str):
        self.name = new_name

    def _setquantity(self, new_quantity):
        self.quantity = new_quantity

    def _setunit(self, new_unit: str):
        self.unit = new_unit

class ShoppingList:
    def __init__(self):
        self.items = []

    def __str__(self):
        for i in self.items:
            print(i)
    
    def to_dict(self):
        return [item.to_dict() for item in self.items]
    
def read_shopping_list_from_file(file_path):
    shopping_list = ShoppingList()
    if isinstance(file_path, str):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = json.load(file)
    else:
        lines = file_path

    for i in range(len(lines)):
        id = lines[i]['id']
        name = lines[i]['name']
        quantity = lines[i]['quantity']
        unit = lines[i]['unit']
        shopping_list_item = ShoppingList_Item(id, name, quantity, unit)
        shopping_list.items.append(shopping_list_item)

    return shopping_list