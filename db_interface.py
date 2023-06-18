import hashlib
import json


class DatabaseModel:
    def __init__(self):
        self.data = {}
        try:
            with open("categories.json", 'r') as categories_file:
                self.store_categories = json.load(categories_file)
        except FileNotFoundError:
            self.store_categories = []

    def unmarshal(self, data):
        self.data["category"] = data["category"]
        self.data["description"] = data["description"]
        self.data["quantity"] = data["quantity"]
        self.data["link"] = data["link"]
        self.data["hash"] = self.calc_hash()

    def marshal(self):
        return self.data

    def calc_hash(self):
        return hashlib.md5(("".join(self.data["category"] + self.data["description"])).encode()).hexdigest()


class DatabaseEngine:

    def __init__(self):
        self.data = None

    def get(self):
        return self.data

    def put(self, data):
        self.data = data
