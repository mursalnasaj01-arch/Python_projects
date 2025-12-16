#Random Number Generator
import random
low_num=int(input("enter the lower bound: "))
high_num=int(input("enter the upper bound: "))

random_num=random.randint(low_num,high_num)
print(f"Random number between {low_num} and {high_num} is: {random_num}")