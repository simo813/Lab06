class Retailer:
    def __init__(self, code, name, type, country):
        self.code = code
        self.name = name
        self.type = type
        self.country = country

    def __str__(self):
        return str(self.name)


