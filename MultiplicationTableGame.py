import time
import random
import sys
menu = """
      Multiplication Table Game
1.Let's learn the multiplication table
2.Learn only a specific number
3.Quit the game
"""
while True:
    print(menu)
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        while True:
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            start = time.time()
            answer = int(input("{a}x{b} = ".format( a=num1, b=num2)))
            end = time.time()
            exactTime = end - start
            if answer == (num1 * num2):
                print(f"Correct!You figured it out in {round(exactTime)} seconds!")
            else:
                print(f"Incorrect!The answer was {num1 * num2}.")
            enter = input("Press enter to continue or type 'q' to quit: ")
            if enter == 'q' or enter == 'Q':
                break
    elif choice == 2:
        number = int(input("Enter the number you want to learn in the multiplication table:"))
        while number > 10 or number < 1:
            print("The number you entered is out of range!Please enter a number between 1 and 10!")
            number = int(input("Enter the number you want to learn in the multiplication table:"))
        while True:
            secondNumber = random.randint(1,10)
            start = time.time()
            answer = int(input("{a}x{b} = ".format( a=number,b=secondNumber)))
            end = time.time()
            exactTime = end - start
            if answer == (number * secondNumber):
                print(f"Correct!You figured it out in {round(exactTime)} seconds!")
            else :
                print(f"Incorrect!The answer was {number * secondNumber}.")
            enter = input("Press enter to continue or type 'q' to quit: ")
            if enter == 'q' or enter == 'Q':
                break
    if choice == 3:
        sys.exit()
    enter = input("Press enter to continue...")

