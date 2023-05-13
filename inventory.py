import json


class StoreItem:

    def __init__(self):
        self.data = {}

    def marshal(self, json_data):
        self.data = json_data
        return self.data

    def __str__(self):
        return self.data


class Store:

    def __init__(self):
        self.store_items = {}
        self.filename = "store.json"
        self.json_file = None
        self.load_from_file()

    def store_to_file(self):
        try:
            with open(self.filename,'w+') as self.json_file:
                json.dump(self.store_items, self.json_file)
        except Exception as e:
            print(e)

    def load_from_file(self):
        try:
            with open(self.filename,'r') as self.json_file:
                self.store_items = json.load(self.json_file)
        except Exception as e:
            print(e)

    def add(self, item):
        self.store_items[item["name"]] = item
        self.store_to_file()


    def get(self):
        return self.store_items