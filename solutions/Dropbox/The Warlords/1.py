# !/usr/bin/python
# -*- coding: utf-8 -*-


from typing import Any, Type, List


"""Weapons."""

class Weapon(object):
    """The base class for all weapons.

    Arguments can be passed as either ``*args`` or ``**kwargs``, not both!

    Args:
        health (int, optional): 
            The health parameter. 
            0 for ``*args``, "health" for ``**kwargs``.
            Defaults to 0.

        attack (int, optional):
            The attack parameter.
            1 for ``*args``, "attack" for ``**kwargs``.
            Defaults to 0.

        defense (int, optional):
            The defense parameter.
            2 for ``*args``, "defense" for ``**kwargs``.
            Defaults to 0.

        vampirism (int, optional):
            The vampirism parameter in percentage.
            3 for ``*args``, "vampirism" for ``**kwargs``.
            Defaults to 0.

        lancer_attack (int, optional):
            The second attack parameter for the `Lancer` unit.
            4 for ``*args``, "lancer_attack" for ``**kwargs``.
            Defaults to 0.

        heal_power (int, optional):
            The heal power parameter for the `Healer` unit.
            5 for ``*args``, "heal_power" for ``**kwargs``.
            Defaults to 0.

        max_health (int, optional): 
            The max health parameter. 
            6 for *args, "max_health" for **kwargs.
            Defaults to self.health.

    Attributes:
        * All args above.

    Default characteristic:
        Health = +0
        Max Health = +0
        Attack = +0
        Defense = +0
        Vampirism = +0
        Lancer Attack = +0
        Heal Power = +0

    """

    def __init__(self, *args, **kwargs):
        """Creates the instance of Weapon."""

        def get(index: int, key: str, default: Any) -> Any:
            if (args and len(args) > index): return args[index]
            if (kwargs and key in kwargs): return kwargs[key]
            return default

        self.health: int = get(0, "health", 0)
        self.attack: int = get(1, "attack", 0)
        self.defense: int = get(2, "defense", 0)
        self.vampirism: int = get(3, "vampirism", 0)
        self.lancer_attack: int = get(4, "lancer_attack", 0)
        self.heal_power: int = get(5, "heal_power", 0)
        self.max_health: int = get(6, "max_health", self.health)

class Sword(Weapon):
    """A Sword weapon.
    
    Default characteristic:
        Health = +5
        Attack = +2
    
    """

    def __init__(self):
        """Creates the instance of Sword."""
        super(Sword, self).__init__(health=+5, attack=+2)

class Shield(Weapon):
    """A Shield weapon.
    
    Default characteristic:
        Health = +20
        Attack = -1
        Defense = +2
    
    """

    def __init__(self):
        """Creates the instance of Shield."""
        super(Shield, self).__init__(health=+20, attack=-1, defense=+2)

class GreatAxe(Weapon):
    """A Great Axe weapon.
    
    Default characteristic:
        Health = -15
        Attack = +5
        Defense = -2
        vampirism = +10
    
    """

    def __init__(self):
        """Creates the instance of GreatAxe."""
        super(GreatAxe, self).__init__(health=-15, attack=+5, defense=-2, vampirism=+10)

class Katana(Weapon):
    """A Katana weapon.
    
    Default characteristic:
        Health = -20
        Attack = +6
        Defense = -5
        Vampirism = +50
    
    """

    def __init__(self):
        """Creates the instance of Katana."""
        super(Katana, self).__init__(health=-20, attack=+6, defense=-5, vampirism=+50)

class MagicWand(Weapon):
    """A Magic Wand weapon.
    
    Default characteristic:
        Health = +30
        Attack = +3
        Heal Power = +3
    
    """

    def __init__(self):
        """Creates the instance of MagicWand."""
        super(MagicWand, self).__init__(health=+30, attack=+3, heal_power=+3)


"""Units."""

