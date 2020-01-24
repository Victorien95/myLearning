import random
import threading
import time
import sys
from threading import Event



class Personnage:
    def __init__(self, level, stamina, name):
        self.name = name
        self._hp = 10
        self.hp_max = 10
        self.accuracy = 70
        self.armor = 50
        self.dmg_min = 50
        self.dmg_max = 100
        self.pierce_armor = 1
        self._stamina = stamina
        self.stamina_max = 5
        self._xp = 0
        self.level = level
        self.skill_points = 0
        self.xp_for_level = 100
#  88888888888888888888888888888888888888888888888
        self.critical_luck = 1
        self.xp_multiplier = 1
        self.stamina_regen = 1

    def _get_hp(self):
        return self._hp

    def _set_hp(self, modificator):
        self._hp += modificator
        if self._hp < 0:
            self._hp = 0
        elif self._hp > self.hp_max:
            self._hp = self.hp_max

    hp = property(_get_hp, _set_hp)

    def _get_stamina(self):
        return self._stamina

    def _set_stamina(self, modificator):
        self._stamina += modificator
        if self._stamina >= self.stamina_max:
            self._stamina = self.stamina_max

    stamina = property(_get_stamina, _set_stamina)

    def _get_xp(self):
        return self._xp

    def _set_xp(self, modificator):
        self._xp += modificator
        if self._xp >= self.xp_for_level:
            self.skill_points += 5
            self._xp -= self.xp_for_level
            self.xp_for_level = self.xp_for_level(1.15)

    xp = property(_get_xp, _set_xp)

    def accuacy_roll(self):
        roll = random.randint(0, 100)
        if roll <= self.accuracy:
            return True
        else:
            return False

    def dmg_roll(self):
        roll = random.randint(self.dmg_min, self.dmg_max)
        return roll

    def dmg_after_armor_reduc(self, target):
        dmg_roll = self.dmg_roll()
        prct_reduc = target.armor * 0.5
        if prct_reduc > 50:
            prct_reduc = 50
        dmg_after_armor_reduc = dmg_roll - target.armor
        dmg_after_armor_reduc -= round(prct_reduc / 100, 0) * dmg_after_armor_reduc
        if dmg_after_armor_reduc < 1:
            dmg_after_armor_reduc = 1
            return -dmg_after_armor_reduc  # Negatif car ce sont des degats
        else:
            return -dmg_after_armor_reduc

    def attack(self, target):
        if self.accuacy_roll():
            print('Hit')
            target.hp = self.dmg_after_armor_reduc(target)
        else:
            print('Miss')

    def heal(self, target):
        if self.stamina == 0 or self.hp == 0:
            return False
        else:
            self.hp += 5
            print("VIC SE HEAL DE 5 HP")

    def experience(self, target):
        self.xp += target.xp * (5/100)

# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
    def hp_up(self):
        self.hp_max = self.hp_max + 5
        self.hp = self.hp_max
        self.skill_points -= 1

    def armor_up(self):
        self.armor = self.armor + 1
        self.skill_points -= 1

    def accuracy_up(self):
        self.accuracy = self.accuracy + 5
        self.skill_points -= 1

    def pierce_armor_up(self):
        self.pierce_armor = self.pierce_armor + 5
        self.skill_points -= 1

    def dmg_max(self):
        self.dmg_max = self.dmg_max + 4
        self.skill_points -= 1

    def dmg_min_up(self):
        self.dmg_min = self.dmg_min + 3
        self.skill_points -= 1

    def stamina_max_up(self):
        self.stamina_max = self.stamina_max + 5
        self.stamina = self.stamina_max
        self.skill_points -= 1

    def stamina_regen_up(self):
        self.stamina_regen = self.stamina_regen + 1
        self.skill_points -= 1

    def xp_multiplier_up(self):
        self.xp_multiplier = self.xp_multiplier + 1
        self.skill_points -= 1


# 888888888 thread test 8888888888888888888888

class StaminaRegen(threading.Thread):
    def __init__(self, hero, timer):
        threading.Thread.__init__(self)
        self.timer = timer
        self.hero = hero

    def run(self):
        temp = ''
        timer = self.timer
        while True:
            self.hero.stamina = 1
            temp = str(self.hero.stamina)
            sys.stdout.write(temp + ' ' + self.hero.name)
            sys.stdout.flush()
            time.sleep(timer)


# ______________________________________________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________________________________________


"""alex = Personnage(1)
vic = Personnage(1)
print(vic.hp)


alex.attack(vic)
print(vic.hp, "HP DE VIC")
vic.heal(vic)
print(vic.hp, "HP APRES HEAL")"""

vic = Personnage(1, 1, ' Vic ')

test = StaminaRegen(vic, 1)

test.start()
test.wait()



