#printing from N to 1

def printNto1(n):
    if(n==0):
        return
    print(n)
    printNto1(n-1)
    
n=int(input("enter the number :"))
printNto1(n)