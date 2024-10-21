import sys

print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

def menu():
    print("Option 1: Nachos")
    print("Option 2: Burritos")
    print("Option 3: Quesadilla")
    print("Option 4: Crunch-wrap")
    print("Option 5: Quit")

menu()

one = 4.00
two = 4.00
three = 4.00
four = 1.50
five = "Quit"

oneChoice = 4
twoChoice = 4
threeChoice = 4
fourChoice = 4

choice= input("Choose your option here, select the number from the items above: ")


if choice == "1":
    print("You have selected Nachos")
    print("The total so far is", oneChoice, "dollars")
elif choice == "2":
    print("You have selected Burritos")
    print("The total so far is", twoChoice, "dollars")
elif choice == "3":
    print("You have selected Quesadillas")
    print("The total so far is", threeChoice, "dollars")
elif choice == "4":
    print("You have selected Baja blast")
    print("The total so far is",fourChoice, "dollars")
elif choice == "5":
    print("You have selected exit, goodbye")
    sys.exit()


menu()


choiceTwo = input("Choose your second option here, select the number from the items above: ")


if choiceTwo == "1":
    print("You have selected Nachos")
    print("The total for this tem as",oneChoice, "dollars")
elif choiceTwo == "2":
    print("You have selected Burritos")
    print("The total for this item is",twoChoice, "dollars")
elif choiceTwo == "3":
    print("You have selected Quesadillas")
    print("The total for this item is",threeChoice, "dollars")
elif choiceTwo == "4":
    print("You have selected Baja blast")
    print("the total for this item is",fourChoice, "dollars")
elif choiceTwo == "5":
    print("Your final price will be", 4, "dollars")
    sys.exit()


menu()

choiceThree = input ("Choose your third option here, select from the items above: ")


if choiceThree == "1":
    print("You have selected Nachos")
    print ("The total for your third item is",oneChoice, "dollars")
elif choiceThree == "2":
    print("You have selected Burritos")
    print ("The total for your third item is",twoChoice, "dollars")
elif choiceThree == "3":
    print("You have selected Quesadillas")
    print ("The total for your third item is",threeChoice, "dollars")
elif choiceThree == "4":
    print("You have selected Baja blast")
    print ("The total for your third item is",fourChoice, "dollars")
elif choiceThree == "5":
    print("Your total will be the your last two items displayed, goodbye")
    print ("Your final price will be", 4+4, "dollars")
    sys.exit()

sum = (choice + choiceTwo + choiceThree)

print ("your final price is", 4+4+4, "dollars")






