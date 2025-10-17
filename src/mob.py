import random
from item import Key

class Mob:
    """A Mob is the parent class for all PCs, NPCs, and Monsters.
    Any autonomous entity with stats is a Mob.
    """

    def __init__(self, strength, agility, stamina, smarts, wisdom, charisma):
        # Stats are defined by ability modifiers, not ability scores like in D&D.
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.smarts = smarts
        self.wisdom = wisdom
        self.charisma = charisma

        self.level = 1
        self.max_hp = self._calc_max_hp()
        self.hp = self.max_hp
        self.inventory = []

    def _calc_max_hp(self) -> int:
        return max(1, 6 + self.stamina + (self.level - 1) * 4)

    def heal(self, num):
        if num > 0:
            self.hp = min(self.hp + num, self.max_hp)

    def take_item(self, item):
        self.inventory.append(item)


class Player(Mob):

    def __init__(self):
        super().__init__(self._roll_stat(), self._roll_stat(), self._roll_stat(), self._roll_stat(), self._roll_stat(), self._roll_stat())

    def _roll_stat(self) -> int:
        """3d6, re-roll if <9, convert to ability score.
        Since that straightforward logic will cause unnecessary loops, 
        the function will choose a random ability score between [-1, 4]
        with each score weighed by the number of results when using the method above.
        """
        return random.choices(list(range(-1, 5)), [25, 54, 46, 25, 9, 1])[0]

    def get_keys(self) -> list:
        return [item for item in self.inventory if isinstance(item, Key)]
