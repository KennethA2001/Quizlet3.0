def header():
    print("Welcome to Kenneth's Quizlet.  This program is meant to help you study for your upcoming assesment.")


def get_terms():


    term = input("Enter the number of terms you would like to study ")
    terms = int(term)

    termList = []

    while len(termList) < terms:
        list_terms = input("Enter terms you would like to study: ")
        termList.append(list_terms)
        print(termList)
    print("Here is your terms list")
    print(termList)

    for list_term in termList:
        definition = input("Enter the definition for " + list_term)
     
        
                
header()
get_terms()

