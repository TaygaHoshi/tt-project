# Phases of Combat
1. Setting up the battle map
2. Determining ambush for the first round
3. Round start
	1. Start phase
		1. Calculate turn order for this round
	2. Action phase
		1. Players and NPCs take their turns in order, choosing and executing one of the following ordered groups:
			1. Move -> Action and Rapid Action
			2. Action and Rapid Action -> Move
			3. Move -> Action and Prepared Action
			4. Action and Prepared Action -> Move
			5. Move -> Move (Running)
			6. Full-turn Action
	3. End phase
		1. Death, leaving combat and fleeing
		2. Conversing, discussing, bargaining
4. End of round
	1. Return to round start if necessary.

# Battle Map
A battle map is a grid of squares overlaid on top of a map, a sketch or a similar image depicting a location that the combat takes place in. Each square in a battle map is considered to be a 1 square meter area. Creatures can be represented with tokens or similar objects on this battle map.

# Rules of Combat
Combat has rules for resolving various situations that players and the GM might come across. These can be found [[List of Rules - Combat]].

# Turn Order
At the start phase of every round, turn order will be calculated for this round. There are several rules:
+ Every creature in combat is ordered in terms of their SPD from highest to lowest.
+ Allies with same SPD value must determine who goes first beforehand. This can only be changed in the end phase during combat.
+ If there are creatures with equal SPD in at least any two sides in the combat, the following rules are applied:
	+ The conflicting sides roll a d20 each.
	+ For conflicting turn order spots, higher rolling teams' members will go earlier than the lower rolling teams' members with the same SPD.
	+ If there is a draw, another set of d20s must be rolled between the drawing sides.

A creature can only have one turn within one round, even if the creature is next in initiative order.

## Ability Durations
+ Effects of abilities with a duration of one or more "hits" trigger and end during the recipient's turns: 
	+ If a creature is bleeding for one hit, they will take bleeding damage at the start of their next turn and the bleeding ends. 
	+ If the bleeding has a duration of two or more hits, then one hit will be spent when the bleeding damage happens.
+ Effects of abilities with a duration of one or more "rounds" end at the start of the turns of their owners.

# Action Types and Timing
Each turn takes approximately 10 seconds in game.

## Action
These are regular actions. Mostly, only one action can be taken during a turn.

## Rapid Action
During a turn, one rapid action can be taken alongside a regular action.
A rapid action is mutually exclusive with a prepared action. Only one of them can be taken during a turn.

## Prepared Action
During a turn, one prepared action can be taken alongside a regular action.
This kind of actions always come with a trigger, and they are usually performed outside a character's turn.
Prepared actions last until end of this round, unless explicitly told otherwise.
A prepared action is mutually exclusive with a rapid action. Only one of them can be taken during a turn.

## Special Actions
These actions can be taken by any player character as long as they fulfill the requirements. See [[List of Rules - Special Actions]].

# Precision Rolls
Precision rolls determine whether a weapon attack, a spell, a combat technique or any other ability succeeds against an unwilling target.

A precision roll is done against a resistance, such as Parry or Evasion. If the result of this roll exceeds or is equal to the resistance it is rolled against, the roll succeeds and the spell or attack connects. 

Additionally, if you roll a 10 with a precision roll's d10, the roll succeeds regardless of the relevant resistance. 

## Precision Roll Formula
A precision roll is calculated according to this formula:
	1d10 + (relevant aptitude)/2 + weapon precision bonus + other bonuses

Terms in this formula are explained below:
	**Relevant aptitude:** Equal to half of the weapon's or the spell's aptitude. For example, an elemental wand uses witchcraft. Bonuses to your aptitudes do not affect your precision rolls.
	**Weapon precision bonus:** A weapon's precision type and bonus is determined by the type of the weapon held in main hand or the wielded two-handed weapon.
	**Other bonuses:** These are bonuses or penalties which come from various sources like status effects, environment and the like.

In some cases, a specific spell, an ability or an attack might include a precision bonus or penalty itself. For example, "wide slash" attack of a glaive doesn't include "weapon precision bonus" in its precision roll. We know this because "wide slash" has the phrase "ignores weapon precision" in its explanation. A weapon precision bonus only applies when a precision roll matches the weapon's precision type. For example, a wand of any type normally doesn't affect precision rolls based on strength.

# Damage
When a creature takes damage, this damage value reduces their health.

## Formula
Damage done to a target is calculated according to this formula:
	Action damage + potency of relevant aptitude + other bonuses - target's armor

Terms in this formula are explained below:
	**Action damage:** Action damage is the damage of an attack or a damaging spell. This value is given for each weapon and spell in the description of it. 
	**Potency of relevant aptitude:** Equal to the potency stat of the weapon's or the spell's aptitude. For example, a curved sword uses POW.
	**Other bonuses:**  These are bonuses or penalties which come from various sources like status effects, environment and the like.
	**Target's armor:** Armor is explained in the Armor section. 

In some cases, a specific spell or attack might include a potency bonus or penalty itself. As an example, let's take the Witchcraft spell Elemental Infusion. This spell includes the phrase "potency bonus to damage is halved for this spell". This simply means "potency of relevant aptitude" is divided by two in the formula:
	Action damage + (potency of relevant aptitude)/2 + other bonuses - target's armor

## Armor
Each creature has two kinds of armor: physical armor and magical armor. Normally, damage from weapon attacks and similar abilities are affected by physical armor and damage from magical sources like spells are affected by magical armor. If something is an exception to this rule, this is told in the explanation of it.

## Damaging Ability
For an ability to be considered a "damaging ability", it should have a base damage. Examples could be abilities like "Dissonance", "Shield Bash" or the hatchet's "Hack". Some actions only apply a status effect, but do not have a base damage. These abilities are not considered damaging abilities.

## "Extra damage" versus "Bonus damage"
Extra damage is a completely different packet of damage that just shares the precision roll of another attack. Extra damage has its own values for action damage, potency, bonuses and it is affected by armor separately from the delivering attack.

On the other hand, bonus damage is just added into the delivering attack's damage calculation. Specifically, into the "other bonuses" term.

