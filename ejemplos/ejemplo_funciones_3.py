'''def create_driver(name, age, bonus = 'Undefinied'):
    print("Name: ", name)
    print("Bonus: ", bonus)
    print("Age: ", age)

create_driver(age = 26, name = "C. Sainz")'''



def sum_numbers(num1, num2):
    result = num1 + num2
    return result


x = int(input("x = "))
y = int(input("y = "))

temp_result = sum_numbers(x, y)

result = temp_result - 2

print(result)
