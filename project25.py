#Anagrams Strings

text1=input("enter the first string: ")
text2=input("enter the second string: ")

if sorted(text1)==sorted(text2):
    print("The strings are Anagrams.")
else:
    print("The strings are not Anagrams.")    