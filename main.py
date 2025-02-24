# This imports all the classes we created from a file called 'classes.py'. The * symbol means all. 'from' should reference the file that the classes are stored in.
from classes import *

# This is just an example of how to import your own custom-functions from a separate file. You can delete this if you want.
from customfunctions import helloWorld 

# ======================= CREATE CHARACTER FUNCTION =========================
'''
Creates a character with the desired class, based on user input.
'''
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    print("5. Rogue")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        # Add Archer class here
        pass
    elif class_choice == '4':
        # Add Paladin class here
        pass
    elif class_choice == '5':
        return Rogue(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# ========================== BATTLE FUNCTION =============================
'''
Facilitates battle between the player and the Dark Wizard.
Has a user menu for actions.
'''
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            # Call the heal method here
            pass  # Implement this
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# =========================== MAIN FUNCTION ==============================
'''
Handles the flow of the game.
'''
def main():
    # This is just an example of how to import a functiom from a separate file and call it. You can delete this.
    helloWorld() 
    
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()