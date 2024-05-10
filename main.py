class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} is sleeping")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} is eating")
        self.power +=1

    def hit(self):
        print(f"{self.name} is hitting")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} is walking")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Endurance: {self.endurance}")
        print(f"Hair color: {self.hair_color}")

war1 = Warrior("Warrior 1", 76, 54, "black")
war2 = Warrior("Warrior 2", 56, 74, "brown")

war1.info()
war2.info()