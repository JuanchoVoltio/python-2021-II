import random
import racing_module as r_m
import mario_kart_base_data as mk_base

class Character(r_m.RacingObject):

    def __init__(self, name, bonus):
        super().__init__(name, bonus)


class Track(r_m.RacingObject):

    def __init__(self, name, bonus):
        super().__init__(name, bonus)


class RacingSimulator:
    

    def use_red_shell(self, character1, character2):
        print(character1.name, "hits", character2.name, "with a red shell")


simulator = RacingSimulator()        
mario = Character(mk_base.mario, "3 stars")
bowser = Character(mk_base.bowser, "5 stars")
vanilla_plains = Track("Vanilla Plains", "4 stars")

simulator.use_red_shell(mario, bowser)

