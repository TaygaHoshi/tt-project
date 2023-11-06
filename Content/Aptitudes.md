# Aptitudes
Aptitudes are main traits of a character which take values between 0 and 10. There are five aptitudes: Strength, Endurance, Witchcraft, Social and Divine. Players gain a set amount of Aptitude Points (AP) on each level up. An aptitude can't be larger than the character's total level. After spending an aptitude point, the player must then choose a stat of that aptitude.

Each aptitude is further divided into two stats: a potency stat and a precision stat, respectively. Two stats of an aptitude can't add up to more than the aptitude itself. 

A total of 23 Aptitude Points (AP) can be earned. APs gained per level are given in this table:
```aptitude_table
lvl | 1| 2| 3| 4| 5| 6| 7| 8| 9|10
AP  |+3|+1|+1|+2|+2|+2|+3|+3|+3|+3
```

List of aptitudes is given below:

**Strength Aptitude**
    Potency: Power (POW)
	Precision: Accuracy (ACU)

**Endurance Aptitude**
	Potency: Vitality (VIT)
	Precision: Speed (SPD)

**Witchcraft Aptitude**
	Potency: Arcane (ARC)
	Precision: Penetration (PEN)

**Divine Aptitude**
	Potency: Wrath (WRA)
	Precision: Praying (PRA)

**Social Aptitude**
	Potency: Expression (EXP)
	Precision: Persuasion (PER)

# Resistances
Resistances lower the accuracy of incoming hits. They act as the success thresholds of precision rolls. Resistances are determined by stats, equipment, class and other various things.

Resistances are calculated with the following formula:
	6 + (total level)/2 + (potency of relevant aptitude)/3 + other bonuses

Each class gets to choose a main resistance. Main resistance of a character is calculated separately using the following formula:
	6 + (total level)/2 + (potency of relevant aptitude)/2 + other bonuses

List of resistances is given below:

**Parry**
	Counters ACU rolls.
	Increases with POW.

**Constitution**
	Usually counters attacks that give status effects.
	Increases with VIT.

**Evasion**
	Usually counters area of effect attacks.
	Increases with SPD.

**Reflection**
	Counters PEN rolls.
	Increases with ARC.

**Faith**
	Counters PRA rolls.
	Increases with WRA.

**Willpower**
	Counters PER rolls.
	Increases with EXP.
