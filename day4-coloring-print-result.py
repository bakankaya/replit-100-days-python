print("Welcome to your Adventure Story Simulator.")
print ()
print("I am going to ask you a bunch of questions and then create an epic story with you as the star.")

print()
name = input("What is your name? ")
print()
enemyName = input("What is your enemy's name? ")
print()
superPower = input("What is your super power? ")
print()
live = input("Where do you live?")
print()
food = input("What is your favorite food?")

print()
print("Hello", "\033[30m", name,"\033[0m", "Your ability to","\033[37m", superPower,"\033[0m", "will make sure you never have to look at", "\033[31m", enemyName, "\033[0m", enemyName, "again." "Go eat", food, "as you walk down the streets of", live, "and use", superPower, "for good and not evil!")

# "\033[0m" a code like this will give color to your print command.
#Color	Value
#Default	0
#Black	30
#Red	31
#Green	32
#Yellow	33
#Blue	34
#Purple	35
#Cyan	36
#White	37