import random

'''
REMINDER:
In addition to completing the Warrior and Mage classes, you need to create two more classes that inherit from Character, such as:
- Archer
- Paladin

Each character must have two unique abilities, such as:
- Archer: "Quick Shot" (double arrow attack) and "Evade" (avoid next attack).
- Paladin: "Holy Strike" (bonus damage) and "Divine Shield" (blocks the next attack).

Your custom classes don't have to be Archer & Paladin nor do they have to have those specific abilities.
You just have to create two of your own. You have creative freedom here.
They can be whatever classes you want with whatever abilities you want.
You just need 2 additional classes with 2 unique abilities per additional class.

Additionally, you need to implement a heal() method in the base Character class.
Lastly, you need to randomize the damage done in the Character class' attack() method.
'''

# ====================== BASE CHARACTER CLASS ============================
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    '''
    Modify this function so that the character does a random amount of damage.
    Hint: Look up the randint() function from Python's random library.
    '''
    def attack(self, opponent):
        # Make sure to set this to a random amount of damage, ideally based on attack power.
        damage = self.attack_power 
        
        # Check if the opponent has a 'evadeNextAttack' attribute. If they do not, proceed with the attack.
        if not hasattr(opponent, 'evadeNextAttack'):
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        # Else, if they do have an 'evadeNextAttack' attribute and the value is 0, proceed with the attack.
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == 0:
            opponent.health -= damage
            print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        # Else, if they do have an 'evadeNextAttack' attribute and the value is 1, decrement the value and display that the attack was evaded.
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == 1:
            print(f"\n{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack = 0

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here

# ============================ SUBCLASSES ================================

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, 120, 30)
        self.evadeNextAttack = 0
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Gathering Shadows")
        print("2. Siphoning Strike")
        print("3. Preemptive Dodge")
        action = input("Which ability do you want to use? ")
        
        if action == '1':
            '''
            Ability: Gathering Shadows
            Increases Rogue's damage by 30, but does not attack.
            '''
            self.attack_power += 30
            print(f"\nShadows gather around {self.name} increasing their damage to {self.attack_power}.")
        elif action == '2':
            '''
            Ability: Siphoning Strike
            Strikes the opponent and heals for half of the damage dealt.
            '''
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2 # Floor division rounds to the nearest integer.
            
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} strikes the Dark Wizard with vampiric daggers, dealing {self.attack_power} damage and siphoning the wizards health, healing to {self.health} health.")
        elif action == '3':
            '''
            Ability: Preemptive Dodge
            Dodge the next attack.
            '''
            self.evadeNextAttack = 1
            print(f"\n{self.name} uses Preemptive Dodge. He will evade the next attack!") 