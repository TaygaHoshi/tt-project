+++
title = 'Combat'
type = "chapter"
weight = 2
+++

## Phases of Combat
1. Setting up the battle map
2. Determining turn order in case of ties
3. Determining ambush for the first round
4. Round start
	1. Start phase
		1. If any, applying effects from the environment such as weather.
		2. Reorder the turn orders of the participants if needed. 
	2. Action phase
		1. Players and NPCs take their turns in order, choosing and executing one of the following ordered groups:
			1. Move -> Action and Minor Action
			2. Action and Minor Action -> Move
			3. Move -> Move (Running)
			4. Full-turn action
	3. End phase
		1. Determining of death, leaving combat and fleeing
		2. During this phase the *speak* common action is free to use without requiring action economy.
5. End of round
	1. Return to round start if the combat is continuing.

---
## Basic Rules of Combat
Combat has rules for resolving various situations that players and the GM might come across.

### Battle Map
A battle map is a grid of squares overlaid on top of a map, a sketch or a similar image depicting the location that the combat takes place in. Each square in a battle map is a 1 square meter area. Creatures such as [[Character Creation|player characters]] and [[Monsters|monsters]] can be represented with tokens or similar objects on this battle map. Battle maps can be virtual or physical, depending on the medium of play.

#### Distances on a Map
Sigil of Uchma has two rule variations for calculating distances on a battle map:
1) Game distance
2) Simulation distance

**Game distance**
With this rule, one square of diagonal distance is treated the same as one square of orthogonal distance. As a result, movement and ability ranges form a cube-like area of effect. This is the default rule.

**Simulation distance**
This variant rule produces more realistic measurements and can be used if the additional calculations and tracking is acceptable, especially when using virtual tabletops. With this rule, diagonal movement alternates between 1 meter and 2 meters, causing movement and ability ranges to be more circular. This creates the same effect as counting two diagonal squares as equal to three orthogonal squares.

### Movement
During combat, a creature can move within the battle map grid for a distance up to its speed. There are various types of speeds used for different types of movement, which are explained below.

#### Walking
+ Walking is the simplest way of movement.
+ Instead of taking an action, a creature might "walk" twice. This is called "running" and unless specified otherwise, it is equal to double the walking speed.
+ A running creature can't take actions, rapid actions, prepared actions or full-turn actions.

#### Flying
+ If a creature can fly, their walking speed is equal to half of its flying speed unless specified otherwise. 
+ Flying speed can be used vertically or horizontally. However, ascending for 1 meter requires 2 meters of flying speed per meter ascended.
+ A flying creature can't use its walking speed unless it lands.
+ Flying creatures are unaffected by effects on the ground unless the effect reaches their altitude.

#### Rough Terrain
+ There are two kinds of rough terrain: light and heavy.
	+ Walking or running through light rough terrain such as soft sand or shallow water takes up 2 walking speed per meter walked.
	+ Walking through heavy rough terrain such as quicksand takes up 3 walking speed per meter walked.
	+ Movement via swimming, climbing and crawling is considered to be in heavy rough terrain.

### Action Types and Timing
Each round takes approximately 10 seconds in game.

#### Action
These are regular actions. Mostly, only one action can be taken during a turn.

#### Minor Actions
There are two kinds of minor actions: rapid actions and prepared actions. Mostly, only one minor action can be taken during a turn.

**Rapid action**
During a turn, one rapid action can be taken alongside a regular action.

**Prepared action**
During a turn, one prepared action can be taken alongside a regular action. Actions of this type always come with a trigger, and they are always executed outside a character's turn. Prepared actions last until end of the current round, unless explicitly told otherwise.

Some prepared actions may mention "moving into, out of or within an area". In this case, the attack is done after the creature successfully moves to a new square on the battle map, even if it would be out of range otherwise. 

#### Full-turn action
+ A full-turn action takes up your whole turn, meaning you can't move or use any other type of action.

### Targeting and Line of Sight
+ A creature has line of sight to objects and creatures it can directly see.
	+ Some abilities may grant line of sight to a creature or object that isn't directly visible.
