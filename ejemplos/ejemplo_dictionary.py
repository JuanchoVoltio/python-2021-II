my_dict = {'a':10, 'b':23, 4:-5, 'z':True}

print(my_dict)
print(my_dict.get('z'))

print('=' * 4)

for current_key in my_dict:
    #print(type(current_key))
    print(my_dict.get(current_key))

print('=' * 4)

for current_value in my_dict.values():
    print(current_value)

print('=' * 4)

for curr_key, curr_value in my_dict.items():
    print(curr_key, " - ", curr_value)
    
