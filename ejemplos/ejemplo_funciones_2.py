def add_new_driver(driver_list, **new_driver):
    name = new_driver['name']
    bonus = new_driver['bonus']
    driver_list[name] = bonus
#End of add_new_driver()


drivers = {"Kobayashi" : "aero"}


add_new_driver(drivers, name = "S. Perez", bonus = "aero")
print(drivers)

add_new_driver(drivers, name = "J. P. Montoya", bonus = "chassis")
print(drivers)
