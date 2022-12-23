#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 20, 2022
# This program asks the user
# to input a list of numbers
# and a divisor. The program
# will then show the remainder
# of all the numbers inputted

import math
import random
# import lists


def calc_remainder(user_num_list, int_divisor):
    # initializing remainder_list[]
    remainder_list = []
    # initializing counter
    counter = 0
    # initializing num_amount
    num_amount = len(user_num_list)
    for a_single_number in user_num_list:
        # initializing current_num
        current_num = user_num_list[counter]
        # initializing remainder_num
        remainder_num = current_num % int_divisor

        # adding remainder_num to list
        remainder_list.append(remainder_num)
        # returning results
        if counter == num_amount:
            return remainder_list
        else:
            counter = counter + 1


def main():
    # introductory paragraph
    print("This program asks the user")
    print("to input a list of numbers")
    print("and a divisor. The program")
    print("will then show the remainder")
    print("of all the numbers inputted")
    print("")

    # initializing list
    user_num_list = []

    # getting numbers
    while True:
        user_input = input("Enter a number [enter stop to stop]: ")
        # checking to see if loop continues
        if user_input == "stop":
            # initializing num_amount
            num_amount = len(user_num_list)
            # are there any numbers?
            if num_amount == 0:
                # error message
                print("Please enter one or more numbers.")
                continue
            else:
                break
        # checking valid input
        try:
            user_input_int = int(user_input)

            # adding input to list
            user_num_list.append(user_input_int)
        except ValueError:
            # Error message
            print("Please don't enter a decimal or string.")

    while (True):
        # getting divisor
        divisor = input("Enter a divisor: ")
        try:
            int_divisor = int(divisor)

            break
        except ValueError:
            # Error message
            print("Please enter a valid divisor.")


    # calling function
    division = calc_remainder(user_num_list, int_divisor)

    # displaying results
    print("The remainders of the inputted numbers are {}.".format(division))


if __name__ == "__main__":
    main()