class Warrior(object):
    """The base class for all units.

    Arguments can be passed as either ``*args`` or ``**kwargs``, not both!

    Args:
        health (int, optional): 
            The health of an unit. 
            0 for ``*args``, "health" for ``**kwargs``.
            Defaults to 50.

        attack (int, optional):
            The attack of an unit.
            1 for ``*args``, "attack" for ``**kwargs``.
            Defaults to 5.

        defense (int, optional):
            The defense of an unit.
            Decreases each enemy attack.
            2 for ``*args``, "defense" for ``**kwargs``.
            Defaults to 0.

        max_health (int, optional): 
            The max health of an unit. 
            3 for *args, "max_health" for **kwargs.
            Defaults to self.health.

    Attributes:
        * All args above.

        is_alive (bool):
            Indicates if the unit is alive.
            Defaults to `True if self.health > 0 else False`.

    Default characteristic:
        Health = 50
        Max Health = 50
        Attack = 5
        Defense = 0

    """

    def __init__(self, *args, **kwargs):
        """Creates the instance of Warrior."""

        def get(index: int, key: str, default: Any) -> Any:
            if (args and len(args) > index): return args[index]
            if (kwargs and key in kwargs): return kwargs[key]
            return default

        self.health: int = get(0, "health", 50)  
        self.attack: int = get(1, "attack", 5)
        self.defense: int = get(2, "defense", 0)
        self.max_health: int = get(3, "max_health", self.health)
        self.is_alive: bool = True if self.health > 0 else False

    def I_Get_BishBashBosh(self, damage: int) -> int:
        """Gets a damage.

        Args:
            damage (int):
                The damage for the unit. 
                If a defense of the unit >= of the damage,
                then the damage will be set to 0.

        Returns (int):
            A damage dealt.

        """
        damage = 0 if self.defense >= damage else damage - self.defense

        self.health -= damage
        self.is_alive = True if self.health > 0 else False

        return damage

    def equip_weapon(self, weapon: Type[Weapon]) -> None:
        """Equips a weapon on the unit.

        All parameters are summed up.
        If the value doesn't exists or initially has 0, then the summarization will be ignored.
        If the value after summarization is < 0, then the value sets to 0.

        """
        def add(param: str, new_value: Any) -> None:
            if not hasattr(self, param):
                return

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

class Unit(Warrior):
    """A simple unit.
    
    Creates the unit with the given *args or **kwargs.

    Note:
        The unit is subclass of Warrior.
        See __doc__ of Warrior for more.

    """

    def __init__(self, *args, **kwargs):
        """Creates the instance of Unit."""
        super(Unit, self).__init__(*args, **kwargs)
        
class Knight(Warrior):
    """A Knight unit.

    Note:
        The unit is subclass of Warrior.
        See __doc__ of Warrior for more.

    Default characteristic:
        Health = 50
        Attack = 7

    """

    def __init__(self):
        """Creates the instance of Knight."""
        super(Knight, self).__init__(health=50, attack=7)

class Defender(Warrior):
    """A Defender unit.

    Note:
        The unit is subclass of Warrior.
        See __doc__ of Warrior for more.

    Default characteristic:
        Health = 60
        Attack = 3
        Defense = 2

    """

    def __init__(self):
        """Creates the instance of Defender."""
        super(Defender, self).__init__(health=60, attack=3, defense=2)

class Vampire(Warrior):
    """A Vampire unit.

    Note:
        The unit is subclass of Warrior.
        See __doc__ of Warrior for more.

    Args:
        vampirism (int, optional):
            The vampirism of an unit in percentage.
            For effect the unit should call `I_Will_Live_Forever` method
            after each attack, `self.vampirisim` will be used in it.
            0 for ``*args``, "vampirism" for ``**kwargs``.
            Defaults to 50.

    Attributes:
        * All args above.

    Default characteristic:
        Health = 40
        Attack = 4
        Vampirism = 50%

    """

    def __init__(self, *args, **kwargs):
        """Creates the instance of Vampire."""

        def get(index: int, key: str, default: Any) -> Any:
            if (args and len(args) > index): return args[index]
            if (kwargs and key in kwargs): return kwargs[key]
            return default
        
        super(Vampire, self).__init__(health=40, attack=4)
        self.vampirism: int = get(0, "vampirism", 50)

    def I_Will_Live_Forever(self, attack: int) -> int:
        """Healing by vampirism.

        Args:
            attack (int):
                A dealt damage for vampirism getting.

        Note:
            If self.health after vampirism is > self.max_health,
            then self.health will be setted to self.max_health.

        Returns (int):
            A current health.

        """
        self.health += self.vampirism * attack / 100

        if self.health > self.max_health:
            self.health = self.max_health

        return self.health

