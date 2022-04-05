class Person:
    def __init__(self, id1: str, first_name: str, last_name: str):
        self.last_name = last_name
        self.first_name = first_name
        self.id = id1

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id}"


class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance


class
