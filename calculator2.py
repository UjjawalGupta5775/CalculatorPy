# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:40:48 2021

@author: hp
"""
print("\t\tWelcome to Calculator by Ujjawal.")
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2



def end_program():
# Ask user to continue or not
# Return true and exit on y
# Return false and repeat on n
# Ask for input again on some other value
    ok_to_finish = False
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input("Do you want to calculate again (y/n): ")
        if user_input == "y":
            user_input_accepted = True
        elif user_input == "n":
            user_input_accepted = True
            ok_to_finish = True
        else:
            print("Input must be (y/n)")
    return ok_to_finish
    


def operator_selector():
    # Give the list of options available to choose
    # Ask user to input a choice
    # If the choice is from options:
        # Return that option
    # If choice is not from options, ask user to input again by giving alert.
    # Return the input received from user as str
    operation_selected = False
    while not operation_selected:
        print("Menu Options Are: ")
        print("\t1. Add")
        print("\t2. Subtract")
        print("\t3. Multiply")
        print("\t4. Divide")
        print("-----------------")
        user_choice = input("Select an option to perform: ")
        if user_choice in ("1", "2","3","4"):
            operation_selected = True
        else:
            print("Please enter an integer (1-4)")
            print("---------------")
    return user_choice
        

def take_num():
    num1 = return_int("Enter the First Number: ")
    num2 = return_int("Enter the Second Number: ")
    return num1, num2
    
def return_int(message):
    check = input(message)
    while not check.isnumeric():
        print("Please enter an intger.")
        check = input(message)
    return int(check)
    
    



finished = False
while not finished:
    result = 0
    # Ask user to select an operator
    menu_choice = operator_selector()
    
    # Ask user for numbers
    n1, n2 = take_num()
    
    # Perform the operation
    if menu_choice == "1":
        result = add(n1, n2)
    elif menu_choice == "2":
        result = subtract(n1, n2)
    elif menu_choice == "3":
        result = multiply(n1, n2)
    elif menu_choice == "4":
        result = divide(n1, n2)
        
    # Print Result
    print("Result:", result)
    
    # Ask user to continue or not
    finished = end_program()
print("Bye")
print("Have a Great Day ahead.")