A new unit type won’t be added in this mission, but instead we’ll add a new tactic - straight_fight(army_1, army_2). It should be the method of the Battle class and it should work as follows:
at the beginning there will be a few duels between each pair of soldiers from both armies (the first unit against the first, the second against the second and so on). After that all dead soldiers will be removed and the process repeats until all soldiers of one of the armies will be dead. Armies might not have the same number of soldiers. If a warrior doesn’t have an opponent from the enemy army - we’ll automatically assume that he’s won a duel (for example - 9th and 10th units from the first army, if the second has only 8 soldiers).

Input: The warriors and armies.
Output: The result of the battle (True or False).

Precondition: 5 types of units, 2 types of battles