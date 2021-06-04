my_set = {30, 10, 50, 45, 21, 13}
another_set = {10, 90, 45, "bla"}
number = 21
counter = 0

print("before: ", my_set, "\t", another_set)

'''my_set.add(80)
my_set.add(50)
my_set.add("76")'''

print("meanwhile: ", my_set, "\t", another_set)

#my_set.discard(number)

'''for current in my_set:
    counter += 1
    if number == current:
        print("I found the number (", number, "). I iterate ", counter, " times.")
        my_set.remove(number)
        print("\tRemoved element: ", number)
        break'''

#my_set.pop()    

print("\nafter union: ", my_set.union(another_set))
print("after intersection: ", my_set.intersection(another_set))
print("after difference: ", my_set.difference(another_set))
print("after symmetric difference: ", my_set.symmetric_difference(another_set))
