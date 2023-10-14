import random

# Player class to store player information
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def add_item(self, item):
        self.inventory.append(item)

# Define some items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

sword = Item("Sword", "A sharp, shiny sword.")
potion = Item("Health Potion", "A magical potion that heals your wounds.")

# Define some enemies
class Enemy:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

goblin = Enemy("Goblin", 10, 30)
dragon = Enemy("Dragon", 20, 100)

# Main game loop
def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    print(f"Welcome, {player.name}! You find yourself in a mysterious forest.")
    
    while player.health > 0:
        print("\n--------------------------")
        print(f"Health: {player.health}")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            explore(player)
        elif choice == "2":
            check_inventory(player)
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

def explore(player):
    if random.random() < 0.5:
        print("You encounter a goblin!")
        fight(player, goblin)
    else:
        print("You find a health potion!")
        player.add_item(potion)
        print("You added a Health Potion to your inventory.")

def check_inventory(player):
    print("Inventory:")
    for item in player.inventory:
        print(item.name + ": " + item.description)

def fight(player, enemy):
    while player.health > 0 and enemy.health > 0:
        print("\n--------------------------")
        print(f"Player Health: {player.health}")
        print(f"{enemy.name} Health: {enemy.health}")
        print("1. Attack")
        print("2. Run")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            player_attack = random.randint(0, 20)
            enemy_attack = random.randint(0, 15)
            
            print(f"You attack {enemy.name} for {player_attack} damage!")
            enemy.health -= player_attack
            print(f"{enemy.name} attacks you for {enemy_attack} damage!")
            player.take_damage(enemy_attack)
        elif choice == "2":
            print(f"You run away from the {enemy.name}!")
            break
        else:
            print("Invalid choice. Try again.")
    
    if player.health <= 0:
        print("You are defeated. Game Over.")
    elif enemy.health <= 0:
        print(f"You have defeated the {enemy.name}!")

if __name__ == "__main__":
    main()
