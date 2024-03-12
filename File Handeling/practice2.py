#from a file containing numbers seperated by comma, print the count of even numbers.

with open("practice.txt","r") as f:
    data=f.read()
    print(data)
    
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            if(int(num)%2==0):
                print(num)
                num=""
        else: 
            num+=data[i]
        