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

---
# Rules of Combat
Combat has rules for resolving various situations that players and the GM might come across.

## Battle Map
A battle map is a grid of squares overlaid on top of a map, a sketch or a similar image depicting the location that the combat takes place in. Each square in a battle map is considered to be a 1 square meter area. Creatures can be represented with tokens or similar objects on this battle map.

## Action Types and Timing
Each turn takes approximately 10 seconds in game.
### Action
These are regular actions. Mostly, only one action can be taken during a turn.
### Rapid Action
During a turn, one rapid action can be taken alongside a regular action.
A rapid action is mutually exclusive with a prepared action. Only one of them can be taken during a turn.
### Prepared Action
During a turn, one prepared action can be taken alongside a regular action.
This kind of actions always come with a trigger, and they are always performed outside a character's turn.
Prepared actions last until end of the current round, unless explicitly told otherwise.
A prepared action is mutually exclusive with a rapid action. Only one of them can be taken during a turn.
### Special Actions
These actions can be taken by any player character as long as they fulfill the requirements. See [[Special Actions|the list of special actions]].

## Turn Order
At the start phase of every round, turn order will be calculated for this round. There are several rules:
+ Every creature in combat is ordered in terms of their initiative value from highest to lowest.
+ Allies with same initiative value must determine who goes first beforehand. This can only be changed in the end phase during combat.
+ If there are creatures with equal initiative in at least any two sides in the combat, the following rules are applied:
	+ The conflicting sides roll a d20 each.
	+ For conflicting turn order spots, higher rolling teams' members will go earlier than the lower rolling teams' members with the same initiative.
	+ If there is a draw, another set of d20s must be rolled between the drawing sides.

A creature can only have one turn within one round, even if it is next in initiative order.

## Ability Durations
+ Effects of abilities with a duration of one or more "hits" trigger and end during the recipient's turns: 
	+ If a creature is bleeding for one hit, they will take bleeding damage at the start of their next turn and the bleeding ends. 
	+ If the bleeding has a duration of two or more hits, then one hit will be spent when the bleeding damage happens.
+ Effects of abilities with a duration of one or more "rounds" end at the start of the turns of their owners.

