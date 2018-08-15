In this mission you should add a new class Warlord(), which should be the subclass of the Warrior class and have the next characteristics:
health = 100
attack = 4
defense = 2

Also, when the Warlord is included in any of the armies, that particular army gets the new move_units() method which allows to rearrange the units of that army for the better battle result. The rearrangement is done not only before the battle, but during the battle too, each time the allied units die. The rules for the rearrangement are as follow:
If there are Lancers in the army, they should be placed in front of everyone else.
If there is a Healer in the army, he should be placed right after the first soldier to heal him during the fight. If the number of Healers is > 1, all of them should be placed right behind the first Healer.
If there are no more Lancers in the army, but there are other soldiers who can deal damage, they also should be placed in first position, and the Healer should stay in the 2nd row (if army still has Healers).
Warlord should always stay way in the back to look over the battle and rearrange the soldiers when it's needed.
Every army can have no more than 1 Warlord.
If the army doesn’t have a Warlord, it can’t use the move_units() method.

Input: The warriors, armies and weapons.
Output: The result of the battle (True or False).

Precondition: 6 types of units, 2 types of battles