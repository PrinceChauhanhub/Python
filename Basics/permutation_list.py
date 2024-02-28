x = int(input("enter x:"))
y = int(input("enter y:"))
z = int(input("enter z:"))

lst=[]
for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                    lst.append([i,j,k])
                    

print(lst)
   