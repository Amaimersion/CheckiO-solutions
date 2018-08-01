class Unit(object):
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack
        self.is_alive = True if health > 0 else False

    """Attack."""
    def BishBashBosh(self, damage):
        self.health -= damage
        self.is_alive = True if self.health > 0 else False

class Warrior(Unit):
    def __init__(self, *args, **kwargs):
        #super(Warrior, self).__init__(*args, **kwargs)
        super(Warrior, self).__init__(50, 5)

class Knight(Unit):
    def __init__(self, *args, **kwargs):
        #super(Knight, self).__init__(*args, **kwargs)
        super(Knight, self).__init__(50, 7)

def fight(unit_1, unit_2):
    while (unit_1.is_alive and unit_2.is_alive):
        unit_2.BishBashBosh(unit_1.attack)
        if not unit_2.is_alive: return True

        unit_1.BishBashBosh(unit_2.attack)
        if not unit_1.is_alive: return False

if __name__ == '__main__':
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
