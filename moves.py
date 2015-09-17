"List of Moves:"

class Moves():
    entity = None
    accuracy = None

class Tackle(Move):
    accuracy = 100
    damage = 35


    def do(self,target):
       # self.applyBuffs()
       # self.applyDebuffs()
       rolled = dice.roll(1,100)
       if self.accuracy >= rolled:
           target.hp -= self.damage

class Growl(Move):
    pass

class Scratch(Move):
    pass
