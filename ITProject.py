from random import randint, choice

#JD - Item super class
class ItemBase:
    def __init__ (name):
        self.name = name
    #An "Abstract" base method with no implementation
    def use(self):
        raise NotImplementedError("Method not implemented for item base class")

#JD - Consumable item derived class
class ItemConsumable(ItemBase):
    def __init__ (self, name, message):
        self.name = name
        self.message = message;
    def use(self): 
        player.heal()
        print(self.message)

#JD - Weapon item derived class
class ItemWeapon(ItemBase):
    def __init__(self, name, message, dmg):
        self.name = name
        self.message = message
        self.dmg = dmg
    def use(self):
        monster.hurt(self.dmg)
        print(self.message)

#Item definitions
pizza = ItemConsumable("Nino's Pizza", "Pizza consumed, restoring some health")
fishChips = ItemConsumable("Fish and Chips", "Nothing's better than Victor's fish and chips")
tennisBall = ItemWeapon("Tennis Ball", "Tennis ball was thrown, doing 4 damage", 4)
	
#Super class for "Living Things"
class LivingThing():
    def __init__(self):
        self.name = 'null'
        self.health = 1
    
	#Causes living thing to take damage over time
	#JR - Changed so damage taken is based on difficulty
    def tire(self):
        if diff == 'hard':
            self.health = self.health - randint(2, 4)
        elif diff == 'medium':
            self.health = self.health - randint(1, 3)
        elif diff == 'easy':
            self.health = self.health - randint(0, 1)
            # JR - old code: self.health = self.health - 2 
	
    #Reduce living thing health by specified amount
    def hurt(self, dmg):
        self.health = self.health - dmg
	
    #Regenerate health
    #JR - Changed so health regeneration is based on difficulty
    def heal(self):
        if diff == 'hard':
            if self.health < 5:
                self.health = self.health + randint(0, 1)
        elif diff == 'medium':
            if self.health < 8:
                self.health = self.health + 1
            elif self.health < 15:
                self.health = self.health + randint(0, 1)
        elif diff == 'easy':
            if self.health < 15:
                self.health = self.health + 1
                # JR - old code: self.health = self.health + 1
	

#Player class
class Player(LivingThing):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.status = 'regular'
        self.inventory = {"Nino's Pizza" : [pizza, 2], "Tennis Ball" : [tennisBall, 1]}
		
    #Show the user their options
    def help(self, monster):
        print('\nYour options are:')
        for key in Commands.keys():
            print(key)
		
	#Displays the player's stats
    def stats(self, monster):
        print(' ')
        print(self.name + '\'s stats:')
        print('Health:', self.health)
        print('Current status:', self.status)
        print('Inventory:')
        for item in self.inventory:
            print(" - ", item, ':', self.inventory[item])
        print(monster.name, 'health is', str(monster.health) + '.')
		
    #Allows the player to "search" the envieronment
    def explore(self, monster):
        #Heal player
        self.heal()
        print(' ')
        print('Your health is now', str(self.health) + '.')
        
		#Inventory test <--- Ignore this
        if randint(0, 1) == 1:
	        #Increase the number of Fubars if one Fubar has already been collected
            if 'Fubar' in self.inventory:
                print(player.name, 'found another Fubar.')
                self.inventory['Fubar'] = self.inventory['Fubar'] + 1
            else:
                print('Fubar acquired!')
                self.inventory['Fubar'] = 1
	    
		#Determine if an encounter occurs
        if randint(0, 1) == 1:
            print(monster.name, 'confronts you...')
            #print('What do you do?')
            self.status = 'confronted'
	
	#Null
    def run(self, monster):
	    #Determine if player escapes
        if randint(0, self.health) < randint (0, monster.health):
            print(' ')
            print('A monster has appeared.')
            self.status = 'confronted'
            self.fight(monster)
        else:
            self.tire()
            monster.heal()
            print(' ')
            print('Your health suffered by running.')
            print('health is now', str(self.health) + '.')

	
    #Fight the monster
    def fight(self, monster):
        if self.status == 'confronted':
            monster.hurt(2)
            self.hurt(monster.attack_dmg)
            print(monster.name, 'attacked you, doing', monster.attack_dmg, 'damage.')
            
            #Print info
            if self.health <= 0:
                print('You were killed by the', monster.name.lower() + '.')
            elif monster.health > 0:
                print('You survived the', monster.name.lower() + '.')
                print('Your health is now', str(self.health) + '.')
            else:
                print('Victory! You defeated the ', monster.name.lower() + '.')
        
        else:
            print('You are safe.')

    #Allows player to use an item - JD
    def use(self, monster, item):
        if(item in self.inventory):
            self.inventory[item][0].use()
            self.inventory[item][1] = self.inventory[item][1] - 1;
	    #Remove item from inventory if quantity is now at 0
            if(self.inventory[item][1] == 0):
                del self.inventory[item]

# Monster class #
class Monster(LivingThing):
    def __init__(self, name, health, attack_dmg):
        self.name = name
        self.health = health
        self.status = 'regular'
        self.attack_dmg = attack_dmg

#JR - Difficulty
diff_choice = ["easy", "medium", "hard"]
print(" ")
diff = input('What difficulty would you like (easy/medium/hard)? ')
while diff not in diff_choice:
    print(" ")
    print('Please check spelling and caps.')
    diff = input('What difficulty would you like (easy/medium/hard)? ')

#Take player's name
print(" ")
name = input('What is your name? ')
player = Player(name, 20)

#Monsters
geezer = Monster('Grumpy Elderly Person', 6, 2)
penguin = Monster('Killer Penguin', 8, 4)
while = Monster('Whale', 14, 6)

#List of fightable monsters
#JR - added monster choice based on difficulty
monsters = []
if diff == "easy":
    monsters.append(geezer)
elif diff == "medium":
    monsters.append(penguin)
elif diff == "hard":
    monsters.append(whale)

#Choose a random monster
monster = choice(monsters)
		
#Constant list of valid inputs, player.use was removed - JD
Commands = {
'help': player.help,
'stats': player.stats,
'explore': player.explore,
'run': player.run,
'fight': player.fight,
}
	
#Game Loop
#JR - added following 3 lines:
print(" ")
print('**********************(TYPE "help" TO GET A LIST OF ACTIONS)**********************')
print(" ")
#JR - altered this to fit with our game rather than old one
print(player.name, 'enters Victor Harbor, searching for the perfect store. When walking down the street, you run into a', monster.name.lower() + '.')

#JR - unnecessary    "print('\n')"
#Get input, if it is a valid command execute it
while player.health > 0 and monster.health > 0:
    line = input('What do you want to do? ')
    if line in Commands.keys():
        Commands[line](monster)
    elif line[:3] == "use":
	#Process string and use item
	player.use(line[4:])
    else:
        print(player.name, 'does not understand.')

# JR - changed so that eg. "Jackson was slain." didn't appear when player killed monster
if player.health <= 0 and monster.health > 0:
    print(player.name, 'was slain.')

print('\n-=+Game Over+=-')