class Lancer(Warrior):
    """A Lancer unit.

    Note:
        The unit is subclass of Warrior.
        See __doc__ of Warrior for more.

    Args:
        lancer_attack (int, optional):
            The second attack for the `Lancer` unit.
            Will be used in second attack if the unit will be attack twice.
            0 for ``*args``, "lancer_attack" for ``**kwargs``.
            Defaults to self.attack * 0.5.

    Attributes:
        * All args above.

    Default characteristic:
        Health = 50
        Attack = 6
        Second attack = 3
    """

    def __init__(self, *args, **kwargs):
        """Creates the instance of Lancer."""

        def get(index: int, key: str, default: Any) -> Any:
            if (args and len(args) > index): return args[index]
            if (kwargs and key in kwargs): return kwargs[key]
            return default

        super(Lancer, self).__init__(health=50, attack=6)
        self.lancer_attack: int = get(0, "lancer_attack", self.attack * 0.5)

class Healer(Warrior):
    """A Healer unit.

    Note:
        The unit is subclass of Warrior.
        See __doc__ of Warrior for more.

    Args:
        heal_power (int, optional):
            The heal power for the `Healer` unit.
            For effect the unit should call `heal` method.
            0 for ``*args``, "heal_power" for ``**kwargs``.
            Defaults to 2.

    Attributes:
        * All args above.

    Default characteristic:
        Health = 60
        Attack = 0
        Heal power = 2

    """

    def __init__(self, *args, **kwargs):
        """Creates the instance of Healer."""

        def get(index: int, key: str, default: Any) -> Any:
            if (args and len(args) > index): return args[index]
            if (kwargs and key in kwargs): return kwargs[key]
            return default

        super(Healer, self).__init__(health=60, attack=0)
        self.heal_power: int = get(0, "heal_power", 2)

    def heal(self, unit_for_heal: Type[Warrior]) -> int:
        """You Will Live Forever! 

        Heals another unit.

        Args:
            unit_for_heal (Warrior):
                A unit for healing.

        Note:
            A health of the unit for heal cannot be greater than his max health.

        Returns (int):
            A health of the unit for heal after healing.

        """
        if not unit_for_heal.is_alive:
            return unit_for_heal.health

        unit_for_heal.health += self.heal_power

        if unit_for_heal.health > unit_for_heal.max_health:
            unit_for_heal.health = unit_for_heal.max_health

        return unit_for_heal.health

class Warlord(Warrior):
    """A Warlord unit.

    Note:
        The unit is subclass of Warrior.
        See __doc__ of Warrior for more.

    Default characteristic:
        Health = 100
        Attack = 4
        Defense = 2

    """

    def __init__(self):
        """Creates the instance of Warlord."""
        super(Warlord, self).__init__(health=100, attack=4, defense=2)

    def move_units(self, army):
        """Move units of the army.

        1. If there are Lancers in the army, they will be placed in front of everyone else.
        2. If there is a Healer in the army, he will be placed right after the first soldier to heal him during the fight. If the number of Healers is > 1, all of them will be placed right behind the first Healer.
        3. If there are no more Lancers in the army, but there are other soldiers who can deal damage, they also will be placed in first position, and the Healer will stay in the 2nd row (if army still has Healers).
        4. Warlord will always stay way in the back to look over the battle and rearrange the soldiers when it's needed.

        """
        army.sort(key=lambda i: type(i) not in (Lancer, Warlord, Healer), reverse=True) # 3
        army.sort(key=lambda i: type(i) == Lancer, reverse=True) # 1
        army[1:] = sorted(army[1:], key=lambda i: type(i) == Healer, reverse=True) # 2
        army.sort(key=lambda i: type(i) == Warlord) # 4


"""Duel."""