+ If a creature is completely blocked from another's point of view, they are out of line of sight and can't be interacted with targeted attacks and techniques.
+ However, even when there is line of sight, some abilities such as most weapon attacks, area of effect abilities and projectiles will not reach the target if a sufficiently large and durable object such as a wall is in the way. 
+ In addition, some abilities such as the *speak* common action may require hearing:
	+ Under most circumstances, sounds are clearly hearable up to 15 meters.
	+ Rocks, deep water, or similar materials block sound. Similarly, some magical effects may block sounds.
	+ Sounds can pass through up to 1 meter of wood, metal, shallow water, or similar materials.
+ If an ability allows you to choose one or more targets, as long as you only target one creature, that ability is considered a single target ability. This does not apply to radius based area of effect abilities.
+ In addition to the above rules, unless specified otherwise, you count as your own ally. 

### Precision Rolls
Precision rolls determine whether a weapon attack, a technique or any other ability succeeds against an unwilling target. A precision roll is made against a resistance, such as Parry or Evasion. If the result of this roll exceeds or is equal to the resistance, the roll succeeds and the technique or attack connects. 

A precision roll is calculated according to this formula:
$\text{1d10} + \frac{\text{level}}{2} + \text{weapon precision} + \text{other bonuses}$

Terms in this formula are explained below:
	**Level:** Your character's current level.
	**Weapon precision:** This bonus is determined by the type of the currently wielded weapons.
	**Other bonuses:** These are bonuses or penalties which come from various sources like status effects, environment and the like.

In some cases, a specific technique, an attack or another ability might include a precision bonus or penalty itself. Moreover, some abilities may affect multiple targets or the same target multiple times, in which case separate precision rolls are required.

Unless specified otherwise, all resistances of non-living objects are zero.

