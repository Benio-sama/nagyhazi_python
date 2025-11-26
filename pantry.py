import json

class Pantry:
    def __init__(self, id, name, quantity, unit):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def add_quantity(self, amount):
        self.quantity += amount

    def remove_quantity(self, amount):
        if amount > self.quantity:
            print("Nincs elég mennyiség a kamrában.")
        else:
            self.quantity -= amount
    
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

def read_pantry_from_file(file_path: str):
    pantry_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = json.load(file)

    for i in range(len(lines)):
        id = lines[i]['id']
        name = lines[i]['name']
        quantity = float(lines[i]['quantity'])
        unit = lines[i]['unit']
        pantry_item = Pantry(id, name, quantity, unit)
        pantry_list.append(pantry_item)

    return pantry_list
