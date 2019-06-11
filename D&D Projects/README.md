# D&D Projects
This directory contains a character sheet manager/dice roller written in Python.

My goals for this program is to have a fully-independent program for managing all features in relation to tracking character's equipment and abilities, spells and spell slots if the character can use any, and capability to create new characters along with leveling up existing characters.

## Core Functionality
The list below shows the highest priority of features this program will use.
  1) Dice Roller
  2) Core stats, modifiers, and skill values
  3) Combat related values (AC, initiative, hitpoints)
  4) Weapons and Spells
  Further proficiencies, equipment, and other details can be placed in a "Notes" section if needed.
  
## Known Issues/Potential Future Upgrades
### Character Selection
Current data to draw from is located in a text file and pointers are hardcoded based on initial coding on a Raspberry Pi. File chosen is also hardcoded and will be changed to allow for users to select from multiple character sheets in a later revision.

Data is also insecure and able to be changed. Currently unsure how to make data contained in folder more secure.

### Main Page
Details regarding character stats could be more user-friendly. Potential improvement could be allowing user to select how they would like data to be displayed from a selection of formats coded into program.

### Dice Roller
Entire program will break if syntax for dice roll is not followed, and passing 0 to the second part of the string may also break the code as well (though this has not been tested). Need to add code for error handling and prevent improper syntax.

Currently able to only roll one set of dice at once with no modifiers. This functionality is needed for doing stat rolls for a new character.

### Skills Page
Currently incomplete, does not display appropriate values for each skill let alone proficiency and any bonuses to each skill. Currently planning on using a #**+ format in data sheet, where the first * denotes proficiency, the second denotes double proficiency bonus, and the plus denotes any relevant modifiers.

### Spells Page
Currently incomplete, does not show all spells and does not track spell slot usage.