### Damage
When a creature takes damage, this damage value reduces their health. Damage done to a target is calculated according to this formula:
$\text{Action damage} + \text{Potency} + \text{other bonuses} - \text{target's armor (when applicable)}$

Terms in this formula are explained below:
	**Action damage:** Action damage is the damage of the respective ability.
	**Potency:** Equal to the potency aptitude of the character dealing the damage.
	**Other bonuses:**  These are bonuses or penalties which come from various sources like status effects, environment and the like.
	**Target's armor:** Armor is explained in the [[#Armor]] section. 

In some cases, a specific ability might include a potency bonus or penalty itself. As an example, let's take an ability which includes the phrase "potency bonus to damage is halved for this attack". This simply means "potency" is divided by two in the formula:
$\text{Action damage} + \frac{\text{Potency}}{2} + \text{other bonuses} - \text{target's armor (when applicable)}$

#### Armor
Each creature has two kinds of armor: physical armor and magical armor. Normally, damage from physical weapon attacks and similar abilities are affected by physical armor and damage from magical techniques or magical weapons are affected by magical armor. If something is an exception to this rule, this is noted in the description of that ability.

#### Damaging Ability
For an ability to be considered a "damaging ability", it should have a base damage. Examples could be abilities like "Shield Bash" or the hatchet's "Hack". Some actions only apply a status effect, but do not have a base damage. These abilities are not considered damaging abilities.

#### Damage Packets
Extra damage is a completely different packet of damage that just shares the precision roll of another attack. Extra damage has its own values for action damage, potency, bonuses and it is affected by armor separately from the delivering attack. 

On the other hand, bonus damage is just added into the delivering attack's damage calculation. Specifically, into the "other bonuses" term.

#### Stealing Health
Some abilities, magic items or creatures may have health stealing effects. This is always considered magical damage. 

When a creature successfully hits with a health steal ability, the amount of health it gains is equal to the health loss of target. Unless specified otherwise, health stealing abilities use normal damage calculation. For example, if an ability steals 20 health and the target has 5 magical armor, the user of the ability would be healed for 15. 

### Turn Order
At the start of the combat, determine turn order as follows:
1. Every opposing group rolls a flat (2d10).  
	• Each group must end with a different roll result; reroll as needed until all results are unique.  
	• If a new opposing group enters the combat later, they also roll a flat (2d10). If their result matches an existing group, only the new group rerolls until they have a unique result.
2. All creatures in combat are ordered from highest to lowest based on their current movement speed.  
	• If a creature that has a flying speed is currently on the ground, use its walking speed instead of its flying speed.
3. Resolve ties in movement speed as follows:  
	• Allies with the same movement speed decide their acting order beforehand. This order may be changed during combat using the *speak* common action.  
	• Enemies with the same movement speed use the flat (2d10) results from step 1 to determine who acts first.

At the start of every round, the creatures participating in the encounter are reordered based on their current movement speed, based on the steps #2 and #3 described above.  

A creature can only take one turn per round, even if it would appear again later in the order.

#### Fleeing from Combat
When a creature wants to flee from combat, it needs to reach one of the open edges of the battle map. Once reached the edge, it can attempt to escape at the end phase of the round, at which point pursuers are also determined. For this creature to successfully escape, there are a few conditions that needs to be met:
1. If the creature is faster than all of its pursuers, it can run away successfully unless the terrain or another obstacle prevents its escape. 
2. If the creature's movement speed is equal to its fastest pursuers:
	- It must make an athletics skill check of against a success threshold of 9.
	- Alternatively, if there are ways for it to lose its pursuers such as moving through a dense forest, the creature can make a scouting skill check. The GM determines the success threshold depending on the situation. 
3. If the creature's movement speed is slower than the fastest of its pursuers, it needs a way to lose its pursuers via a scouting skill roll as described above. Otherwise it can't flee from combat.

On a successful escape, both the fleeing creature and its pursuers leave the battle map.

### Ability Durations
+ All ability durations are measured in rounds.
+ At the start of a creature's turn, damaging effects and regeneration trigger:
	+ If a creature is bleeding for 1 round, it takes bleeding damage at the start of its turn, then the bleeding ends at the end of that same turn.
	+ If the bleeding has a duration of 2 or more rounds, it triggers at the start of the turn as normal, then the duration decrements by one at the end of that turn.
+ At the end of a creature's turn, all active effect durations decrement by one. Effects that reach zero rounds end.
+ Durations of abilities that does not target creatures, such as *elemental ground*, decrement at the end of the user's turns starting from their next turn.
+ If multiple effects would end at the same time, they end in the order of application.

### Adjacency
+ A creature is adjacent to another if there aren't any battle map squares between them. 
+ Significant height differences caused by the environment may break adjacency.

### Flanking
+ During battle, whenever a creature has two or more adjacent foes wielding melee weapons, it is considered flanked.
+ Attacking a flanked creature grants a +1 bonus to precision rolls done with melee abilities.

### High and Low Ground
A significant difference in elevation affects projectile attacks' precision rolls:
1. Attacking from high ground grants you a +1 bonus.
2. Attacking from low ground gives you a -1 penalty.

### Cover
+ When a character is behind cover, they are semi-protected against projectile attacks or abilities.
+ There are 3 types of cover:
	+ Quarter Cover: -1 penalty to precision rolls with projectile abilities.
	+ Half Cover: -2 penalty to precision rolls with projectile abilities.
	+ Full Cover: -4 penalty to precision rolls with projectile abilities.
+ Having other creatures in the way while determining cover counts as half cover. This doesn't increase with the amount of creatures in the way.
+ Cover does not stack, only the highest applicable one is used.

### Falling Prone
+ A creature can go into prone voluntarily if they give up half of their walking speed as part of their movement during their turn.
+ When a creature falls or goes prone, they need to use half of their walking speed to get up.
+ A prone creature has quarter cover.
+ Attacking a prone creature grants a +1 bonus to precision rolls when adjacent to that creature. This also includes projectile attacks. 
+ A prone creature can only do basic weapon attacks. These attacks deal half damage after armor and ignore weapon precision.
+ When a flying creature is immobilized, or falls prone, it loses up to 3 meters of altitude and takes 5 armor-ignoring damage if it collides with the ground or an object.

### Fall Damage
A character takes fall damage when they fall more than 4 meters. This damage is armor-ignoring and it is calculated as such:
$10 \times (\text{fall distance in meters} - 4)$

### Ambushes
When the party ambushes or gets ambushed by one or more foes, the ambushed side is considered disadvantageous and they receive the following effects for the next round of combat:
+ -2 penalty to movement speed, down to a minimum of 1 meter
+ -1 penalty to all precision rolls by this creature
+ +1 bonus to all precision rolls against this creature

---
## Advanced Rules of Combat
### Light and Visibility 
Combat in darker areas such as at night or in a dark room is more difficult due to low visibility. There are three degrees of darkness: bright, moonlight and dark. 
- "Brightly lit" is the normal visibility.
- "Moonlit" is equivalent to fighting in nighttime. 
- "Darkness" is equivalent to being in a cave without a torch.

When a creature or an object's visibility is "moonlit", it is under quarter cover and the line of sight to it breaks after a distance of 5 meters. Similarly, if its visibility is "in darkness", it has half cover and the line of sight to it breaks after 1 meter. Your own visibility level does not affect you in any way. 

In most cases, instead of determining each creature's visibility one by one, it is inherited from the area and time of day: during nighttime, all creatures and objects are moonlit if they are fighting outside without any light sources. 

### Mounted Combat
A creature can ride a suitable mount during or outside combat. While mounted, the following rules apply:
* A creature can get on an adjacent mount as an action, and can dismount as an action. Getting on a mount who is not familiar with the rider requires a Riding skill roll. The success threshold is different for each type of mount and how a mount becomes familiar with a creature is also determined by the mount's type.
* If the rider or the mount falls prone, it is forcibly dismounted, falling to an adjacent square of their choosing. The rider takes 5 armor-ignoring damage as fall damage, and both the rider and the mount are prone.
* Health, status effects, and similar values are handled separately for the rider and the mount. However, only the rider's movement speed is used to determine turn order.
* The mount uses its movement as the rider's move: when the rider would move, the mount moves for them using its movement speed, carrying the rider with it. The rider's move otherwise works as normal. A rider cannot run while mounted.
* To make the mount run, or to have it take an action, a minor action, or a full-turn action, the rider can use the *speak* common action to command it. Some mount actions commanded this way may require a Riding skill roll.
* An ability that affects the ground can only affect the mount. For any other targeted or non-targeted ability, the attacker chooses whether to target the mount or the rider.
* Most mounts treat stairs and similar features as light rough terrain, since such features are built mainly for bipedal creatures. Depending on a mount's body shape, certain surfaces or materials may be impossible for it to walk on at all. 

### Summoning
+ Summoner can control their minions during combat. Normally, a summoner can control only one minion unless that minion does not count toward the summon limit. In case the summoner wants a second minion, they can choose which minion to keep when summoning a new one.
+ A minion disappears immediately when its summoner dies. 
+ Summoners have a simple telepathic bond to their minions. A summoner will know where a minion is and how much damage it suffered at all times. 
+ The minions follow the regular turn order. On a turn a minion is summoned, if they have higher movement speed than their summoner, they take their turn immediately after the summoner.
+ Minions gain potency bonus to their damage normally unless specified otherwise, according to their relevant potency stat.
+ Minions don't use energy for their skills, unless specified otherwise.

### Transforming
When a creature transforms into another, several rules should be followed:
+ A creature can only use the abilities of what it transformed into, and its stats are set to the stats of the new form. Status effects or abilities with durations are unaffected by transforming. 
+ When returning to the original form, a creature's health is set to what it was before the transformation. Going below 0 health does not break the transformation. See: [[Character Creation#Death|death]].
+ If a creature is unwillingly transformed during its own turn, this turn immediately ends.
+ If the new form cannot physically fit within the environment, the creature takes 5 armor-ignoring damage and the transformation fails.

### Player versus Player
Conflicts between player characters should be resolved with words. However, sometimes arguments might escalate into fights, duels or even ambushes. In this case, rather than starting a combat encounter, the GM may opt to use the simple method of PvP instead:
1. Players split into teams or stay neutral.
2. Each team rolls a (1d10) per player. The team that rolls the highest in total wins.
3. The GM may grant up to a +2 bonus to a team’s total if it has a clear situational advantage aside from numbers.

---
## Quick Reference Guide
Unless specified otherwise, values in the formulas below and in ability descriptions are always rounded down. 

| Explanation                                                                                                                                   | Formula                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Turn order tiebreak formula, e.g. member of the team that rolled higher goes earlier than member of another team with the same movement speed | $\text{2d10}$                                                                                            |
| Precision roll formula                                                                                                                        | $\text{1d10} + \frac{\text{level}}{2} + \text{weapon precision} + \text{other bonuses}$                  |
| Dealing damage, including status effects                                                                                                      | $\text{Action damage} + \text{Potency} + \text{other bonuses} - \text{target's armor (when applicable)}$ |
| Fall damage                                                                                                                                   | $10 \times (\text{fall distance in meters} - 4)$                                                         |
| Skill roll (normal skill)                                                                                                                     | $\text{1d10} + \frac{\text{Control}}{2} + \text{other bonuses}$                                          |
| Skill roll (major skill)                                                                                                                      | $\text{2d10} + \frac{\text{Control}}{2} + \text{other bonuses}$                                          |
