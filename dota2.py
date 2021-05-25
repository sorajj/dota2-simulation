from math import fabs
from random import randint

class Unit:
    strengh = 0
    agility = 0
    inteligy = 0
    atack_misses = 0
    health = 100
    movement_speed = None
    turn_speed = None
    mana_pool = None
    armour = None
    atack_speed = None
    atack_damage = None
    attack_range = None
    magic_resistance = None


    def __init__(self,name, side):
        self.name = name
        self.side = side




    def show_info(self):
        print('''
        {namee}         {side}
Health                           {hlth}
Mana                             {mana}
Armour                           {arm}
Magic resistance                 {mag_res}
Attack damage                    {at_dam} 
Attack range                     {at_rg}
Movement speed                   {m_s}
Strength                         {stra}
Agility                          {agil}
Intelligence                     {intel}
'''.format(side=self.side, hlth=self.health, mana=self.mana_pool,
           arm=self.armour, mag_res=self.magic_resistance, at_dam=self.atack_damage,
           at_rg=self.attack_range, m_s=self.movement_speed, namee=self.name, stra=self.strengh,
           agil=self.agility, intel=self.inteligy))


class UnitNeutralCreep(Unit):
    def __init__(self, name, side, atack_type, health, mana_pool, armour, movement_speed, atack_damage, atack_range, magic_resistance, spell_dmg, strenght, agility, intelligence):
        Unit.__init__(self, name, side)
        self.atack_type = atack_type
        self.health = health
        self.mana_pool = mana_pool
        self.armour = armour
        self.movement_speed = movement_speed
        self.atack_damage = atack_damage
        self.attack_range = atack_range
        self.magic_resistance = magic_resistance
        self.spell_dmg = spell_dmg
        self.strengh = strenght
        self.agility = agility
        self.inteligy = intelligence

    def hit(self, target):
        arm_formul = 1 - (0.06 * target.armour) / (0.9+0.06 * fabs(target.armour))
        atc_dmg = randint(self.atack_damage[0], self.atack_damage[1])
        reduced = atc_dmg - int((atc_dmg * arm_formul))
        dmg_done = atc_dmg - reduced
        target.health -= int((atc_dmg * arm_formul))
        print("""\ract_dmg   =  {0}
        \rdmg_dome  =  {1}
        \rreduced   =  {2}
        """.format(atc_dmg, dmg_done, reduced))

    def use_spell(self, target):
        if target.magic_resistance != 0:
            mag_dmg_after_reduce = self.spell_dmg *(1-target.magic_resistance)*(1-target.strengh*0.0008)
            target.health -= mag_dmg_after_reduce
            print('\nmag dmg after reduce =', int(mag_dmg_after_reduce))
        else:
            target.health -= self.spell_dmg
            print('\nmag dmg after reduce =', self.spell_dmg)

class UnitHeroAxe(Unit):
    strengh = 25
    agility = 20
    inteligy = 18
    atack_misses = 25
    health = 200 +(strengh*20)
    movement_speed = 310
    turn_speed = 0.6
    mana_pool = 75+(inteligy*12)
    armour = 2.33
    atack_speed = 150
    atack_damage = [27,31]
    attack_range = 150
    magic_resistance = 0.25

    def __init__(self, name, side):
        Unit.__init__(self, name, side)

    def hit(self, target):
        arm_formul = 1 - (0.06 * target.armour) / (0.9+0.06 * fabs(target.armour))
        atc_dmg = randint(self.atack_damage[0], self.atack_damage[1]) + self.strengh
        reduced = atc_dmg - int((atc_dmg * arm_formul))
        dmg_done = atc_dmg - reduced
        target.health -= int((atc_dmg * arm_formul))
        print("""\ract_dmg   =  {0}
        \rdmg_dome  =  {1}
        \rreduced   =  {2}
        """.format(atc_dmg, dmg_done, reduced))




# Creating units
axe = UnitHeroAxe('Axe', 'Dire')

dire_observer_ward = Unit('observer ward', 'dire')

centaur_neutral_creep = UnitNeutralCreep('Centaur', 'Jungle creep', 'Meele', 1100, 200, 4, 320, [49, 55], 100, 0, 75, 'none', 'none', 'none')

harpy = UnitNeutralCreep('Harpy', 'Jungle creep', "Range", 550, 125, 2, 310, [30, 37], 450, 0, 140, 'none', 'none', 'none')

# Checking unit's info
axe.show_info()
harpy.show_info()
centaur_neutral_creep.show_info()
dire_observer_ward.show_info()

# Testing hitting and using spells
# Axe hit Centaur
print('\nAxe hit Centaur')
axe.hit(centaur_neutral_creep)
# Axe hit Harpy
print('\nAxe hit harpy')
axe.hit(harpy)

# Harpy hitting Axe 3 times and then use her spell
# 1st action
print('\n{} have {}hp'.format(axe.name ,axe.health))

print('\nHarpy 1st time hitting Axe\n')
harpy.hit(axe)
print('\n{} has {}hp'.format(axe.name ,axe.health))

# 2nd action
print('\nHarpy 2nd time hitting  Axe\n')
harpy.hit(axe)
print('\n{} has {}hp'.format(axe.name ,axe.health))

# 3rd action
print('\nHarpy 3rd time hitting  Axe\n')
harpy.hit(axe)
print('\n{} has {}hp'.format(axe.name ,axe.health))

#  Harpy use spell on Axe
print('\nHarpy use spell on Axe (spells damage = 140)')
harpy.use_spell(axe)
print('{} has {}hp'.format(axe.name ,int(axe.health)))

# Harpy hit cent
print('\nHapry hit Centaur')
harpy.hit(centaur_neutral_creep)

# Harpy use spell on Centaur
print('Harpy use spell on Centaur (cent has 0 magic resistance)', end='')
harpy.use_spell(centaur_neutral_creep)

# Centaur hitting axe
print('Cent hit Axe')
centaur_neutral_creep.hit(axe)

# Centaur hitting Harpy
print('Cent hit Harpy')
centaur_neutral_creep.hit(harpy)







