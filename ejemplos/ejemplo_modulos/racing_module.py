default_track_name = "Unknown track"

def print_message():
    print("This message is from a funcion in another module")

    
class RacingObject:
    name = ""
    bonus = []

    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
