# Assignment: Animal

# Create an Animal class and give it the below attributes and methods.
# Extend the Animal class to two child classes, Dog and Dragon.

class Animal:
    def __init__(self, name, health, winged):
        self.name = name
        self.health = health
        self.winged = winged

    def walk(self):
        self.health -= 1
        print(f"{self.name} Walked")
        return self

    def run(self):
        self.health -= 5
        print(f"{self.name} Ran")
        return self

    def display_health(self):
        print(f"Health: {self.health}")

print("*"*20)

animal_1 = Animal("Bear", 175, False)
animal_1.walk().walk().walk().run().run().display_health()

print("*"*20)

class Dog(Animal):
    def __init__(self, name, health, winged):
        super().__init__(name, health, winged)
        self.health = 150

    def pet(self):
        if self.__class__.__name__ == "Animal":
            print("Only a specific kind of animal can be petted")
            return self
        else:
            self.health += 5
            print(f"{self.name} was Petted")
            return self

dog_1 = Dog("Wolve", 0, False)
dog_1.walk().walk().walk().run().run()
Dog.pet(dog_1)
dog_1.display_health()

print("*"*20)

class Dragon(Animal):
    def __init__(self, name, health, winged):
        super().__init__(name, health, winged) # use super to call the Human __init__() method
        self.health = 170

    def fly(self):
        if self.winged == True:
            self.health -= 10
            print(f"{self.name} Flew")
        else:
            print(f"{self.name} isn't a winged animal")
        return self
    
    def displayFunction(self):
        Animal.display_health(self)
        if self.__class__.__name__ == "Dragon":
            print("I am a Dragon")
        else:
            pass
        return self

dragon_1 = Dragon("Myghty", 0, True)
print(dragon_1.name)
Dragon.fly(dragon_1)
Dragon.displayFunction(dragon_1)

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods,
# and its displayHealth() is not saying 'this is a dragon!'.
# Also confirm that your Dog class can not fly().

print("*"*20)

animal_2 = Animal("Fish", 75, False)
Dog.pet(animal_2) #check
Dragon.fly(animal_2) #check
Dragon.displayFunction(animal_2) #check

print("*"*20)

dog_2 = Dog("Lucky", 500, False)
Dragon.fly(dog_2)
Dog.display_health(dog_2)
