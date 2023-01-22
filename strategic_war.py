import random

class Soldier:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}"
    
    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        enemy.health -= damage
        print(f"{self.name} dealt {damage} damage to {enemy.name}")

class Army:
    def __init__(self, name, soldiers):
        self.name = name
        self.soldiers = soldiers
        
    def __str__(self):
        return f"Army: {self.name}\n{'-'*20}\n" + "\n".join([str(s) for s in self.soldiers])
        
    def attack_enemy_army(self, enemy_army):
        for soldier in self.soldiers:
            enemy_soldier = random.choice(enemy_army.soldiers)
            soldier.attack_enemy(enemy_soldier)
        enemy_army.soldiers = [s for s in enemy_army.soldiers if s.health > 0]

    def buy_solder (self, name, health, attack, defense, price):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.price = price
        
# Create two armies
army_a = Army("Army A", [Soldier("Soldier 1", 100, 10, 5), Soldier("Soldier 2", 80, 15, 3), Soldier("Soldier 3", 60, 20, 2)])
army_b = Army("Army B", [Soldier("Soldier 4", 120, 7, 8), Soldier("Soldier 5", 90, 10, 5), Soldier("Soldier 6", 70, 12, 4)])

# Game loop
while True:
    # Print status of both armies
    print(army_a)
    print(army_b)
    print("="*20)
    # Player input
    player_choice = input("Enter 'attack' to attack enemy army or 'exit' to quit: ")
    if player_choice == "attack":
        army_a.attack_enemy_army(army_b)
    elif player_choice == "exit":
        break
    else:
        print("Invalid command. Try again.")
    # Check for end of game
    if not army_b.soldiers:
        print("Army B has been defeated!")
        break
    if not army_a.soldiers:
        print("Army A has been defeated!")
        break
