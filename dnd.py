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
#or add more based on bonuses etc?

ability_scores = {
	"STR":11,
	"DEX":15,
	"CON":13,
	"INT":20,
	"WIS":11,
	"CHA":11,
}

ability_proficiencies = {
	"STR":0,
	"DEX":0,
	"CON":0,
	"INT":1,
	"WIS":1,
	"CHA":0,
}

#level as index
proficiency_bonus_table = [0,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]

def proficiencyBonus():
	return proficiency_bonus_table[char_level]
	
def abilityProficiencyBonus(ability):
	return proficiencyBonus()*ability_proficiencies[ability]
	
	
#ability modifier table
ability_modifier_table = [0,-5,-4,-4,-3,-3,-2,-2,-1,-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10]

def abilityModifier(ability):
	return ability_modifier_table[ability_scores[ability]]

def abilitySavingThrow(ability):
	return abilityModifier(ability)+abilityProficiencyBonus(ability)
	
	
#dict of skills and the proficiencies that they use
#proficiencies match other dicts
skills = {
	"Athletics":"STR",
	"Acrobatics":"DEX",
	"Sleight of Hand":"DEX",
	"Stealth":"DEX",
	"Arcana":"INT",
	"History":"INT",
	"Investigation":"INT",
	"Nature":"INT",
	"Religion":"INT",
	"Animal Handling":"WIS",
	"Insight":"WIS",
	"Medicine":"WIS",
	"Perception":"WIS",
	"Survival":"WIS",
	"Deception":"CHA",
	"Intimidation":"CHA",
	"Performance":"CHA",
	"Persuasion":"CHA"
}

def printAbilities():
	for k, v in ability_scores.items():
		print("{} score: {}, modifier: {}, proficiency bonus: {}, saving throw: {}".format(k, v, abilityModifier(k), abilityProficiencyBonus(k),abilitySavingThrow(k)))
	return
	
printAbilities()
	
print(abilityModifier("INT"))

#ability modifier based on table
#saving throw = modified + proficience
#how to tell what proficiency is in?

#add logic to set these based on class
hit_dice_per_level=1
hit_dice="d6"

def hitDice():
	#dice_count = hit_dice_per_level*char_level
	return str(hit_dice_per_level*char_level)+hit_dice
	



#passive perception = 10 + wisdom modifier
	
printCharacterTitle()
print("Hit Dice: {}".format(hitDice()))
print("Proficiency Bonus: {}".format(proficiencyBonus()))