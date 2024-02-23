def palindrome(str):
    clean_str=str.replace(" ","").lower()
    rev_str=clean_str[::-1]
    return clean_str==rev_str

str=input("Enter the strings :")
if(palindrome(str)):
   print("palindrome")
else:
    print("not palindrome")    