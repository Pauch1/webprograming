def main():    
    stair(5)
        
def stair(x, i = 0):
    if x == 0:
        return
    else:
        for a in range(i + 1):
            print('#', end="")
        print("")   
    stair(x - 1, i + 1)
            
main()