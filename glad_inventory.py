from sys import exit

class Item():
    def __init__(self, name, value, tradable, limit, amount):
        self.name = name
        self.value = value
        self.tradable = tradable
        self.limit = limit
        self.amount = amount

class Gold(Item):
    def __init__(self, amount):
        super().__init__("gold", 1, True, 100, amount)

class Potion(Item):
    def __init__(self, amount):
        super().__init__("potions", 5, True, 5, amount)

class Person():
    def __init__(self, name, gold, potion, gender, pl_controlled):
        self.name = name
        self.gold = Gold(gold)
        self.potion = Potion(potion)
        self.gender = gender
        self.pl_controlled = pl_controlled
        self.pouch = [Gold(gold), Potion(potion)]

    def person_check(self):
        if self.pl_controlled == False:
            person = vendor
            print(person.name)
        else:
            person = player
            print(person.name)

    def ls_inventory(self):
        a = 0
        if self.pl_controlled == False: #: Should be person_check()
            person = vendor
        else:
            person = player

        for items in person.pouch:
            if person.pouch[a].amount == 0:
                pass
            else:
                print(f"{person.pouch[a].name}: {person.pouch[a].amount}")
            a += 1


player = Person("John", 50, 0, "male", True)
player.ls_inventory()
print(len(player.pouch))
player.person_check()

vendor = Person("Ginger", 100, 5, "female", False)
vendor.ls_inventory()
print(type(vendor.pouch))
