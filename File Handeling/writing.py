f=open("demo.txt","w")

#write mode
f.write("this is new line")     #overwites the entire file

f.close()

f1=open("demo.txt","a")
f1.write("this is appended text")

f1.close()       #this is appended text