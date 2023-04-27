# Imagine a game where you can create a zoo and start raising different types of animals.
# Say that for each zoo you create, it can have different list of animals.
# One way you could put together this zoo is by doing the following:

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

# Note that we have a property/attribute in class Zoo called animals, which contains a list of objects from different classes.
# Just as you can store a string, a number, or even an anonymous function inside a list, you can also store objects/instances of another class into the list.  Isn't this cool?

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def addDog(self, name, health, winged):
        self.animals.append( Dog(name, health, winged) )
    def addDragon(self, name, health, winged):
        self.animals.append( Dragon(name, health, winged) )
    def printAllHealth(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            Dragon.displayFunction(animal)
    def printInfo(self):
        print(self.animals)

zoo1 = Zoo("John's Zoo")
zoo1.addDog("Tracy", 0, False)
zoo1.addDog("Doggy", 0, False)
zoo1.addDragon("Draggy", 0, False)
zoo1.addDragon("Dragoon", 0, False)
zoo1.printInfo()
zoo1.printAllHealth()