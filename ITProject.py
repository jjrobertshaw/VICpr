from random import randint, choice

#Super class for "Living Things"
class LivingThing():
    def __init__ (self):
        self.name = 'null'
        self.health = 1
	
	#Causes living thing to take damage over time
    def tire(self):
	    self.health = self.health - 2 
	
    #Reduce living thing health by specified amount
    def hurt(self, dmg):
        self.health = self.health - dmg
	
	#Regenerate health
    def heal(self):
	    self.health = self.health + 1
	

#Player class
class Player(LivingThing):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.status = 'regular'
        self.inventory = {'Foo' : 2, 'Bar' : 1}
		
    #Show the user their options
    def help(self, monster):
        print('\n')
        print('Your options are:')
        for key in Commands.keys():
            print(key)
		
	#Displays the player's stats
    def stats(self, monster):
        print('\n')
        print(self.name + '\'s stats:')
        print('Health:', self.health)
        print('Current status:', self.status)
        print('Inventory [2/5]')
        for item in self.inventory:
            print(" - ", item, ':', self.inventory[item])
        print(monster.name, 'health is', monster.health, '\n')
		
    #Allows the player to "search" the envieronment
    def explore(self, monster):
        #Heal player
        self.heal()
        print('\n')
        print('Your health is now', self.health)
        
		#Inventory test <--- Ignore this
        if randint(0, 1) == 1:
	        #Increase the number of Fubars if one Fubar has already been collected
            if 'Fubar' in self.inventory:
                print(player.name, 'found another Fubar')
                self.inventory['Fubar'] = self.inventory['Fubar'] + 1
            else:
                print('Fubar acquired')
                self.inventory['Fubar'] = 1
	    
		#Determine if an encounter occurs
        if randint(0, 1) == 1:
            print(monster.name, 'confronts you')
            print('What do you do?')
            self.status = 'confronted'
	
	#Null
    def run(self, monster):
	    #Determine if player escapes
        if randint(0, self.health) < randint (0, monster.health):
            print('\n')
            print('A monster has appeared')
            self.status = 'confronted'
            self.fight(monster)
        else:
            self.tire()
            monster.heal()
            print('\n')
            print('Your health suffered by running.')
            print('health is now', self.health)

	
	#Fight the monster
    def fight(self, monster):
        if self.status == 'confronted':
            monster.hurt(2)
            self.hurt(monster.attack_dmg)
            print('\n')
            print(monster.name, 'attacked you, doing', monster.attack_dmg, 'damage')
            
            #Print info
            if self.health <= 0:
                print('You were killed by the', monster.name.lower(), '\n')
            elif monster.health > 0:
                print('You survived the', monster.name.lower())
                print('Your health is now', self.health)
            else:
                print('Victory! You defeated the ', monster.name.lower())
        
        else:
            print('You are safe.')

	#Allows player to use an item
    def use(self, monster):
        	
            
		
#Monster class
class Monster(LivingThing):
    def __init__(self, name, health, attack_dmg):
        self.name = name
        self.health = health
        self.status = 'regular'
        self.attack_dmg = attack_dmg

#Take player's name
name = input('What is your name?\n')
player = Player(name, 20)

#Monsters
goblin = Monster('Goblin', 30,5)
spider = Monster('Spider', 20, 10)
dragon = Monster('Dragon', 50, 15)

#List of fightable monsters
monsters = []
monsters.append(goblin)
monsters.append(spider)
monsters.append(dragon)

#Choose a random monster
monster = choice(monsters)
		
#Constant list of valid inputs
Commands = {
'help' : player.help,
'stats' : player.stats,
'explore' : player.explore,
'run' : player.run,
'fight' : player.fight,
'use' : player.use
}
	
#Game Loop
print ('(type \"help\" to get a list of actions)')
print(player.name, 'enters a dark cave, searching for adventure. You will soon face the', monster.name.lower(), '\n')

while player.health > 0 and monster.health > 0:
    print('\n')
    #Get input, if it is a valid command execute it
    line = input('What do you want to do?\n')
    if line in Commands.keys():
        Commands[line](monster)
	elif line[0:3] == "use":
	    print("FUBAR")
    else:
	    print(player.name, 'does not understand.')

print(player.name, 'was slain.\n-=+Game Over+=-')