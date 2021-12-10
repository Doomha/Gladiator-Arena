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
    def __init__(self, name, gold, potion, pl_controlled):
        self.name = name
        self.gold = Gold(gold)
        self.potion = Potion(potion)
        self.pl_controlled = pl_controlled
        self.pouch = [Gold(gold), Potion(potion)]

    def person_check(self):
        if self.pl_controlled == False:
            person = vendor
        else:
            person = player

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

    def drink_potion(self):
        if self.potion.amount >= 1:
            self.potion.amount -= 1
            print(f"{self.name} consumed a potion.")
            print(f"{self.name} has {self.potion.amount} potions left.")
        else:
            print(f"{self.name} does not have any potions right now.")
#: def trade_item_select():



player = Person("John", 50, 0, True)
vendor = Person("Ginger", 100, 3, False)
contestant1 = Person("Harry", 35, 1, False)

contestant1.ls_inventory()
contestant1.gold.amount -= 10
contestant1.drink_potion()
print(f"{contestant1.name} has {contestant1.gold.amount} left.")
