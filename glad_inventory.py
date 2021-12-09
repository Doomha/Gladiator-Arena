#: Keep track of all items in inventory (Contestants have them,
#: so that means that it would be a sub element of a Contestant)
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

starting_gold = 50

gold1 = Gold(starting_gold)
gold2 = Gold(35)
potion1 = Potion(0)

pouch = [gold1, potion1]

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.pouch = pouch

    def inventory_ls(self):
        a = 0
        for items in pouch:
            if pouch[a].amount == 0:
                pass
            else:
                print(pouch[a].name)
            a += 1



person1 = Person("John", 32, "male")
person1.inventory_ls()

#: print(f"First item is: {items_ls[0].name}. Their value is: {items_ls[0].value}.")

print(f"{potion1.name}'s cost {potion1.value} each.")
print(f"You can buy up to {potion1.limit} of them. Would you like to buy one?")
potion_buy = input("> ")
if potion_buy == "yes":
    gold1.amount -= int(potion1.value)
    gold2.amount += int(potion1.value)
    print(items_ls[0].amount, gold2.amount)
    potion1.amount += 1
    print(potion1.amount)



"""
pouch = Inventory(10, 1, 3)
print(f"This person has {pouch.gold} gold coins.")

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.pouch = pouch

adventurer = Person("John Smith", 32, "male")
print(f"The adventurer's name is {adventurer.name}, and they have {pouch.gold} gold coins.")

def hide_contents():
    for item in pouch:
        if pouch(item) != 0:
            print()
"""
"""class Inventory():
    def __init__(self, gold, javelins, healing_potions):
        self.gold = gold
        self.javelins = javelins
        self.healing_potions = healing_potions"""
