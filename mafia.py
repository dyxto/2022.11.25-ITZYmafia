import random
from time import sleep


def TYPED_OUT(text,textspeed):
    for i in text:
        print(i,end="")
        sleep(textspeed)
    sleep(1)
    print("\n")

print("\n-------------------------------------------\n")

itzy_members=["yeji","lia","ryujin","chaeryeong","yuna"]

print("ITZY's members:",*itzy_members)

# for x in itzy_members:
#     print(x, end="")
#     sleep(.2)


mafia=random.choice(itzy_members)

guess_who=input("\nWho is the MAFIA? : ")

print("You guessed :",guess_who)


while guess_who != mafia:
    guess_who=input("\nGUESS AGAIN : ")


print("")
for x in range(5):
        print(".",end="")
        sleep(.3)

print("\n")
print(mafia,"was the mafia!")

sleep(1)
print("\n")


text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
text1="abdcefu"

TYPED_OUT(text,.00625)

print("\n-------------------------------------------\n")