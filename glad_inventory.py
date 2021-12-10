from sys import exit
import glad_items as items

class Person():
    def __init__(self, name, gold, potion, ale, pl_controlled):
        self.name = name
        self.gold = items.Gold(gold)
        self.potion = items.Potion(potion)
        self.ale = items.Ale(ale)
        self.pl_controlled = pl_controlled
        self.pouch = [self.gold, self.potion, self.ale]

    def person_check(self):
        if self.pl_controlled == False:
            pass
        else:
            pass

    def ls_inventory(self):
        a = 0
        print(f"\n{self.name}'s inventory:")
        print("-" * 10)
        for items in self.pouch:
            if self.pouch[a].amount == 0:
                pass
            else:
                print(f"{self.pouch[a].name}: {self.pouch[a].amount}")
            a += 1
        print("-" * 10, "\n")

    def drink_potion(self):
        if self.potion.amount >= 1:
            self.potion.amount -= 1
            print(f"{self.name} consumed a potion.")
            print(f"{self.name} has {self.potion.amount} potions left.")
        else:
            print(f"{self.name} does not have any potions right now.")


player = Person("John", 50, 0, 1, True)
vendor = Person("Ginger", 100, 3, 1, False)
contestant1 = Person("Harry", 35, 1, 1, False)

contestant1.ls_inventory()
contestant1.gold.amount -= 10
contestant1.drink_potion()
print(f"{contestant1.name} has {contestant1.gold.amount} left.")
