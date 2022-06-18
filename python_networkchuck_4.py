#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot Barista!!



#print("Hello, welcome to NetworkChuck Coffee!!!!!!!!!!!!!!")


#name = input("What is your name?\n")

#if name == "Ben":
#  print("You're not welcome here Evil Ben!! Get Out!!")
#else:
 # print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

#if 2 > 3:
 # print("Yep, true")
  #print("Still true")
#else:
 # print("Nope")

# me == "NetworkChuck"

#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot Barista!!

#Greet your customer

print("Hello, welcome to NetworkChuck Coffee!!!!!!!!!!!!!!")

#Ask your customer what their name is with the input() function and store that in the variable NAME.
name = input("What is your name?\n")

#Greet the customer with their name and thank them for coming in today using concatenation.

if name == "Ben":
  print("You're not welcome here Ben!! Get out!!")
  exit()
else:
  print("Hello " + name + ", thank you so much for coming in today.\n\n\n")



#Coffee menu
menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

#Ask the customer what they would like from the menu and store it in the variable order.
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

#Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")

price = 8

#Calculate the customer's total
total = price * int(quantity)

#Give the customer their total
print("Thank you. Your total is: $" + str(total))

#Final statement
print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")