## Movement
See: [[#Battle Map|Battle Maps]]
During combat, a creature can move within the battle map grid. There are various types of moving, which are explained below.

Movement speed of a creature is equal to:
	(base movement speed + other bonuses) squares/round 
	**Base movement speed:** Most creatures have a base movement speed of 6 by default.
### Walking
* Walking is the simplest way of movement. a creature's walking speed is equal to its movement speed, normally.
### Running
+ Instead of taking an action, a creature might "walk" twice. This is called "running" and unless specified otherwise, it is equal to double the walking speed.
+ A running creature can't take actions, rapid actions, prepared actions or full-turn actions.
### Flying
+ If a creature can fly, their flight speed is equal to their walking speed unless specified otherwise. 
+ Flight speed can be used vertically or horizontally. However, ascending takes up 3 flight speed per meter ascended.
+ A flying creature can't use its walking speed unless they land.
+ If a creature is flying, they are unaffected by any effects on the ground, unless the effect is tall enough to reach it.
### Rough Terrain
+ There are two kinds of rough terrain: light and heavy.
	+ Walking or running through light rough terrain such as soft sand or shallow water takes up 2 walking speed per meter walked.
	+ Walking through heavy rough terrain such as quicksand takes up 3 walking speed per meter walked.
	+ Swimming, climbing and crawling are considered heavy rough terrain.

## Precision Rolls
Precision rolls determine whether a weapon attack, a technique or any other ability succeeds against an unwilling target. A precision roll is done against a resistance, such as Parry or Evasion. If the result of this roll exceeds or is equal to the resistance it is rolled against, the roll succeeds and the technique or attack connects.  Additionally, if you roll a 10 with a precision roll's d10, the roll succeeds regardless of the relevant resistance. 

A precision roll is calculated according to this formula:
	1d10 + (level)/2 + weapon precision bonus + other bonuses

Terms in this formula are explained below:
	**Level:** Your character's current level.
	**Weapon precision bonus:** This bonus is determined by the type of the weapon held in main hand.
	**Other bonuses:** These are bonuses or penalties which come from various sources like status effects, environment and the like.

In some cases, a specific spell, an ability or an attack might include a precision bonus or penalty itself.

Some abilities may affect multiple targets. In this case, multiple precision rolls are required to determine which targets get affected by this ability.

## Damage
When a creature takes damage, this damage value reduces their health.

Damage done to a target is calculated according to this formula:
	Action damage + potency + other bonuses - target's armor

Terms in this formula are explained below:
	**Action damage:** Action damage is the damage of the respective ability.
	**Potency:** Equal to the potency aptitude of the character dealing the damage.
	**Other bonuses:**  These are bonuses or penalties which come from various sources like status effects, environment and the like.
	**Target's armor:** Armor is explained in the [[#Armor]] section. 

In some cases, a specific ability might include a potency bonus or penalty itself. As an example, let's take an ability which includes the phrase "potency bonus to damage is halved for this attack". This simply means "potency" is divided by two in the formula:
	Action damage + (potency)/2 + other bonuses - target's armor
### Armor
Each creature has two kinds of armor: physical armor and magical armor. Normally, damage from weapon attacks and similar abilities are affected by physical armor and damage from magical techniques are affected by magical armor. If something is an exception to this rule, this is noted in the description of that ability.
### Damaging Ability
For an ability to be considered a "damaging ability", it should have a base damage. Examples could be abilities like "Shield Bash" or the hatchet's "Hack". Some actions only apply a status effect, but do not have a base damage. These abilities are not considered damaging abilities.
### "Extra damage" versus "Bonus damage"
Extra damage is a completely different packet of damage that just shares the precision roll of another attack. Extra damage has its own values for action damage, potency, bonuses and it is affected by armor separately from the delivering attack.

On the other hand, bonus damage is just added into the delivering attack's damage calculation. Specifically, into the "other bonuses" term.

## Death
+ When a player character falls below 0 health, they are considered "unconscious".
+ An unconscious character is considered prone.
+ If a player character takes damage equal to or more than double their base maximum health in total, they die immediately.
+ At the end phase of each round, unconscious characters make a death save roll against increased thresholds:
	+ Death save rolls are calculated with this formula: (1d10 + level/2)
	+ 1st round: 3
	+ 2nd round: 5
	+ 3rd round: 7
	+ 4th round: 9
+ A character dies if they fail any of their death saves or when they reach their 5th consecutive round in unconscious state. 
+ If a character is healed to at least 1 health during unconscious state, they become conscious again and they are considered prone.

## Adjacency
+ A creature is adjacent to another if there aren't any battle map squares between them. 
+ Significant height difference between two creatures due to environmental factors may break adjacency. 
### Flanking
+ During battle, whenever a creature has two or more adjacent foes wielding melee weapons, it is considered flanked.
+ Attacking a flanked creature grants a +1 bonus to precision rolls done with melee abilities.

## High and Low Ground
A significant difference in elevation affects projectile attacks' precision rolls:
1. Attacking from high ground grants you a +1 bonus.
2. Attacking from low ground gives you a -1 penalty.

## Cover and Line of Sight
+ When a character is behind cover, they are semi-protected against projectile attacks or abilities.
+ There are 3 types of cover:
	+ Quarter Cover: +1 bonus to all resistances versus projectiles.
	+ Half Cover: +2 bonus to all resistances versus projectiles.
	+ Full Cover: +4 bonus to all resistances versus projectiles.
+ Having other creatures in the way while determining cover counts as half cover. This doesn't increase with the amount of creatures in the way.
+ If a creature is completely blocked from another's point of view, they are out of line of sight and can't be interacted with targeted attacks and techniques.
+ Abilities, techniques and attacks which affect an area may require hearing or sight:
	+ Sounds can't pass rocks, deep water and similar materials.
	+ Sounds can pass 1 meter of wood, metal, shallow water and other similar materials.
	+ Cover of any kind doesn't break line of sight.
	+ Magical remote eyes and ears count as sight and hearing for the purposes of these kind of effects.
	+ There may be magical effects which can break line of sight or block sounds.

## Falling Prone
+ A creature can go into prone voluntarily if they give up half of their base movement speed as a part of their movement during their turn.
+ When a creature falls or goes prone, they have to be in movement phase of their turn and use half of their base movement speed to get up.
+ A prone creature has half cover against projectiles.
+ A prone creature has -2 to all resistances against abilities used within melee range, including projectiles.
+ A prone creature can only do their basic weapon attack, dealing half damage and ignoring weapon precision.

## Fall Damage
+ A character takes fall damage when they fall more than 5 meters.
+ This damage is armor-ignoring and it is calculated as such:
	+ Fall damage = 10 x (fall distance in meters - 5)

## Ambushes
When the party ambushes or gets ambushed by one or more foes, the ambushed side is considered disadvantageous and they receive the following effects for the next round of combat:
+ -2 penalty on initiative
+ -1 penalty on all precision rolls
+ -1 penalty on all resistances

## Summoning
+ Summoner can control their minions during combat. A minion disappears immediately when its summoner dies.
+ Summoners have a simple telepathic bond to their minions. A summoner will know where a minion is and how much damage it suffered at all times. 
+ The minions follow the regular initiative order. On a turn a minion is summoned, if they have higher initiative than their summoner, they take their turn immediately after the summoner.
+ Minions gain potency bonus to their damage normally, according to their relevant potency stat.
+ Minions don't use energy and energy for their skills, unless specified otherwise.

## Mounted Combat
#TODO 

## Transformation and Transforming
#TODO 

## Player versus Player
#TODO 