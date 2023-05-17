# A simple python program to calculate an addition subtraction etc 
import turtle 
import os 

def addition(choice):
    if choice == 1:
        print("What is the first number: ")
        num1 = int(input("> "))
        print("What is the second number: ")
        num2 = int(input("> "))

        total = num1 + num2
        return print(f"The total of {num1} and {num2} is {total}")

def subtract(choice):
    if choice == 2:
        print("What is the first number: ")
        num1 = int(input("> "))
        print("What is the second number: ")
        num2 = int(input("> "))

        difference = num1 - num2 
        return print(f"The difference of {num1} and {num2} is {difference}")
    
def multiply(choice):
    if choice == 3:
        print("What is the first number: ")
        num1 = int(input("> "))
        print("What is the second number: ")
        num2 = int(input("> "))

        total = num1 * num2 
        return print(f"The total of {num1} and {num2} is {total}")

def division(choice):
    if choice == 4: 
        print("What is the first number: ")
        num1 = int(input("> "))
        print("What is the second number: ")
        num2 = int(input("> "))

        total = num1 // num2 
        return print(f"The total of {num1} divided {num2} is {total}")
    

print("What would you like me to do: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("> "))
if choice ==  1:
    print("You have choose addition! ")
    addition(choice) 
elif choice == 2:
    print("You have choose Subtraction")
    subtract(choice)
elif choice == 3:
    print("You have choose Multiplication")
    multiply(choice)
elif choice == 4:
    print("You have choose Division")
    division(choice)
