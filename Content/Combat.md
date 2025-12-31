# Phases of Combat
1. Setting up the battle map
2. Determining turn order in case of ties
3. Determining ambush for the first round
4. Round start
	1. Start phase
		1. Applying effects from the environment, if any
	2. Action phase
		1. Players and NPCs take their turns in order, choosing and executing one of the following ordered groups:
			1. Move -> Action and Minor Action
			2. Action and Minor Action -> Move
			3. Move -> Move (Running)
			4. Full-turn Action
	3. End phase
		1. Determining of death, leaving combat and fleeing
5. End of round
	1. Return to round start if the combat is continuing.

---
# Rules of Combat
Combat has rules for resolving various situations that players and the GM might come across.

## Battle Map
A battle map is a grid of squares overlaid on top of a map, a sketch or a similar image depicting the location that the combat takes place in. Each square in a battle map is a 1 square meter area. Creatures such as [[Player Characters]] and [[Introduction to Monsters|Monsters]] can be represented with tokens or similar objects on this battle map. Battle maps can be virtual or physical, depending on the medium of play.

### Distances on a Map
Sigil of Uchma has two rule variations for calculating distances on a battle map:
1) Game distance
2) Simulation distance

**Game distance**
With this rule, one square of diagonal distance is treated the same as one square of orthogonal distance. As a result, movement and ability ranges form a cube-like area of effect. Unless specified otherwise, game distance is the default rule.

**Simulation distance**
This variant rule produces more realistic measurements and can be used if the additional tracking is acceptable. Here, diagonal movement alternates between 1 meter and 2 meters, causing movement and ability ranges to be more circular. This creates the same effect as counting two diagonal squares as equal to three orthogonal squares.

## Movement
During combat, a creature can move within the battle map grid for a distance up to its speed. There are various types of speeds used for different types of movement, which are explained below.

### Walking
* Walking is the simplest way of movement.
+ Instead of taking an action, a creature might "walk" twice. This is called "running" and unless specified otherwise, it is equal to double the walking speed.
+ A running creature can't take actions, rapid actions, prepared actions or full-turn actions.

### Flying
+ If a creature can fly, their walking speed is equal to half of its flying speed unless specified otherwise. 
+ Flying speed can be used vertically or horizontally. However, ascending for 1 meter requires 2 meters of flying speed per meter ascended.
+ A flying creature can't use its walking speed unless it lands.
+ Flying creatures are unaffected by effects on the ground unless the effect reaches their altitude.

### Rough Terrain
+ There are two kinds of rough terrain: light and heavy.
	+ Walking or running through light rough terrain such as soft sand or shallow water takes up 2 walking speed per meter walked.
	+ Walking through heavy rough terrain such as quicksand takes up 3 walking speed per meter walked.
	+ Movement via swimming, climbing and crawling is considered to be in heavy rough terrain.

## Action Types and Timing
Each round takes approximately 10 seconds in game.

### Action
These are regular actions. Mostly, only one action can be taken during a turn.

### Minor Actions
There are two kinds of minor actions: rapid actions and prepared actions. Mostly, only one minor action can be taken during a turn.

**Rapid Action**
During a turn, one rapid action can be taken alongside a regular action.

**Prepared Action**
During a turn, one prepared action can be taken alongside a regular action. Actions of this type always come with a trigger, and they are always executed outside a character's turn. Prepared actions last until end of the current round, unless explicitly told otherwise.

Some prepared actions may mention "moving into, out of or within an area". In this case, the attack is done after the creature successfully moves to a new square on the battle map, even if it would be out of range otherwise. 

### Full-turn Action
- A full-turn action takes up your whole turn, meaning you can't move or use any other type of action.

## Special Actions
+ These actions can be taken by any player character as long as they fulfil the requirements. See [[Special Actions|the list of special actions]].

## Precision Rolls
Precision rolls determine whether a weapon attack, a technique or any other ability succeeds against an unwilling target. A precision roll is done against a resistance, such as Parry or Evasion. If the result of this roll exceeds or is equal to the resistance it is rolled against, the roll succeeds and the technique or attack connects. 

A precision roll is calculated according to this formula:
	1d10 + (level)/2 + weapon precision bonus + other bonuses

Terms in this formula are explained below:
	**Level:** Your character's current level.
	**Weapon precision bonus:** This bonus is determined by the type of the weapon held in main hand.
	**Other bonuses:** These are bonuses or penalties which come from various sources like status effects, environment and the like.

In some cases, a specific spell, an ability or an attack might include a precision bonus or penalty itself. Moreover, some abilities may affect multiple targets. In this case, multiple precision rolls are required to determine which targets get affected by this ability.

Unless specified otherwise, all of the resistances of non-living objects are zero.

## Damage
When a creature takes damage, this damage value reduces their health. Damage done to a target is calculated according to this formula:
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

### Stealing Health
Some abilities, magic items or creatures may have health stealing effects. This is always considered magical damage. 

When a creature tries to steal health, the amount it gains is equal to the health loss of target. Unless specified otherwise, health stealing abilities use normal damage calculation. For example, if an ability steals 20 health and the target has 5 magical armor, the user of the ability would be healed for 15. 

## Turn Order
At the start of the combat, determine turn order as follows:

