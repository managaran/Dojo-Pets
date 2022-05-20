import ninja
class Pet:
    def __init__(self,name,type,tricks,noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    
    def play(self):
        self.health += 5
        print(f"Ein loves to go walking!")
        return self
    
    def bark(self):
        print(self.noise)

ein = Pet("Ein","Corgi","Answering the phone","Woof")
