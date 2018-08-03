"""Duel."""

class Warrior(object):
    def __init__(self, health=50, attack=5, defense=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.is_alive = True if health > 0 else False

    """Getting damage."""
    def BishBashBosh(self, damage):
        self.health -= 0 if self.defense >= damage else damage - self.defense
        self.is_alive = True if self.health > 0 else False
        
class Knight(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Knight, self).__init__(*args, **kwargs)
        super(Knight, self).__init__(50, 7, 0)

class Defender(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Defender, self).__init__(*args, **kwargs)
        super(Defender, self).__init__(60, 3, 2)

def fight(unit_1, unit_2):
    while (unit_1.is_alive and unit_2.is_alive):
        unit_2.BishBashBosh(unit_1.attack)
        if not unit_2.is_alive: return True

        unit_1.BishBashBosh(unit_2.attack)
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

    """Getting damage."""
    def WeWillNeverBeSlaves(self, damage):
        unit = self.BreakYourselfUponMyBody()
        index = self.horde.index(unit)

        unit.BishBashBosh(damage)
        self.horde.pop(index) if not unit.is_alive else None
        self.is_alive = True if self.horde else False

    """Get available unit."""
    def BreakYourselfUponMyBody(self):
        return self.horde[-1] if self.horde else None

class Battle(object):
    def __init__(self):
        super(Battle, self).__init__()

    def fight(self, army_1, army_2):
        while (army_1.is_alive and army_2.is_alive):
            army_1_human = army_1.BreakYourselfUponMyBody()
            army_2_orc = army_2.BreakYourselfUponMyBody()

            army_2.WeWillNeverBeSlaves(army_1_human.attack)
            if not army_2_orc.is_alive and army_2.is_alive: continue
            if not army_2.is_alive: return True

            army_1.WeWillNeverBeSlaves(army_2_orc.attack)
            if not army_1_human.is_alive and army_1.is_alive: continue
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

    # battle tests.
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
