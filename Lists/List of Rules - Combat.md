(see: [[Combat]])

# Movement
(see: [[Combat#Battle Map|Battle Maps]])
During combat, a creature can move within the battle map grid. There are various types of moving, which are explained below.

Movement speed of a creature is equal to:
	(base movement speed + other bonuses) meters/round

Base movement speed of a creature is calculated with the formula below:
	(10 + SPD) meters/round

## Walking
* Walking is the simplest way of movement. a creature's walking speed is equal to its movement speed, normally.

## Running
+ Instead of taking an action, a creature might "walk" twice. This is called "running" and unless specified otherwise, it is equal to double the walking speed.
+ A running creature can't take actions, rapid actions, prepared actions or full-turn actions.

## Flying
+ If a creature can fly, their flight speed is equal to their walking speed unless specified otherwise. 
+ Flight speed can be used vertically or horizontally. However, ascending takes up 4 flight speed per meter ascended.
+ A flying creature can't use its walking speed unless they land.
+ If a creature is flying, they are unaffected by any effects on the ground, unless the effect is tall enough to reach it.

## Rough Terrain
+ There are two kinds of rough terrain: light and heavy.
	+ Walking or running through light rough terrain such as soft sand or shallow water takes up 2 walking speed per meter walked.
	+ Walking through heavy rough terrain such as quicksand takes up 4 walking speed per meter walked.
	+ Swimming, climbing and crawling are considered heavy rough terrain.

# Death
+ When a player character falls below 0 health, they are considered "unconscious".
+ An unconscious character is considered prone.
+ If a player character takes equal to or more than double their base maximum health, they die immediately.
+ At the end phase of each round, unconscious characters make a death save roll against increased thresholds:
	+ Death save rolls are calculated with this formula: (1d10 + VIT)
	+ 1st round: 3
	+ 2nd round: 5
	+ 3rd round: 7
	+ 4th round: 9
+ A character dies if they fail any of their death saves or when they reach their 5th consecutive round in unconscious state. 
+ If a character is healed to at least 1 health during unconscious state, they become conscious again and they are considered prone.

# Summoning
+ Summoner can control their minions during combat. A minion disappears immediately when its summoner dies.
+ Summoners have a simple telepathic bond to their minions. A summoner will know where a minion is and how much damage it suffered at all times. 
+ The minions follow the regular initiative order. On a turn a minion is summoned, if they have higher initiative than their summoner, they take their turn immediately after the summoner.
+ Minions gain potency bonus to their damage normally, according to their relevant potency stat.
+ Minions don't use energy and energy for their skills, unless specified otherwise.

# Transformation and Transforming
#TODO 

# Cover and Line of Sight
+ When a character is behind cover, they are semi-protected against projectile attacks or projectile spells.
+ There are 3 types of cover:
	+ Quarter Cover: +1 bonus to all resistances versus projectiles.
	+ Half Cover: +2 bonus to all resistances versus projectiles.
	+ Full Cover: +4 bonus to all resistances versus projectiles.
+ Having other creatures in the way while determining cover counts as half cover. This doesn't increase with the amount of creatures in the way.
+ If a creature is completely blocked from another's point of view, they are out of line of sight and can't be interacted with targeted attacks and spells.
+ Abilities, spells and attacks which affect an area may require hearing or sight:
	+ Sounds can't pass rocks, deep water and similar materials.
	+ Sounds can pass 1 meter of wood, metal, shallow water and other similar materials.
	+ Cover of any kind doesn't break line of sight.
	+ Magical remote eyes and ears count as sight and hearing for the purposes of these kind of effects.
	+ There may be magical effects which can break line of sight or block sounds.

# Adjacency
+ A creature is adjacent to another if there aren't any battle map squares between them. 
+ Significant height difference between two creatures due to environmental factors may break adjacency. 

# Flanking
+ During battle, whenever a creature has two or more adjacent foes wielding melee weapons, they are considered flanked.
+ Attacking a flanked creature grants a +1 bonus to precision rolls done with melee abilities.

# Falling Prone
+ A creature can go into prone voluntarily if they give up half of their base movement speed as a part of their movement during their turn.
+ When a creature falls or goes prone, they have to be in movement phase of their turn and use half of their base movement speed to get up.
+ A prone creature has half cover against projectiles.
+ A prone creature has -2 to all resistances against attacks and spells used within melee range, including projectiles.
+ A prone creature can only do their basic weapon attack, dealing half damage and ignoring weapon precision.

# Fall Damage
+ A character takes fall damage when they fall more than 3 meters.
+ The damage from fall is armor-ignoring and it is calculated as such:
	+ Fall damage = 10 x (fall distance in meters - 3)

# High and Low Ground
A significant difference in elevation affects projectile attacks' precision rolls:
1. Attacking from high ground grants you a +1 bonus.
2. Attacking from low ground gives you a -1 penalty.

# Ambushes
When the party ambushes or gets ambushed by one or more foes, the ambushed side is considered disadvantageous and they receive the following effects for the first round of combat:
+ -2 penalty on SPD
+ -1 penalty on all precision rolls
+ -1 penalty on all resistances

# Mounted Combat
#TODO 

# Food & Eating
#TODO 

# Player versus Player
#TODO 