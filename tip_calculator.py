"""
Write a program that receives the following inputs from the user:
    the server's name
    how much the meal cost
    the tax rate as a floating point (e.g. 6.5)
    the tip percent as an integer (e.g. 15 or 20)
Print out the following results:
    The amount to tip
    The total amount for the meal
    A thank you for the server
"""

print ('Hello, what is your server\'s name? ')
name = input()


while True:
    try:
        print("How much did your meal cost?")
        cost = float(input())
        break
    except:
        print("\nThat is not a valid number\n")

if cost < 5:
    print("How was lunch at McDonalds?\n")
elif cost < 10:
    print("So you don't eat fast food.\n")
elif cost > 700000:
    print("Ummmm, can you give ME that much money? Where'd you even go for that cost? Mortgage? A billion starving mice could have been fed with that money!\n")
elif cost > 100:
    print("When you realize all that store's profits go to charity. And you don't like giving to charity.\n")


while True:
    try:
        print("What percent will you tip?")
        tipInput = int(input())
        break
    except:
        print("\nThat is not a valid integer\n")





while True:
    try:
        print("\nAnd what is the tax percent?")
        taxInput = float(input())
        break
    except:
        print("\nYou have failed me for the last time!\n")


tax = cost*taxInput/100
tip = cost*tipInput/100
total = cost + tip + tax



print( "The tip amount is: $" + str(tip))
print("The total amount for my meal is: $" + str(total))
print ("Thanks for your service " + name)
