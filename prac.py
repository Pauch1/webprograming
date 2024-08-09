
       



def build(x, y = 1):
    if x == 0:
        return
    else:
        for i in range(y):
            print("#",end='')
        print("")
        
        build(x-1, y + 1)
        
y = build(5)
print(y)