import json
import os
import sys
from db_interface import DatabaseEngine,DatabaseModel

class JSON_Store(DatabaseEngine):
    def __init__(self):
        super().__init__()
        self.storage = {}
        self.filename = "store.json"
        self.json_file = None
        if not os.path.isfile(self.filename):
            with open(self.filename, "w+") as self.json_file:
                self.json_file.write("{}")
        self.load_from_file()

    def store_to_file(self):
        try:
            with open(self.filename, 'w+') as self.json_file:
                json.dump(self.storage, self.json_file)
        except Exception as e:
            print(e)

    def load_from_file(self):
        try:
            with open(self.filename, 'r+') as self.json_file:
                self.storage = json.load(self.json_file)
        except Exception as e:
            print(f"Error opening file: {e}")
            sys.exit(os.EX_IOERR)

    def put(self, data):
        store_item = DatabaseModel()
        store_item.unmarshal(data)
        self.storage[store_item.data["hash"]] = store_item.marshal()
        self.store_to_file()

    def get(self):
        return self.storage
