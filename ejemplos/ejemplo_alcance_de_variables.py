a = 100

def f_A():
    global a
    a = 200
    print(a)

def f_B():
    a = 150
    print(a)



f_A()
f_B()
print(a)

