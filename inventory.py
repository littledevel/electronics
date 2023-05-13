import random
import json

MAXITEMS = 100000


class Item:

    def __init__(self):
        self.id = random.randint(0, MAXITEMS)
        self.accepted_attrs = ["id", "name", "count", "description"]

    def __str__(self):
        return json.dumps(self.__dict__, indent=2)

    def marshal(self, json_data):
        for k, v in json_data.items():
            if k in self.accepted_attrs:
                self.__dict__[k] = v

class Inventory:

    def __init__(self):
        self.inventory = {}
        self.filename = "inventory.json"
        self.items = []
        self.load_from_file()

    def marshal(self):
        self.items = [str(v) for _, v in self.inventory.items()]

    def load_from_file(self):
        with open(self.filename, "r") as json_file:
            self.inventory = json.load(json_file)

    def put(self, item: Item):
        self.inventory[item.id] = item
        self.marshal()
        with open(self.filename, "w+") as json_file:
            json.dump(self.inventory, json_file)

    def get(self, id):
        return self.inventory[id]

    def get_all(self):
        self.marshal()
        return self.items
