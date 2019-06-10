import random
from subprocess import call

#Grab character values from file

sheetName = 'Kera'
sheetLocation = str('/home/pi/Character_Sheets/'+sheetName+'.txt')
sheetData = open(sheetLocation, 'r')

#Create array of character name, race, and class(es)
characterData = (sheetData.readline())
characterDetails = characterData.split(';')

#Create array of ability scores
abilityContents=(sheetData.readline())
abilityScores = abilityContents.split(';')

#Clean off newline characters from end-of-list items
def clearNewline(list):
    list[-1] = list[-1].strip()
    return

clearNewline(characterDetails)

#Create a more user-friendly string for multiclass characters
def multiClassHandler(list):
    levelString = ""
    for level in range(2,len(list)):
        levelString = levelString + list[level]
        if (list[level] != list[-1]):
            levelString = levelString + "/"
    return levelString

# Print out character name, race, class(es), and ability scores and modifiers
def characterSheet (scores, details):
    print(str(details[0])+', '+str(details[1])+'. '+multiClassHandler(details))
    print('STR = '+scoreMod(scores[0])+' ('+scores[0]+')')
    print('DEX = '+scoreMod(scores[1])+' ('+scores[1]+')')
    print('CON = '+scoreMod(scores[2])+' ('+scores[2]+')')
    print('INT = '+scoreMod(scores[3])+' ('+scores[3]+')')
    print('WIS = '+scoreMod(scores[4])+' ('+scores[4]+')')
    print('CHA = '+scoreMod(scores[5])+' ('+scores[5]+')')

# Calculate ability modifiers
def scoreMod(score):
    mod = (int(score)-10)/2
    if mod >= 0:
        modifier = '+' + str(mod)
        return modifier
    return str(mod)

# Rolls a certain number and size of dice determined by user input
def dieRoller():
    call(['clear'])
    print('This is the Dice Roller screen.\nPlease enter in the number and value of dice to be rolled (example: 3d8).')
    print('You can roll as many times as you like, or enter \'Q\' to exit: ')
    while True:
        dice = raw_input()   # Collects the value and number of dice to be rolled
        dice = dice.lower()  
        if dice == 'q':
            call(['clear'])  # Exits to main menu if 'q' is entered
            return
        for character in range(len(dice)):   # Determines the location of the letter 'd' in the string for dice to be rolled
            if dice[character] == 'd':
                diceBreak = character
        diceNumber = dice[0:diceBreak]   # Number of dice to roll
        diceValue = dice[(diceBreak+1):] # Number of sides the die/dice has
        tempList = []                    # Creates a list to hold the value of each roll
        for x in range(int(diceNumber)):
            tempList.append(random.randint(1,int(diceValue)))
        tempSum = sum(tempList)
        print tempSum, tempList   # Prints out the total of the dice and each individual roll

# Print out saving throw and skill modifiers
def skillsList(scores):
    while(True):
        call(['clear'])
        skills = ['Acrobatics','Animal Handlimg','Arcana','Athletics','Deception',
                  'History','Insight','Intimidation','Investigation','Medicine',
                  'Nature', 'Performance','Persuasion','Religion','Sleight of Hand',
                  'Stealth', 'Survival']
        for x in range(0,len(skills)):
            print (skills[x])
        userExit = raw_input("\nYou can view your skills and appropriate modifiers here.\nEnter \'Q\' to exit: ")
        if userExit.lower() == 'q':
            return

# Prints out a list of spells the character has, and allows for dice rolling required for the spell. Also tracks spell slot usage.
def spellList():
    call(['clear'])
    print('\nHere is a list of the spells you have or know.\nPrepared spells will be followed with (Prep).')
    print('Spells that can be prepared but are not are followed by (Unprep).')
    spellsL0 = ['Bless', 'Guidance', 'Shocking Grasp', 'Thaumaturgy', 'Thunderclap', 'True Strike', 'Light']
    spellsL1 = ['Chromatic Orb', 'Witch Bolt', 'Shield']
    spellsList = [spellsL0, spellsL1]
    for x in range(len(spellsL1)):
        print(' '+str((x+1))+': '+spellsL1[x])
    var = raw_input('Please select a number for the matching spell, or enter \'Q\' to exit: ')
    if var.lower() == 'q':
        call(['clear'])
        return

#Tracks the player's spell slot usage    
def spellSlots(): 
    return



#Beginning of program, starts at main menu splash screen
call(['clear'])
    
while True:
    print
    characterSheet(abilityScores, characterDetails)
    print('\nWelcome to the Python D&D Character Sheet Program!\n')
    print('Option 1: Dice Roller')
    print('Option 2: Skills List')
    print('Option 3: Spells List')
    
    menuSelection = raw_input('\nPlease type the number of the option you want to open.\nYou can also enter \'Q\' to quit: ')
    
    if menuSelection == '1':
        dieRoller()
    if menuSelection == '2':
        skillsList(abilityScores)
    if menuSelection == '3':
        spellList(abilityScores)
    if menuSelection.lower() == 'q':
        sheetData.close()
        exit()
    else:
        call(['clear'])