def fight(unit_1: Type[Warrior], unit_2: Type[Warrior], back_unit_1: Type[Warrior]=None, back_unit_2: Type[Warrior]=None) -> bool:
    """Duel of two units until one of them die.

    Args:
        unit_1 (Warrior):
            The first unit for fight vs second unit.

        unit_2 (Warrior):
            The second unit for fight vs first unit.

        back_unit_1 (Warrior, optional):
            The unit that stands behind the first unit.
            If back_unit_1 is Healer, then back_unit_1 will heal unit_1,
            if unit_2 is Lancer, then unit_2 will damage back_unit_1,
            etc.
            Defaults to None.

        back_unit_2 (Warrior, optional):
            The unit that stands behind the second unit.
            If back_unit_2 is Healer, then back_unit_2 will heal unit_2,
            if unit_1 is Lancer, then unit_1 will damage back_unit_2,
            etc.
            Defaults to None.

    Returns (bool):
        True if unit_1 won (unit_2 die), False if unit_2 won (unit_1 die).

    """
    while (unit_1.is_alive and unit_2.is_alive):
        # unit_1 and back_unit_1 actions.

        damage = unit_2.I_Get_BishBashBosh(unit_1.attack)

        if (type(unit_1) == Vampire):
            unit_1.I_Will_Live_Forever(damage)

        if (back_unit_2 and back_unit_2.is_alive and type(unit_1) == Lancer):
            back_unit_2.I_Get_BishBashBosh(unit_1.lancer_attack)

        if (back_unit_2 and back_unit_2.is_alive and type(back_unit_2) == Healer):
            back_unit_2.heal(unit_2)

        if not unit_2.is_alive:
            return True

        # unit_2 and back_unit_2 actions.

        damage = unit_1.I_Get_BishBashBosh(unit_2.attack)

        if (type(unit_2) == Vampire):
            unit_2.I_Will_Live_Forever(damage)

        if (back_unit_1 and back_unit_1.is_alive and type(unit_2) == Lancer):
            back_unit_1.I_Get_BishBashBosh(unit_2.lancer_attack)

        if (back_unit_1 and back_unit_1.is_alive and type(back_unit_1) == Healer):
            back_unit_1.heal(unit_1)

        if not unit_1.is_alive: 
            return False


"""Army."""

class Army(object):
    """An army that contains an units.

    Note:
        - An army can contain only 1 Warlord.
        - You should manually remove dead units by calling `We_Will_Never_Be_Slaves` or `Dont_Stay_Down_On_The_Ground`.

    Attributes:
        units (List of Warrior):
            The units in the army.

        is_alive (bool):
            Indicates if the army is alive.

        has_warlord (bool):
            Indicates if the army has the Warlord.

        warlord_instance (Warlord):
            The Warlord instance if he in the army.

    """

    def __init__(self):
        """Creates the instance of Army."""
        super(Army, self).__init__()
        self.horde: List[Type[Warrior]] = []
        self.is_alive: bool = False
        self.has_warlord: bool = False
        self.warlord_instance: Type[Warlord] = None

    def __getitem__(self, index: int) -> Type[Warrior]:
        """Returns the unit by the index."""
        return self.horde[index]

    def __len__(self) -> int:
        """Returns a len of the army."""
        return len(self.horde)

    @property
    def units(self) -> List[Type[Warrior]]:
        """A units in the army."""
        return self.horde
    
    def add_units(self, unit_type: Type[Warrior], count: int=1) -> None:
        """Adds a units in the army.

        Args:
            unit_type (Warrior):
                A type of unit that will be added in the army.

            count (int, optional):
                A number of units that will be added in the army.
                Defaults to 1.

        Note:
            An army can have only 1 Warlord.
        
        """
        if (unit_type == Warlord and not self.has_warlord):
            instance = unit_type()
            self.horde.extend([instance])
            self.has_warlord = True
            self.warlord_instance = instance
        elif (unit_type != Warlord):
            self.horde.extend([unit_type() for i in range(count)])

        self.is_alive = True if self.horde else False

    def I_Will_Break_Yourself_Upon_My_Body(self, unit_index: int=0) -> Type[Warrior]:
        """Gets available unit by the index.

        Args:
            unit_index (int, optional):
                An index of the unit.
                Defaults to 0.

        Returns (Warrior or None):
            Warrior if index in the army else None.
        
        """
        return self.horde[unit_index] if (self.horde and len(self.horde) > abs(unit_index)) else None

    def We_Will_Never_Be_Slaves(self, unit_index: int=0) -> bool:
        """Checks if the unit by the index is alive. If not, then removes it.

        Args:
            unit_index (int, optional):
                An index of the unit.
                Defaults to 0.

        Returns (bool):
            False if the unit is alive, True if the unit is not alive and was removed.

        """
        unit = self.I_Will_Break_Yourself_Upon_My_Body(unit_index)

        if ((not unit) or (unit.is_alive)):
            return False

        index = self.horde.index(unit)
        self.horde.pop(index)
        self.is_alive = True if self.horde else False

        if type(unit) == Warlord:
            self.has_warlord = False
            self.warlord_instance = None

        return True

    def Dont_Stay_Down_On_The_Ground(self) -> None:
        """Removes all dead units."""
        self.horde = list(filter(lambda unit: unit.is_alive, self.horde))

        if not self.horde:
            self.is_alive = False

        if self.warlord_instance not in self.horde:
            self.has_warlord = False
            self.warlord_instance = None

    def move_units(self):
        """Changes the order of units in the army by Warlord `move_units` method.

        Note:
            You cant use this method, if there are no Warlord.

        """
        if not (self.has_warlord and self.warlord_instance):
            return

        self.warlord_instance.move_units(self.horde)


