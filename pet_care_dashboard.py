class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = 50  # private: stored as _Pet__health
        self.set_health(health)

    def get_health(self):
        return self.__health

    def set_health(self, value):
        ok = type(value) is int and 0 <= value <= 100
        if ok:
            self.__health = value
        else:
            print(f"{self.name}: health must be a whole number from 0 to 100, not {value!r}.")

    def show_info(self):
        print(f"{self.name}: health {self.get_health()}")

    def care_action(self):
        print(f"{self.name} needs general care.")


class Dog(Pet):
    def care_action(self):
        print(f"{self.name} needs a walk and playtime.")


class Cat(Pet):
    def care_action(self):
        print(f"{self.name} needs brushing and a quiet nap.")


class Rabbit(Pet):
    def care_action(self):
        print(f"{self.name} needs hay and a clean hutch.")


pets = [
    Dog("Buddy", 85),
    Cat("Misty", 75),
    Rabbit("Snowy", 120),
]

for pet in pets:
    pet.show_info()
    pet.care_action()

pets[0].set_health(90)
pets[1].set_health("high")
print("Buddy now has health", pets[0].get_health())