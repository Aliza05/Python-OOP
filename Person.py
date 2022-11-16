import PetAnimal


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def talk(self):
        print(f"Hi, I am {self.name}\nFollowing are my details: ")
        print(f"Age: {self.age}\nCity: {self.city}")
        dog = PetAnimal.Dog("Susy", "2 Years")
        dog.mammal_name()
        dog.mammal_age()


person = Person("Aliza", "22", "Hyderabad")
person.talk()
