#first phase of dnd program
#just kinda going for items
#will probably change EVERYTHING

#variable for character
#the stuff that everything else is calculated from
#store these in a json file or something?
char_name = "Aldred Myrkwood"
char_race = "Human"
char_class = "Wizard"
char_level = 8

def printCharacterTitle():
	print("{}, Level {} {} {}".format(char_name, char_level, char_race, char_class))
	return


#ability scores
#what you rolled when you created your character
#need to add more based on bonuses etc.
char_base_str = 10
char_base_dex = 15
char_base_con = 12
char_base_int = 15
char_base_wis = 10
char_base_cha = 10

#ability modifier based on table
#saving throw = modified + proficience
#how to tell what proficiency is in?

#add logic to set these based on class
hit_dice_per_level=1
hit_dice="d6"

def hitDice():
	#dice_count = hit_dice_per_level*char_level
	return str(hit_dice_per_level*char_level)+hit_dice
	
#level as index
proficiency_bonus_table = [0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]

def proficiencyBonus():
	#calculate proficiency bonus
	return proficiency_bonus_table[char_level]


#passive perception = 10 + wisdom modifier
	
printCharacterTitle()
print("Hit Dice: {}".format(hitDice()))
print("Proficiency Bonus: {}".format(proficiencyBonus()))