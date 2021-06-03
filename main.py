# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random


total_person=len(names)
who = random.randint(0,total_person-1)
print(f"{names[who]} is gonna to pay the bill")


