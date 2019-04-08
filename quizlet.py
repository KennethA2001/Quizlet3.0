def header():
    print("Welcome to Kenneth's Quizlet.  This program is meant to help you study for your upcoming assesment.")


def get_num_terms():

    term = input("Enter the number of terms you would like to study ")
    terms = int(term)
    
    a = str(input("Please enter the first term you would like to study"))
    terms -= 1

        
     if terms == 0:
        print("Enter the defintion for the term")
    elif terms > 0:
        print(a)
    


                
header()
get_num_terms()
