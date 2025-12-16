#Count Vowels in a string

text=input("enter a string: ")
Vowels="eoiuaAUIOE"
total=0

for char in text:
    if char in Vowels:
        total+=1
print(f"the number of Vowels in {text} is: {total}")        