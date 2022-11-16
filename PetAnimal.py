class Mammal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mammal_name(self):
        print(f"Name of pet: {self.name}")

    def mammal_age(self):
        print(f"Age of pet: {self.age}")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass



