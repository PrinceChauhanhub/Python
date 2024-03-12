f=open("P:\Python\File Handeling\demo.txt","r")

#reads a single line 
line2=f.readline()
print(line2)

#reads entire file
line1=f.read()
print(line1)


f.close()