# Variables
# Episode 2

#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!
# Let's make a robot barista

print("Hello, welcome to NetworkChuck Coffee!!!!!!!")

# print("What is your name?")

name = input("What is your name?\n")

print("Hello " + name + ", thank you so much for coming in today!" )


#CHALLENGE 1 ----> (timestamp 12:36)

#Program the robot barista to give the customer a menu, (make the menu a variabe) ask them what they want, and tell them it will be ready in a moment. Here is an example of the output:

menu = ("sandwich", "ramen", "potato")

print("Here is our menu")
print(menu)
food = input("What do you want " + name + "?\n")

print("I want " + food + " please!")

print("Sounds good " + name + "! We'll have that coffee_beverage ready for you in a moment!!")

print("\n\n\nHello, welcome to NetworkChuck Coffee!!!!!!!")

# print("What is your name?")

name = input("What is your name?\n")

print("Hello " + name + ", thank you so much for coming in today!\n\n\n" )

menu = ("black coffee, espresso, latte, cappucino")

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

print("Sounds good " + name + ", we'll have that " + order + " ready for you in a moment.")
