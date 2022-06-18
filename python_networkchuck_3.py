# Let's play with some numbers

name = "Zane"

age = 21

actual_age = 21.56

math = 5 * 7 - 6 ** 45

print(math)

results = age + actual_age + math

print(results)

print("\n\n\nHello, welcome to NetworkChuck Coffee!!!!!!!")

# print("What is your name?")

name = input("What is your name?\n")

print("Hello " + name + ", thank you so much for coming in today!\n\n\n" )

menu = ("black coffee, espresso, latte, cappucino")

print(name + ", What would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 8

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")

# price = 1

# amount_coffee = input("How many would you like? ")
# print("The total cost is " + price * amount_coffee + ".")
