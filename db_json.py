import json
import os
import sys
from db_interface import DatabaseEngine


class StoreItem:

    def __init__(self):
        self.data = {}

    def marshal(self, json_data: dict):
        self.data = json_data
        return self.data

    def set_data(self, data: dict):
        self.data = data
        return self.data

    def __str__(self):
        return self.data


class Store(DatabaseEngine):
    def __init__(self):
        super().__init__()
        self.store_items = {}
        self.filename = "store.json"
        self.json_file = None
        if not os.path.isfile(self.filename):
            with open(self.filename, "w+") as self.json_file:
                self.json_file.write("{}")
        self.load_from_file()

    def store_to_file(self):
        try:
            with open(self.filename, 'w+') as self.json_file:
                json.dump(self.store_items, self.json_file)
        except Exception as e:
            print(e)

    def load_from_file(self):
        try:
            with open(self.filename, 'r+') as self.json_file:
                self.store_items = json.load(self.json_file)
        except Exception as e:
            print(f"Error opening file: {e}")
            sys.exit(os.EX_IOERR)

    def put(self, data):
        store_item = StoreItem().set_data(data)
        self.store_items[store_item["name"]] = store_item
        self.store_to_file()

    def get(self):
        return self.store_items
