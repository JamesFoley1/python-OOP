class Animal():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayHealth(self):
        print(self.name+"'s health is:", self.health)
        return self

# animal1 = Animal("Dog", 20)
# animal1.walk().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health = 150):
        super().__init__(name, health)
        
    def pet(self):
        self.health += 5
        return self
    
dog1 = Dog("Spot")
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super().__init__(name, health)

    def fly(self):
        self.health -= 10

    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")
    
dragon1 = Dragon("Shyvanna")
dragon1.displayHealth()