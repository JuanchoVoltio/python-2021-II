import random

class RacingObject:
    name = ""
    bonus = []

    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus


class Driver(RacingObject):

    def __init__(self, name, bonus):
        super().__init__(name, bonus)


class Track(RacingObject):

    def __init__(self, name, bonus):
        super().__init__(name, bonus)


class RacingSimulator:

    bonus_time = {"engine":  0.4,
                  "chassis" : 0.6,
                  "aero": 0.5}

    def get_bonus_time(self, bonus_name):
        return bonus_time[bonus_name] 

    def simulate_driver_lap_time(self, driver, track):
        base_time = random.randint(1, 70)
        driver_time = base_time
        if driver.bonus in track.bonus:
            driver_time = base_time - self.get_bonus_time(driver.bonus)

        return driver_time


simulator = RacingSimulator()
driver_1 = Driver("C. Muñoz", "chassis")
track_1 = Track("Long Beach", ["chassis", "aero"])


time = simulator.simulate_driver_lap_time(driver_1, track_1)
print(time)
