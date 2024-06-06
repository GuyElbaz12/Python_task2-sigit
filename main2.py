class Animal:
    zoo_name = "Hayaton"  # Class variable to store the zoo name

    def __init__(self, name_, hunger_=0):
        """
        Initializes an animal with a name and hunger level.
         name_: The name of the animal
        hunger_: The hunger level of the animal (default is 0)
        """
        self.name_ = name_  # Instance variable to store the name
        self.hunger_ = hunger_  # Instance variable to store the hunger level

    def get_name(self):
        """
        Returns the name of the animal.
        :return: The name of the animal
        """
        return self.name_

    def is_hungry(self):
        """
        Checks if the animal is hungry.
        :return: True if the animal is hungry, False if other
        """
        return self.hunger_ > 0

    def feed(self):
        """
        Reduces the hunger level of the animal by 1.
        """
        if self.is_hungry():
            self.hunger_ -= 1

    def talk(self):
        """
        Abstract method to be implemented by subclasses.
        """
        pass  # Implement in subclasses
class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    _color = "Green"  # Additional attribute specific to Dragon

    def __init__(self, name_, hunger_=0):
        """
        Initializes a Dragon with a name and hunger level.
        Inherits from Animal.
        name_: The name of the dragon
        : The hunger level of the dragon (default is 0)
        """
        super().__init__(name_, hunger_)
        self.color_ = Dragon._color  # Initializes color attribute with default value

    def talk(self):
        print("Raaaawr")

    def breathe_fire(self):
        print("$@#$#@$")
def main():
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
    ]

    # Feed hungry animals and make them talk
    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()
        print(animal.get_name())
        animal.talk()

    # Perform unique actions for each animal type
    for animal in zoo_lst:
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breathe_fire()

    # Add new animals to the zoo
    new_animals = [
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80),
    ]

    zoo_lst.extend(new_animals)

    # Feed and make new animals talk
    for animal in new_animals:
        while animal.is_hungry():
            animal.feed()
        print(animal.get_name())
        animal.talk()

    for animal in new_animals:
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breathe_fire()

    print(f"{Animal.zoo_name}")  # Print the name of the zoo


if __name__ == "__main__":
    main()
