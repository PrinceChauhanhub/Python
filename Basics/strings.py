name1='prince'

name2="india"

#multiline string
name3='''this is 
india'''

print(name1,name2,name3)

#type of datatype
print(type(name1))
print(type(name2))
print(type(name3))

#indexing in a string
print(name1[0])
print(name1[4])

#negative indexing in a string
print(name1[-1])
print(name1[-4])

#traversing a list
for i in name1:
    print(i,end="")

#length of string
print("/n")
print(len(name1))

#find a char / substrig in a string  //returns the index of first occurence of character or substring
print(name1.find('in'))

#slicing from any index
print(name1[1:3])

#slicing from start
print(name1[:4])

#create new string using old string

#converting to uppper case
str1="new york"
str2=str1.upper()
print(str2)

#conerting to lower case
str3=str2.lower()
print(str3)

#for captalizing first character of the string
str4=str3.capitalize()
print(str4)

#for stripping/removing any trailing whitspaces
str5="          hello world       "
print(str5.strip())
print(str5)

#replace old substring with new substring 
#syntax: sting.replace(old_substring,new_substring,count)

str6="Hello World,What a good day in this World"
print(str6.replace("World","Earth"))
print(str6.replace("World","Earth",1))

#splitting strings
str7="ria,pia,sia,mia"
list=str7.split(",",2)
print(list)

str8="apple mango banana"
list1=str8.split()
print(list1)

#concatenation
str9="Hello World"
str10=" great place"
print(str9+str10)

#Format function
name="prince"
marks="100"

str11="The Student name is {s}, and marks is {t}".format(s=name,t=marks)
print(str11)