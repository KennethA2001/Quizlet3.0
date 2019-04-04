import random

def header():
    print("Welcome to Kenneth's Quizlet.  This program is meant to help you study for your upcoming assesment")


def get_num_terms():
    terms = input("Enter the number of terms you would like to study")

    if terms.isnumeric():
        first_term = input("Please enter the first term you would like to study")
    else:
        print("Make sure you enter a number of terms")
            

header()
get_num_terms()
