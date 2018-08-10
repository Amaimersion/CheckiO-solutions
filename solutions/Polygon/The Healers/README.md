The battle continues and each army is losing good warriors. Let's try to fix that and add a new unit type - the Healer.
Healer won't be fighting (his attack = 0, so he can't deal the damage). But his role is also very important - every time the allied soldier hits the enemy, the Healer will heal the allie, standing right in front of him by +2 health points with the heal() method. Note that the health after healing can't be greater than the maximum health of the unit. For example, if the Healer heals the Warrior with 49 health points, the Warrior will have 50 hp, because this is the maximum for him.
The basic parameters of the Healer:
health = 60
attack = 0

Input: The warriors and armies.
Output: The result of the battle (True or False).

Precondition: 6 types of units