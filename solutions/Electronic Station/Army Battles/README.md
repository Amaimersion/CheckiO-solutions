In the previous mission - Warriors - you've learned how to make a duels between 2 warriors happen. Great job! But let's move to something that feels a little more epic - the armies! In this mission your task is to add new classes and functions to the existing ones. The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army. Also you need to create a Battle() class with a fight() function, which will determine the strongest army.

The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army. As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the battle() function should return True, if the first army won, or False, if the second one was stronger.

Input: The warriors and armies.
Output: Theresult of the battle (True or False).

Precondition: 2 types of units