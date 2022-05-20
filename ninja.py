from pet import ein
class Ninja:
    def __init__(self,first_name,last_name,pet,pet_food,treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.pet_food = pet_food
        self.treats = treats

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        print(f"Feeding {self.pet.name} {pet_food}!")
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.bark()
        return self

pet_food = "Purina"
treats = "Biscuits","Sausages"

ichigo = Ninja("Ichigo","Kurosaki",ein,pet_food,treats)

ichigo.feed();
ichigo.walk();
ichigo.bathe();