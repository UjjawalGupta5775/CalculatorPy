# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:53:51 2021

@author: hp
"""

def add(x,y):
    """ Add Two Numbers. """
    return x + y

def subtract(x,y):
    """  Subtract Two Numbers. """
    return x - y

def multiply(x, y):
    """Multiply Two Numbers."""
    return x * y

def divide(x,y):
    """Divide Two Numbers. """
    return x / y

def check_if_user_has_finished():
    """
    Checks that the user wants to finish or not.
    Performs some verification of the input."""
    
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input("Do you want to finish (y/n): ")
        if user_input == "y":
            user_input_accepted = True
        elif user_input == "n":
            ok_to_finish = False
            user_input_accepted = True
        else:
            print("Respond must be (y/n), please try again")
    return ok_to_finish



def get_operation_choice():
    input_ok = False
    while not input_ok:
        print("Menu Options are:")
        print("\t1. Add")
        print("\t2. Subtract")
        print("\t3. Multiply")
        print("\t4. Divide")
        print("-----------------")
        user_selection = input("Please make a selection: ")
        if user_selection in ("1", "2", "3", "4"):
            input_ok = True
        else:
            print("Invalid Input (must be 1-4)")       
    print("-----------------")
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input("Input the First Number: ")
    num2 = get_integer_input("Input the Second Number: ")
    return num1, num2

def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print("The input must be an integer")
        value_as_string = input(message)
    return int(value_as_string)




finished = False
while not finished:
    result = 0
    # Get the Operator From the User
    menu_choice = get_operation_choice()
    # Get the numbers from the User.
    n1, n2 = get_numbers_from_user()
    # Select the Operator
    if menu_choice == "1":
        result = add(n1, n2)
    elif menu_choice == "2":
        result = subtract(n1, n2)
    elif menu_choice == "3":
        result = multiply(n1, n2)
    elif menu_choice == "4":
        result = divide(n1, n2)
    
    #Print Data
    print("Result:", result)
    print("=================")
    # Determine if the user has finished
    finished = check_if_user_has_finished()
    
print("Bye")
    

