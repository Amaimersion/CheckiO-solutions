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
        self.lancer_attack = get(4, "lancer_attack", 0)
        self.heal_power = get(5, "heal_power", 0)
        self.max_health = get(6, "max_health", self.health)
        self.is_alive = True if self.health > 0 else False

    """Getting damage."""
    def I_Get_BishBashBosh(self, damage):
        damage = 0 if self.defense >= damage else damage - self.defense

        self.health -= damage
        self.is_alive = True if self.health > 0 else False

        return damage

    """heal_power."""
    def I_Will_Live_Forever(self, attack):
        self.health += self.vampirism * attack / 100

        if (self.health > self.max_health):
            self.health = self.max_health

        return self.health

    def equip_weapon(self, weapon):
        def add(param, new_value):
            old_value = getattr(self, param)

            if old_value == 0:
                return

            setattr(self, param, old_value + new_value)

            if getattr(self, param) < 0:
                setattr(self, param, 0)

        add("health", weapon.health)
        add("max_health", weapon.max_health)
        add("attack", weapon.attack)
        add("defense", weapon.defense)
        add("vampirism", weapon.vampirism)
        add("heal_power", weapon.heal_power)
        add("lancer_attack", weapon.lancer_attack)

        self.is_alive = True if self.health > 0 else False
        
class Knight(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Knight, self).__init__(*args, **kwargs)
        super(Knight, self).__init__(health=50, max_health=50, attack=7, defense=0, vampirism=0, heal_power=0)

class Defender(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Defender, self).__init__(*args, **kwargs)
        super(Defender, self).__init__(health=60, max_health=60, attack=3, defense=2, vampirism=0, heal_power=0)

class Vampire(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Vampire, self).__init__(*args, **kwargs)
        super(Vampire, self).__init__(health=40, max_health=40, attack=4, defense=0, vampirism=50, heal_power=0)

class Lancer(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Lancer, self).__init__(*args, **kwargs)
        super(Lancer, self).__init__(health=50, max_health=50, attack=6, lancer_attack=3, defense=0, vampirism=0, heal_power=0)

class Healer(Warrior):
    def __init__(self, *args, **kwargs):
        #super(Healer, self).__init__(*args, **kwargs)
        super(Healer, self).__init__(health=60, max_health=60, attack=0, defense=0, vampirism=0, heal_power=2)

    """You Will Live Forever"""
    def heal(self, unit_for_heal):
        if not unit_for_heal.is_alive:
            return

        unit_for_heal.health += self.heal_power

        if (unit_for_heal.health > unit_for_heal.max_health):
            unit_for_heal.health = unit_for_heal.max_health

def fight(unit_1, unit_2, back_unit_1=None, back_unit_2=None):
    while (unit_1.is_alive and unit_2.is_alive):
        damage = unit_2.I_Get_BishBashBosh(unit_1.attack)
        unit_1.I_Will_Live_Forever(damage)

        if (back_unit_2 and back_unit_2.is_alive and type(unit_1) == Lancer):
            damage = back_unit_2.I_Get_BishBashBosh(unit_1.lancer_attack)
            unit_1.I_Will_Live_Forever(damage) # if the unit_1 is Vampire Lancer!

        if (back_unit_2 and back_unit_2.is_alive and type(back_unit_2) == Healer):
            back_unit_2.heal(unit_2)

        if not unit_2.is_alive: 
            return True


        damage = unit_1.I_Get_BishBashBosh(unit_2.attack)
        unit_2.I_Will_Live_Forever(damage)

        if (back_unit_1 and back_unit_1.is_alive and type(unit_2) == Lancer):
            damage = back_unit_1.I_Get_BishBashBosh(unit_2.lancer_attack)
            unit_2.I_Will_Live_Forever(damage) # if the unit_2 is Vampire Lancer!

        if (back_unit_1 and back_unit_1.is_alive and type(back_unit_1) == Healer):
            back_unit_1.heal(unit_1)

        if not unit_1.is_alive: 
            return False


"""Battle."""

class Army(object):
    def __init__(self):
        super(Army, self).__init__()
        self.horde = []
        self.is_alive = False

    def __getitem__(self, index):
        return self.horde[index]

    def __len__(self):
        return len(self.horde)

    @property
    def units(self):
        return self.horde
    
    def add_units(self, type, count):
        self.horde.extend([type() for i in range(count)])
        self.is_alive = True if self.horde else False

    """Get available unit."""
    def I_Will_Break_Yourself_Upon_My_Body(self, unit_index=0):
        return self.horde[unit_index] if (self.horde and len(self.horde) > abs(unit_index)) else None

    """Checks if the I_Will_Break_Yourself_Upon_My_Body unit is alive."""
    def We_Will_Never_Be_Slaves(self, unit_index=0):
        unit = self.I_Will_Break_Yourself_Upon_My_Body(unit_index)

        if not unit:
            return

        index = self.horde.index(unit)
        self.horde.pop(index) if not unit.is_alive else None
        self.is_alive = True if self.horde else False

    """Remove dead units."""
    def Dont_Stay_Down_On_The_Ground(self):
        self.horde = list(filter(lambda unit: unit.is_alive, self.horde))

        if not self.horde:
            self.is_alive = False

