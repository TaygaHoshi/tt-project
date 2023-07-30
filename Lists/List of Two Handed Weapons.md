(see: [[Weapons]])

# Two-handed
Two-handed weapons have three weapon attacks. All weapon attacks tagged (Prepared) are prepared actions.

```two_handed
weapon           |  damage  | precision | range | armor piercing
glaive           |    32    |     0     |  2m   |  -
spear            |    28    |     1     |  2m   |  -
two-handed sword |    28    |     1     |  1m   |  -
war hammer       |    28    |     0     |  1m   | 50%
occultic staff   |    24    |     0     | 10m   |  -
divine staff     |    24    |     0     | 10m   |  -
longbow          |    24    |     0     | 15m   |  -
crossbow         |    24    |     1     | 15m   | 50%
shortbow         |    20    |     1     | 10m   |  -
war drums        |     -    |     1     | 10m   |  -
```

## Glaive
+ Aptitude: Strength
+ Slash
	+ Range: 2 meters.
	+ Deals 32 damage.
+ Wide Slash
	+ This attack's precision rolls are made against Evasion.
	+ Ignores weapon precision.
	+ Deals 16 damage. Potency bonus to damage is doubled for this attack. 
	+ Hits all creatures in 8 squares in a cone shape in front of you.
+ (Prepared) Opportunistic Slash
	+ Range: 2 meters.
	+ Choose a target. 
	+ Attack this target next time they attack or cast a spell within range.
	+ Deals 16 damage. Potency bonus to damage is doubled for this attack. 

## Spear
+ Aptitude: Strength
+ Thrust
	+ Range: 2 meters.
	+ Deals 28 damage.
+ Keep At Bay
	+ Range: 2 meters.
	+ Deals 14 damage. Potency bonus to damage is doubled for this attack. 
	+ Target is pushed (2 + POW/4) meters away from you.
+ (Prepared) Opportunistic Thrust
	+ Range: 2 meters.
	+ Ignores weapon precision.
	+ Choose a target. 
	+ Attack this target next time they move into or out of range.
	+ Deals 14 damage. Potency bonus to damage is doubled for this attack. 

## Two-handed Sword
+ Aptitude: Strength
+ Slash
	+ Deals 28 damage.
+ Attack 2
	+ #TODO 
+ (Prepared) Defensive Stance
	+ You have a (1 + POW/4) bonus to Parry against the next physical attack.

## War Hammer
+ Aptitude: Strength
+ Smash
	+ Deals 28 damage.
	+ Pierces 50% armor.
+ Momentum Swing
	+ This attack's precision rolls are made against Evasion.
	+ Deals 14 damage. 
	+ Hits all creatures within range, stunning the creatures you hit for 1 round.
+ (Prepared) Blind Swing
	+ This attack's precision roll is made against Evasion.
	+ Ignores weapon precision.
	+ Attack any creature, including allies, who moves into or out of range.

## Nature Staff
+ Aptitude: Witchcraft
+ (Projectile) Elemental Bolt
	+ Range: 10 meters
	+ Deals 24 damage. 
+ Vine Growth
	+ This attack's precision roll is made against Evasion.
	+ Ignores weapon precision.
	+ Hardened vines grow from the tip of your staff, hitting all creatures on 3 squares in a line in front of you. 
	+ Deals 12 damage. Potency bonus to damage is doubled for this attack.
+ (Prepared) Staff Strike
	+ Range: 2 meters.
	+ Ignores weapon precision.
	+ Choose a target. 
	+ Attack this target next time they move into or out of range.
	+ Deals 10 physical damage.

## Divine Staff
+ Aptitude: Divine
+ (Projectile) Arrow of Light
	+ Range: 10 meters
	+ Deals 24 damage. 
+ Projectile Shielding
	+ Range: 5 meters
	+ Choose a 1 meter square area. You create a magical shield there.
	+ This ward acts like quarter cover against projectiles passing through it.
	+ This ward lasts for one round.
+ (Prepared) Warding
	+ You have a (1 + WRA/4) bonus to Faith, Willpower and Reflection against the next magical attack.

## Longbow
+ Aptitude: Strength
+ (Projectile) Shoot
	+ Range: 15 meters
	+ Receives a -1 penalty to precision rolls against targets within 5 meters.
	+ Deals 24 damage.
+ (Projectile) Dual Shot
	+ Range: 15 meters
	+ This attack's precision rolls are made against Evasion.
	+ Receives a -1 penalty to precision rolls against targets within 5 meters.
	+ You shoot an arrow each to two targets adjacent to each other within range.
	+ These arrows each deal 12 damage. Potency bonus to damage is doubled for these attacks. 
+ (Prepared) (Projectile) Half-drawn Shot
	+ Ignores weapon precision.
	+ Choose a target. 
	+ Shoot this target next time they move into or out of a radius of 5 meters, dealing 12 damage.

## Crossbow
+ Aptitude: Strength
+ (Projectile) Shoot
	+ Range: 15 meters.
	+ Ignores weapon precision against targets within 5 meters.
	+ Deals 24 damage.
	+ Pierces 50% armor.
+ (Projectile) Pinning Shot
	+ Range: 15 meters.
	+ Ignores weapon precision against targets within 5 meters.
	+ This attack's precision roll is made against Constitution.
	+ Deals 12 damage. Potency bonus to damage is doubled for this attack. 
	+ Slows the target for (1 + POW/4) rounds.
+ (Prepared) (Projectile) Crossbow Bash
	+ Range: 2 meters.
	+ Ignores weapon damage and precision.
	+ Next time a foe within range attempts to attack or cast a spell, it is interrupted and their action fails.

## Shortbow
+ Aptitude: Strength
+ (Projectile) Shoot
	+ Range: 10 meters.
	+ Deals 20 damage.
+ (Projectile) Shoot Vitals
	+ Range: 10 meters.
	+ This attack's precision roll is made against Constitution.
	+ Ignores weapon damage.
	+ Applies (3 + POW/4) turns of bleeding on hit.
+ (Prepared) (Projectile) Disrupting Shot
	+ Range: 5 meters.
	+ Ignores weapon damage and precision.
	+ Choose a target. 
	+ When this target attempts to attack with a weapon within range, they are interrupted on hit, and their action fails.

## War Drums
+ Aptitude: Social
+ Allies who are unable to hear are not affected by war drums. 
+ (Rapid Action) Beat of Swords
	+ Radius: 10 meters.
	+ All other allies within range gain a 5 bonus damage until your next turn. Potency bonus to damage is halved for this ability.
	+ This bonus doesn't affect damaging status effects such as bleeding and burning.
	+ This bonus doesn't affect lingering area effects such as Dissonance.
	+ Being stunned, falling or going prone, diving under water or becoming unavailable to cast spells in any way stops the bonuses granted by this weapon attack.
+ (Rapid Action) Beat of Shields
	+ All other allies within range gain (5 + EXP/2) temporary physical armor and temporary magical armor until your next turn.
	+ Being stunned, falling or going prone, diving under water or becoming unavailable to cast spells in any way stops the bonuses granted by this weapon attack.
	+ Does not stack.
+ (Rapid Action) Beat of Haste
    + All allies within range gain (1 + EXP/2) bonus to movement speed until your next turn.
    + Being stunned, falling or going prone, diving under water or becoming unavailable to cast spells in any way stops the bonuses granted by this weapon attack.
    + Does not stack.
