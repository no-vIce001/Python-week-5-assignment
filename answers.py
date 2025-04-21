# Assignment 1
# Class representing Superhero
class Superhero:
    # Constructor method  to initialize the object
    def __init__(self, name, power, weakness):
        self.name = name
        self.power = power
        self.power = weakness

heroDetails = Superhero("Flash", "Superspeed" , "Blindness")
print(heroDetails.name)

# Inheritance
class Villain(Superhero):
    pass
villain = Villain("ReverseFlash", "Superspeed", "ExtremeCold")
print(villain.name)





# Activity 2
# Polymorphism Challenge
class Horse:
    def move(self):
        return "Gallop!"

class Shark:
    def move(self):
        return "Swim!"

class Eagle:
    def move(self):
        return "Fly!"

class Snake:
    def move(self):
        return "Slither!"
    
class Hare:
    def move(self):
        return "Hop!"

for animal in [Horse(), Shark(), Eagle(), Snake(), Hare()]:
    print(animal.move())