"""Battle."""

class Battle(object):
    """A different battles between two armies."""

    def __init__(self):
        """Creates the instance of Battle."""
        super(Battle, self).__init__()

    def fight(self, army_1: Type[Army], army_2: Type[Army]) -> bool:
        """Fight of two armies until one of them die.

        Args:
            army_1 (Army):
                The first army for fight vs second army.

            army_2 (Army):
                The second army for fight vs first army.

        Returns (bool):
            True if army_1 won (army_2 die), False if army_2 won (army_1 die).

        """
        forward_index = 0 # index of the forward unit.
        backward_index = 1 # index of the backward unit.

        while (army_1.is_alive and army_2.is_alive):
            army_1_human = army_1.I_Will_Break_Yourself_Upon_My_Body(forward_index)
            army_2_orc = army_2.I_Will_Break_Yourself_Upon_My_Body(forward_index)
            army_1_back_unit = army_1.I_Will_Break_Yourself_Upon_My_Body(backward_index)
            army_2_back_unit = army_2.I_Will_Break_Yourself_Upon_My_Body(backward_index)

            winner = fight(army_1_human, army_2_orc, army_1_back_unit, army_2_back_unit)

            if (
                (
                    army_1.We_Will_Never_Be_Slaves(forward_index) or
                    army_1.We_Will_Never_Be_Slaves(backward_index)
                ) and 
                army_1.has_warlord
            ):
                army_1.move_units()

            if (
                (
                    army_2.We_Will_Never_Be_Slaves(forward_index) or
                    army_2.We_Will_Never_Be_Slaves(backward_index)
                ) and 
                army_2.has_warlord
            ):
                army_2.move_units()

            if not army_2.is_alive: return True
            if not army_1.is_alive: return False

    def straight_fight(self, army_1: Type[Army], army_2: Type[Army]) -> bool:
        """Straight fight of two armies until one of them die.

        Args:
            army_1 (Army):
                The first army for fight vs second army.

            army_2 (Army):
                The second army for fight vs first army.

        Returns (bool):
            True if army_1 won (army_2 die), False if army_2 won (army_1 die).

        See:
            https://py.checkio.org/en/mission/straight-fight/
            
        """
        while (army_1.is_alive and army_2.is_alive):
            for i in range(min(len(army_1), len(army_2))):
                fight(army_1[i], army_2[i])

            army_1.Dont_Stay_Down_On_The_Ground()
            army_2.Dont_Stay_Down_On_The_Ground()

            if not army_2.is_alive: return True
            if not army_1.is_alive: return False


"""(´・◡・｀)"""