1. Every opposing group rolls a flat 2d10.  
	• Each group must end with a different roll result; reroll as needed until all results are unique.  
	• If a new opposing group enters the combat later, they also roll a flat 2d10. If their result matches an existing group, only the new group rerolls until they have a unique result.
2. All creatures in combat are ordered from highest to lowest based on their current movement speed.  
	• If a creature that has a flying speed is currently on the ground, use its walking speed instead of its flying speed.
3. Resolve ties in movement speed as follows:  
	• Allies with the same movement speed decide their acting order beforehand. This order may be changed during combat using the *speak* special action.  
	• Enemies with the same movement speed use the flat 2d10 results from step 1 to determine who acts first.

A creature can only take one turn per round, even if it would appear again later in the order.


## Ability Durations
+ Effects of abilities with a duration of one or more "hits" trigger and end during the recipient's turns: 
	+ If a creature is bleeding for one hit, they will take bleeding damage at the start of their next turn and the bleeding ends. 
	+ If the bleeding has a duration of two or more hits, then one hit will be spent when the bleeding damage happens.
+ Effects of abilities with a duration of one or more "rounds" end at the start of the turns of their owners.

## Death
+ When a player character falls below 1 health, they are considered "unconscious".
+ An unconscious character is considered prone.
+ If a player character takes damage equal to or more than double their base maximum health in total, they die immediately.
+ At the end phase of each round, unconscious characters make a death save roll against increased thresholds:
	+ Death save rolls are calculated as (1d10 + level/2)
	+ 1st round: 3
	+ 2nd round: 5
	+ 3rd round: 7
	+ 4th round: 9
+ A character dies if they fail any of their death saves or when they reach their 5th consecutive round in unconscious state. 
+ If a character is healed to at least 1 health during unconscious state, they become conscious again and they are considered prone. Temporary health does not count as healing for this purpose.

## Adjacency
+ A creature is adjacent to another if there aren't any battle map squares between them. 
+ Significant height differences caused by the environment may break adjacency.

## Flanking
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
+ Cover does not stack, only the highest applicable one is used.
+ If a creature is completely blocked from another's point of view, they are out of line of sight and can't be interacted with targeted attacks and techniques.
+ Abilities, techniques and attacks which affect an area may require hearing or sight:
	+ Sounds cannot pass through rocks, deep water, or similar materials.
	+ Sounds can pass through up to 1 meter of wood, metal, shallow water, or similar materials.
	+ Cover of any kind doesn't break line of sight.
	+ Magical remote eyes and ears count as sight and hearing for these effects.
	+ Some magical effects may break line of sight or block sounds.

## Falling Prone
+ A creature can go into prone voluntarily if they give up half of their walking speed as a part of their movement during their turn.
+ When a creature falls or goes prone, they need to use half of their walking speed to get up.
+ A prone creature has quarter cover.
+ Attacking a prone creature grants a +1 bonus to precision rolls when adjacent to that creature. This also includes projectile attacks. 
+ A prone creature can only do basic weapon attacks, dealing half damage after armor and ignoring weapon precision.
+ When a flying creature is stunned, immobilized, or falls prone, it loses up to 3 meters of altitude and takes 5 armor-ignoring damage if it collides with the ground or an object.

## Fall Damage
+ A character takes fall damage when they fall more than 5 meters.
+ This damage is armor-ignoring and it is calculated as such:
	+ Fall damage = 10 x (fall distance in meters - 5)

## Ambushes
When the party ambushes or gets ambushed by one or more foes, the ambushed side is considered disadvantageous and they receive the following effects for the next round of combat:
+ -2 penalty to movement speed, down to a minimum of 1 meter
+ -1 penalty to all precision rolls
+ -1 penalty to all resistances

## Summoning
+ Summoner can control their minions during combat. A minion disappears immediately when its summoner dies.
+ Summoners have a simple telepathic bond to their minions. A summoner will know where a minion is and how much damage it suffered at all times. 
+ The minions follow the regular turn order. On a turn a minion is summoned, if they have higher movement speed than their summoner, they take their turn immediately after the summoner.
+ Minions gain potency bonus to their damage normally, according to their relevant potency stat.
+ Minions don't use energy for their skills, unless specified otherwise.

## Transforming
When a creature transforms into another, several rules should be followed:
+ A creature can only use the abilities of what it transformed into, and its stats are set to the stats of the new form. Status effects or abilities with durations are unaffected by transforming. 
+ When returning to the original form, a creature's health is set to what it was before the transformation. Going below 0 health does not break the transformation. See: [[Combat#Death|death]].
+ If a creature is unwillingly transformed during its own turn, this turn immediately ends.
+ If the new form cannot physically fit within the environment, the creature takes 5 armor-ignoring damage and the transformation fails.


## Mounted Combat
#TODO 


## Player versus Player
Conflicts between player characters should be resolved with words. However, sometimes arguments might escalate into fights, duels or even ambushes. In this case, rather than getting into combat, the GM may opt to use the simple method of PvP instead:
1. Players split into teams or stay neutral.
2. Each team rolls a d10 per player. The team that rolls the highest in total wins.
3. The GM may grant up to a +2 bonus to a team’s total if it has a clear situational advantage.