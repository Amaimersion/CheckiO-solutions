"""Duel."""

class Warrior(object):
    def __init__(self, *args, **kwargs):
        def get(index, key, default):
            if (args and len(args) > index): return args[index]
            if (kwargs and key in kwargs): return kwargs[key]
            return default

        self.health = get(0, "health", 50)
        self.attack = get(1, "attack", 5)
        self.defense = get(2, "defense", 0)
        self.vampirism = get(3, "vampirism", 0)
        self.is_alive = True if self.health > 0 else False

    """Getting damage."""
    def I_Get_BishBashBosh(self, damage):
        damage = 0 if self.defense >= damage else damage - self.defense

        self.health -= damage
        self.is_alive = True if self.health > 0 else False

        return damage

    """Healing."""
    def I_Will_Live_Forever(self, attack):
        self.health += self.vampirism * attack / 100
        return self.health
        
class Knight(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Knight, self).__init__(*args, **kwargs)
        super(Knight, self).__init__(health=50, attack=7, defense=0, vampirism=0)

class Defender(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Defender, self).__init__(*args, **kwargs)
        super(Defender, self).__init__(health=60, attack=3, defense=2, vampirism=0)

class Vampire(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Vampire, self).__init__(*args, **kwargs)
        super(Vampire, self).__init__(health=40, attack=4, defense=0, vampirism=50)

class Lancer(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Lancer, self).__init__(*args, **kwargs)
        super(Lancer, self).__init__(health=50, attack=6, defense=0, vampirism=0)

def fight(unit_1, unit_2, back_unit_1=None, back_unit_2=None):
    while (unit_1.is_alive and unit_2.is_alive):
        damage = unit_2.I_Get_BishBashBosh(unit_1.attack)
        unit_1.I_Will_Live_Forever(damage)
        damage = back_unit_2.I_Get_BishBashBosh(unit_1.attack * 0.5) if back_unit_2 else 0 # if the unit_1 is Lancer.
        unit_1.I_Will_Live_Forever(damage) # if the unit_1 is Vampire Lancer!
        if not unit_2.is_alive: return True

        damage = unit_1.I_Get_BishBashBosh(unit_2.attack)
        unit_2.I_Will_Live_Forever(damage)
        damage = back_unit_1.I_Get_BishBashBosh(unit_2.attack * 0.5) if back_unit_1 else 0 # if the unit_2 is Lancer.
        unit_2.I_Will_Live_Forever(damage) # if the unit_2 is Vampire Lancer!
        if not unit_1.is_alive: return False


"""Battle."""

class Army(object):
    def __init__(self):
        super(Army, self).__init__()
        self.horde = []
        self.is_alive = False

    def __getitem__(self, index):
        return self.horde[index]

    def add_units(self, type, count):
        self.horde += [type() for i in range(count)]
        self.is_alive = True if self.horde else False

    """Get available unit."""
    def I_Will_Break_Yourself_Upon_My_Body(self, unit_index=-1):
        return self.horde[unit_index] if (self.horde and len(self.horde) >= abs(unit_index)) else None

    """Checks if the I_Will_Break_Yourself_Upon_My_Body unit is alive."""
    def We_Will_Never_Be_Slaves(self, unit_index=-1):
        unit = self.I_Will_Break_Yourself_Upon_My_Body(unit_index)

        if not unit:
            return

        index = self.horde.index(unit)
        self.horde.pop(index) if not unit.is_alive else None
        self.is_alive = True if self.horde else False

class Battle(object):
    def __init__(self):
        super(Battle, self).__init__()

    def fight(self, army_1, army_2):
        while (army_1.is_alive and army_2.is_alive):
            army_1_human = army_1.I_Will_Break_Yourself_Upon_My_Body(-1)
            army_2_orc = army_2.I_Will_Break_Yourself_Upon_My_Body(-1)
            army_1_back_unit = army_1.I_Will_Break_Yourself_Upon_My_Body(-2) if type(army_2_orc) == Lancer else None
            army_2_back_unit = army_2.I_Will_Break_Yourself_Upon_My_Body(-2) if type(army_1_human) == Lancer else None

            winner = fight(army_1_human, army_2_orc, army_1_back_unit, army_2_back_unit)

            army_1.We_Will_Never_Be_Slaves(-1)
            army_2.We_Will_Never_Be_Slaves(-1)
            army_1.We_Will_Never_Be_Slaves(-2) # back units check.
            army_2.We_Will_Never_Be_Slaves(-2) # back units check.

            if not army_2.is_alive: return True
            if not army_1.is_alive: return False


"""Battlefield - CheckiO"""

if __name__ == '__main__':
    # fight tests.
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests.
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False

    print("Coding complete? Let's try tests!")
