import random
import racing_module as r_m

class Driver(r_m.RacingObject):

    def __init__(self, name, bonus):
        super().__init__(name, bonus)


class Track(r_m.RacingObject):

    def __init__(self, name, bonus):
        super().__init__(name, bonus)


class RacingSimulator:

    bonus_time = {"engine":  0.4,
                  "chassis" : 0.6,
                  "aero": 0.5}
    

    def simulate_driver_lap_time(self, driver, track):
        base_time = random.randint(60, 70)
        driver_time = base_time
        if driver.bonus in track.bonus:
            driver_time = base_time - self.bonus_time[driver.bonus]

        return driver_time

    def print_lap_time_simulation(self, driver, track):
        message_template = "[TIME] Driver {0}: {1} sec."
        time = self.simulate_driver_lap_time(driver, track)

        print(message_template.format(driver.name, time))

        

simulator = RacingSimulator()
driver_1 = Driver("C. Muñoz", "chassis")
driver_2 = Driver("K. Kobayashi", "engine")
track_1 = Track("Long Beach", ["chassis", "aero"])

simulator.print_lap_time_simulation(driver_1, track_1)

print(r_m.print_message())
