#given string,number N,need to mirror chracter from nth position up to length of string in alphabetical order.
# in mirror option, we change 'a' to 'z' ,'b' to 'y' ans so on
 
input_string=input("Enter the string:")
n=int(input("enter n:"))

#creating dictionary for mirror operation
alphabets="abcdefghijklmnopqrstuvwxyz"
reverse=alphabets[::-1]
dict1 = dict(zip(alphabets,reverse))


#finding part of string on which we will do mirror operation
prefix=input_string[0:n-1]
suffix=input_string[n-1:]

#finding the mirror string
mirror=""
for i in range(0,len(suffix)):
    mirror=mirror + dict1[suffix[i]] 
    
#creating final string
res= prefix + mirror

print(res)