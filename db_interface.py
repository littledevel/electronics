import hashlib


class DatabaseModel:
    def __init__(self):
        self.data = {}
        self.store_categories = [
            "LED",
            "CAPACITOR",
            "RESISTOR",
            "SWITCH",
            "MICRO",
            "GATE",
            "DIODE",
            "MOTOR",
            "DRIVER",
            "TRANSISTOR",
            "POTENSIOMETER",
            "MULTIPLEXER",
            "PHOTOSENSOR",
            "BOARD",
            "AUDIOSENSOR",
            "MATRIX",
            "LCD",
            "BLUETOOTH",
            "RF",
            "SENSOR",
            "STEPPER",
            "TRIMMER",
        ]

    def unmarshal(self, data):
        self.data["category"] = data["category"]
        self.data["description"] = data["description"]
        self.data["quantity"] = data["quantity"]
        self.data["hash"] = self.calc_hash()


    def marshal(self):
        return self.data
    def calc_hash(self):
        hash = hashlib.md5(("".join(self.data["category"] + self.data["description"])).encode()).hexdigest()
        return hash


class DatabaseEngine:

    def __init__(self):
        pass

    def get(self):
        return self.data

    def put(self, data):
        self.data = data
