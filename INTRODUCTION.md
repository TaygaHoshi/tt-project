# Introduction
Sigil of Uchma is a work-in-progress fantasy tabletop role playing game based on medieval Central Asian mythologies. The name is a reference to historical usage of [Nazar amulets](https://en.wikipedia.org/wiki/Nazar_(amulet)), and it can be abbreviated simply as "Sigil".

The game is played with one game master (GM) and one or more players:
- The GM builds and runs the campaign, enforces the rules of the game, applies or creates resolution mechanics as necessary and controls the non-player characters (NPCs). 
- Each player controls a single player character (PC). Through their characters, players can explore the world, battle enemies, interact with NPCs, pursue and complete quests, find treasures and go on adventures.

Sigil is not ready for running campaigns yet. You are seeing the version: *v1-a10* (alpha)

# Features
**Fun, tactical and engaging turn-based combat**
Each character consists of many unique but balanced choices: weapons provide both active and passive abilities, techniques carry an impact while not being overpowered, and armors are strong. There are rarely any limitations: a Guide or a Sorcerer can wear any type of armor and wield all weapons without penalties.

During your adventures you might come across and fight against monsters such as charming snake-women, tickling sheep-men, elemental spirits as protectors of the nature or owl-vampires.

Furthermore, Sigil is a relatively simplified take on the more well-known tabletop games. There are not many calculations to slow turns down during combat. Most numbers like damage of a weapon can be calculated beforehand. With proper notes, turns can get fast.

**Soft mechanics and rules for role playing**
Sigil of Uchma includes various rules for exploration, inventory management, crafting, travelling, interactions with NPCs and other similar activities. Such activities have simple rules, and most of the moment-to-moment decision making outside combat is left to common sense and imagination.

---
# Quickstart Guides
While reading the full rules are recommended, this section can be used as a general overview and for quick reference during play.

## Creating a Player Character
Full rules: [[Player Characters]]

A guide on creating a level 1 character:
1. Find a character concept and create a fitting backstory.
2. Choose a Path: [[Path of Warriors|Warrior]], [[Path of Sorcerers|Sorcerer]], [[Path of Poets|Poet]] and [[Path of Guides|Guide]].
	1. Choose one technique among the available ones.
3. Choose a Branch: [[Wildbond]], [[Warwise]], [[Iconcraft]], [[Druid]].
	1. Choose one technique among the available ones.
4. Choose an [[Armor & Weapons#Armor|armor]] and [[Armor & Weapons#Weapon Sets|two sets of weapons]].
5. Choose the [[Player Characters#Resistances|resistances]] you want to focus on:
	1. Either one major (+2 bonus) resistance and a minor (+1 bonus) resistance, or
	2. three minor resistances (+1 bonus to each)
6. Spend your one aptitude point in either Potency or Control.
7. Choose two skills as your major skills.
8. Give a name to your character.

You can check out the [the character creation website](https://sigil-create.tyghsh.cc) after reading this section.

## Combat Rule Reference Guide 
Full rules: [[Combat]]

### Phases of Combat 
1. Setting up the battle map
2. Turn order tiebreak rolls (described in the [[INTRODUCTION#Formula Reference Guide|reference guide below]])
3. Determining ambush for the first round
4. Round start
	1. Start phase: Apply environmental effects if any.
	2. Action phase: Player characters and NPCs take their turns in movement speed order.
	3. End phase: death save rolls, leaving combat and fleeing.
5. End of round

### Taking a Turn
During your turn, you can do one of the sequences below:
1. You can move, take 1 action and 1 minor action. You can't break up your movement between your actions but you can move before or after your actions.
2. Move twice (run).
3. Take a full-turn action.

When using an ability that targets one or more hostile/unwilling creatures, roll a precision roll against your target(s)' resistances. If that precision roll is equal to or above that resistance, your attack hits. If this is a damaging ability, you can then use the damage formula to calculate the damage you dealt.

### Status Effects

| Status Effect            | Type         | Explanation                                                                                                                                                                |
| ------------------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Blinded                  | Debilitating | Line of Sight reduced to 1 meter and -5 penalty to precision rolls.                                                                                                        |
| Cracked Armor            | Debilitating | Armor is ineffective. Does not affect temporary armor.                                                                                                                     |
| Disoriented              | Debilitating | $1+\frac{\text{Potency}}{3}$ penalty to precision rolls.                                                                                                                   |
| Exposed                  | Debilitating | Whenever this creature takes damage from a weapon attack, it receives (3 + P/2) bonus damage.                                                                              |
| Fatigued                 | Debilitating | Reduces movement speed by 2 per stack, -2 penalty on precision rolls and all resistances per stack. Stacks up to 5.                                                        |
| Immobilized              | Debilitating | Movement speed is reduced to zero and -1 penalty to Evasion.                                                                                                               |
| Sickened                 | Debilitating | $1+\frac{\text{Potency}}{4}$ penalty to Constitution and whenever the creature receives a harmful status effect, one hit is spent immediately.                             |
| Slowed                   | Debilitating | $1+\frac{\text{Potency}}{4}$ penalty to Evasion and Movement speed is halved.                                                                                              |
| Soaked                   | Debilitating | Cancels burning, doubles the damage of frostbitten or electrified once.                                                                                                    |
| Stunned                  | Debilitating | Unable to take any actions or run, -2 penalty to Parry and Evasion.                                                                                                        |
| Weakened Defenses        | Debilitating | $1+\frac{\text{Potency}}{4}$ penalty to Parry.                                                                                                                             |
| Bleeding                 | Harmful      | 5 armor-ignoring damage.                                                                                                                                                   |
| Burning                  | Harmful      | 10 physical damage.                                                                                                                                                        |
| Electrified              | Harmful      | 10 magical damage.                                                                                                                                                         |
| Frostbitten              | Harmful      | 5 armor-ignoring damage and cancels burning.                                                                                                                               |
| Diseased                 | Harmful      | 5 armor-ignoring damage without potency bonus. Spreads to adjacent creatures at the end of turn with a duration of 1 hit.                                                  |
| Inspired                 | Supportive   | Once, choose one: +1 bonus to a precision roll, 1d4 bonus to one skill roll or 2d4 bonus to the damage of a basic weapon attack.                                           |
| Protected                | Supportive   | Halves incoming damage after armor once, excluding status effects.                                                                                                         |
| Predictive Foresight     | Supportive   | +1 bonus to the next precision roll.                                                                                                                                       |
| Protective Foresight     | Supportive   | +1 bonus to all resistances for the next precision roll against this creature.                                                                                             |
| Quickened                | Supportive   | Movement speed is increased by $2+\frac{\text{Potency}}{3}$ meters.                                                                                                        |
| Regeneration             | Supportive   | Heal for $2+\frac{\text{Potency}}{2}$.                                                                                                                                     |
| Surefooted               | Supportive   | Can't fall prone or be moved unwillingly.                                                                                                                                  |
| Temporary Health         | Supportive   | Increases health until the duration ends.                                                                                                                                  |
| Temporary Magical Armor  | Supportive   | Protects target against magical damage until it breaks or the duration ends, one point of temporary magical armor breaks for every point of magical damage reduced by it.  |
| Temporary Physical Armor | Supportive   | Protects target against physical damage until it breaks or the duration ends, one point of temporary magical armor breaks for every point of magical damage reduced by it. |

### Additional Rules of Combat

| Rule                 | Explanation                                                                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rough terrain        | Light rough terrain requires 2 meters of walking speed per meter walked. Heavy rough terrain requires 3 meters of walking speed per meter walked.                                                                       |
| Ambush               | When ambushed, a creature receives a -2 penalty to its movement speed (down to a minimum of 1 meter). It also receives a -1 penalty to its precision rolls, and precision rolls against that creature gains a +1 bonus. |
| Flanking             | A creature has two melee hostile creatures adjacent to it. +1 bonus to all precision rolls against that creature.                                                                                                       |
| Cover                | Affects precision rolls of projectile attacks. Quarter cover gives a -1 penalty, half cover gives a -2 penalty and full cover gives a -4 penalty. Does not stack.                                                       |
| Falling prone        | +1 bonus to precision rolls when targeting an adjacent prone creature. A prone creature has quarter cover, and it can use half of its walking speed to get up.                                                          |
| Attacking when prone | A prone creature can only do basic weapon attacks that deal half damage after armor and ignore weapon precision bonus.                                                                                                  |
| High ground bonus    | +1 bonus to precision rolls when attacking from above.                                                                                                                                                                  |
| Low ground penalty   | -1 penalty to precision rolls when attacking from below.                                                                                                                                                                |

## Formula Reference Guide

| Explanation                                                                                                                                   | Formula                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Turn order tiebreak formula, e.g. member of the team that rolled higher goes earlier than member of another team with the same movement speed | $\text{2d10}$                                                                                            |
| Precision roll formula                                                                                                                        | $\text{1d10} + \frac{\text{level}}{2} + \text{weapon precision} + \text{other bonuses}$                  |
| Dealing damage, including status effects                                                                                                      | $\text{Action damage} + \text{Potency} + \text{other bonuses} - \text{target's armor (when applicable)}$ |
| Fall damage                                                                                                                                   | $10 \times (\text{fall distance in meters} - 5)$                                                         |
| Death save rolls                                                                                                                              | $\text{1d10} + \frac{\text{level}}{2}$                                                                   |
| Death save success thresholds per round                                                                                                       | 1st round: 3<br>2nd round: 5<br>3rd round: 7<br>4th round: 9                                             |
| Skill roll (normal skill)                                                                                                                     | $\text{1d10} + \frac{\text{Control}}{2} + \text{other bonuses}$                                          |
| Skill roll (major skill)                                                                                                                      | $\text{2d10} + \frac{\text{Control}}{2} + \text{other bonuses}$                                          |


---
# Release Cycle
Sigil of Uchma is versioned using a simple release cycle consisting of the following stages:
1. Alpha (current)
2. Beta
3. Feature freeze
4. Full release

# Contact & Contributing
You can contact me through GitHub or Discord (*taygahoshi*). Sigil of Uchma is developed openly in [this GitHub repository](https://github.com/TaygaHoshi/tt-project). Contributors are welcome so feel free to reach out to me.