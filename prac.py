def factorial(x):
    if x == 1:
        return 1
    else:
       return x * factorial(x-1)
       



def build(x):
    if x == 0:
        return False
    else:
        for i in range(x):
            print("#",end='')
        print("")
        build(x-1)
y = build(5)
print(y)