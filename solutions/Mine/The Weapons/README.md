In this mission you should create a new class Weapon(health, attack, defense, vampirism, heal_power) which will equip your soldiers with weapons. Every weapon's object will have the parameters that will show how the soldier's characteristics change while he uses this weapon. Assume that if the soldier doesn't have some of the characteristics (for example, defense or vampirism), but the weapon have those, these parameters don't need to be added to the soldier.

The parameters list:
health - add to the current health and the maximum health of the soldier this modificator;
attack - add to the soldier's attack this modificator;
defense - add to the soldier's defense this modificator;
vampirism - increase the soldier’s vampirism to this number (in %. So vampirism = 20 means +20%);
heal_power - increase the amount of health which the healer restore for the allied unit.

All parameters could be positive or negative, so when a negative modificator is being added to the soldier’s stats, they are decreasing, but none of them can be less than 0.

Let’s look at this example: vampire (basic parameters: health = 40, attack = 4, vampirism = 50%) equip the Weapon(20, 5, 2, -60, -1). The vampire has the health and the attack, so they will change - health will grow up to 60 (40 + 20), attack will be 9 (4 + 5). The vampire doesn’t have defense or the heal_power, so these weapon modificators will be ignored. The weapon's vampirism modificator -60% will work as well. The standard vampirism value is only 50%, so we’ll get -10%. But, as we said before, the parameters can’t be less than 0, so the vampirism after all manipulations will be just 0%.

Also you should create a few standard weapons classes, which should be the subclasses of the Weapon. Here’s their list:
Sword - health +5, attack +2
Shield - health +20, attack -1, defense +2
GreatAxe - health -15, attack +5, defense -2, vampirism +10%
Katana - health -20, attack +6, defense -5, vampirism +50%
MagicWand - health +30, attack +3, heal_power +3

And finally, you should add an equip_weapon(weapon_name) method to all of the soldiers classes. It should equip the chosen soldier with the chosen weapon.
This method also should work for the units in the army. You should hold them in the list and use it like this:
my_army.units[0].equip_weapon(Sword()) - equip the first soldier with the sword.

Notes:
While healing (both vampirism and health restored by the healer), the health can’t be greater than the maximum amount of health for this unit (with consideration of all of the weapon's modificators).
If the heal from vampirism is float (for example 3.6, 1.1, 2.945), round it down in any case. So 3.6 = 3, 1.1 = 1, 2.945 = 2.
Every soldier can be equipped with any number of weapons and get all their bonuses, but if he wears too much weapons with the negative health modificator and his health is lower or equal 0 - he is as good as dead, which is actually pretty dead in this case.

Input: The warriors, armies and weapons.
Output: The result of the battle (True or False).

Precondition: 5 types of units, 2 types of battles