class Battle(object):
    def __init__(self):
        super(Battle, self).__init__()

    def fight(self, army_1, army_2):
        forward_index = 0
        backward_index = 1

        while (army_1.is_alive and army_2.is_alive):
            army_1_human = army_1.I_Will_Break_Yourself_Upon_My_Body(forward_index)
            army_2_orc = army_2.I_Will_Break_Yourself_Upon_My_Body(forward_index)
            army_1_back_unit = army_1.I_Will_Break_Yourself_Upon_My_Body(backward_index)
            army_2_back_unit = army_2.I_Will_Break_Yourself_Upon_My_Body(backward_index)

            winner = fight(army_1_human, army_2_orc, army_1_back_unit, army_2_back_unit)

            army_1.We_Will_Never_Be_Slaves(forward_index)
            army_2.We_Will_Never_Be_Slaves(forward_index)
            army_1.We_Will_Never_Be_Slaves(backward_index) # back units check.
            army_2.We_Will_Never_Be_Slaves(backward_index) # back units check.

            if not army_2.is_alive: return True
            if not army_1.is_alive: return False

    def straight_fight(self, army_1, army_2):
        while (army_1.is_alive and army_2.is_alive):
            for i in range(min(len(army_1), len(army_2))):
                fight(army_1[i], army_2[i])

            army_1.Dont_Stay_Down_On_The_Ground()
            army_2.Dont_Stay_Down_On_The_Ground()

            if not army_2.is_alive: return True
            if not army_1.is_alive: return False


"""Weapons."""

class Weapon(object):
    def __init__(self, *args, **kwargs):
        def get(index, key, default):
            if (args and len(args) > index): return args[index]
            if (kwargs and key in kwargs): return kwargs[key]
            return default

        self.health = get(0, "health", 0)
        self.attack = get(1, "attack", 0)
        self.defense = get(2, "defense", 0)
        self.vampirism = get(3, "vampirism", 0)
        self.heal_power = get(4, "heal_power", 0)
        self.lancer_attack = get(5, "lancer_attack", 0)
        self.max_health = get(6, "max_health", self.health)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(health=+5, attack=+2)

class Shield(Weapon):
    def __init__(self):
        super(Shield, self).__init__(health=+20, attack=-1, defense=+2)

class GreatAxe(Weapon):
    def __init__(self):
        super(GreatAxe, self).__init__(health=-15, attack=+5, defense=-2, vampirism=+10)

class Katana(Weapon):
    def __init__(self):
        super(Katana, self).__init__(health=-20, attack=+6, defense=-5, vampirism=+50)

class MagicWand(Weapon):
    def __init__(self):
        super(MagicWand, self).__init__(health=+30, attack=+3, heal_power=+3)


"""Battlefield - CheckiO"""

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing.
    
    ogre = Warrior()
    lancelot = Knight()
    richard = Defender()
    eric = Vampire()
    freelancer = Lancer()
    priest = Healer()

    sword = Sword()
    shield = Shield()
    axe = GreatAxe()
    katana = Katana()
    wand = MagicWand()
    super_weapon = Weapon(50, 10, 5, 150, 8)

    ogre.equip_weapon(sword)
    ogre.equip_weapon(shield)
    ogre.equip_weapon(super_weapon)
    lancelot.equip_weapon(super_weapon)
    richard.equip_weapon(shield)
    eric.equip_weapon(super_weapon)
    freelancer.equip_weapon(axe)
    freelancer.equip_weapon(katana)
    priest.equip_weapon(wand)
    priest.equip_weapon(shield)

    ogre.health == 125
    lancelot.attack == 17
    richard.defense == 4
    eric.vampirism == 200
    freelancer.health == 15
    priest.heal_power == 5

    fight(ogre, eric) == False
    fight(priest, richard) == False
    fight(lancelot, freelancer) == True

    my_army = Army()
    my_army.add_units(Knight, 1)
    my_army.add_units(Lancer, 1)

    enemy_army = Army()
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 1)

    my_army.units[0].equip_weapon(axe)
    my_army.units[1].equip_weapon(super_weapon)

    enemy_army.units[0].equip_weapon(katana)
    enemy_army.units[1].equip_weapon(wand)

    battle = Battle()
    battle.fight(my_army, enemy_army) == True

    print("Coding complete? Let's try tests!")
