class Item():
    def __init__(self, name, value, amount, health_incr, strength_incr, defense_incr, speed_incr):
        self.name = name
        self.value = value
        self.amount = amount
        self.health_incr = health_incr
        self.strength_incr = strength_incr
        self.defense_incr = defense_incr
        self.speed_incr = speed_incr

#:Non-weapon items
class Gold(Item):
    def __init__(self, amount):
        super().__init__("gold", 1, amount, 0, 0, 0, 0)

class StrengthPotion(Item):
    def __init__(self, amount):
        super().__init__("strength potions", 10, amount, 0, 3, 0, 0)

class DefensePotion(Item):
    def __init__(self, amount):
        super().__init__("defense potions", 10, amount, 0, 0, 6, 0)

class SpeedPotion(Item):
    def __init__(self, amount):
        super().__init__("speed potions", 10, amount, 0, 0, 0, 3)

class Sweetcakes(Item):
    def __init__(self, amount):
        super().__init__("sweetcakes", 5, amount, 2, 0, 0, 0)

#: Weapons
class Weapon(Item):
    def __init__(self, name, value, w_type, speed, damage):
        super().__init__(name, value, 1, 0, 0, 0, 0)
        self.w_type = w_type
        self.speed = speed
        self.damage = damage

#: Ranged weapons
class Ranged_weapon(Weapon):
    def __init__(self, name, value, speed, damage):
        super().__init__(name, value, "ranged", speed, damage)

class Bow(Ranged_weapon):
    def __init__(self):
        super().__init__("Bow", 6, 5, 5)

#: Melee weapons
class Melee_weapon(Weapon):
    def __init__(self, name, value, speed, damage):
        super().__init__(name, value, "melee", speed, damage)

class Sword(Melee_weapon):
    def __init__(self):
        super().__init__("Sword", 7, 5, 7)

class Spear(Melee_weapon):
    def __init__(self):
        super().__init__("Spear", 5, 4, 4)

class Warhammer(Melee_weapon):
    def __init__(self):
        super().__init__("Warhammer", 6, 2, 8)

class Fist(Melee_weapon):
    def __init__(self):
        super().__init__("Bare fist", 0, 4, 0)


#: Armor items
class Armor(Item):
    def __init__(self, name, value, defense, weight):
        super().__init__(name, value, 1, 0, 0, 0, 0)
        self.defense = defense
        self.weight = weight

class Chainmail(Armor):
    def __init__(self):
        super().__init__("Chainmail", , 4, 4)

class Platemail(Armor):
    def __init__(self):
        super().__init__("Platemail", 8, 10, 6)

class StuddedLeather(Armor):
    def __init__(self):
        super().__init__("Studded Leather", 3, 4, 2)

class Tunic(Armor):
    def __init__(self):
        super().__init__("Tunic", 0, 0, 1)
