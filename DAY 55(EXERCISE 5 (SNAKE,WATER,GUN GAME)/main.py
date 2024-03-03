# for practice
# import random
# l=[1,2,3,4,5,6,7]
# print(random.choice(l))
# import random
# l=[1,2,3,4,5,6,7]
# print(random.sample(l,2))

# exercise
import random
a=["snake","water","gun"]
b=input(f"What you want to choose from {a}:")
c=["snake","water","gun"]
print(random.choice(c))
if (b==("snake") and random.choice(c)==("snake")):
    print("draw")
if (b==("snake") and random.choice(c)==("water")):
    print("you won")
if (b==("snake") and random.choice(c)==("gun")):
    print("you lost")
if (b==("water") and random.choice(c)==("snake")):
    print("you lost")
if (b==("water") and random.choice(c)==("water")):
    print("draw")
if (b==("water") and random.choice(c)==("gun")):
    print("you won")
if (b==("gun") and random.choice(c)==("snake")):
    print("you won")
if (b==("gun") and random.choice(c)==("water")):
    print("you lost")
if (b==("gun") and random.choice(c)==("gun")):
    print("draw")
