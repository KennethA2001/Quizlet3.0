def header():
    print("Welcome to Kenneth's Quizlet.  This program is meant to help you study for your upcoming assesment.")


def get_terms():

    global term, terms, termList, list_terms


    term = input("Enter the number of terms you would like to study ")
    terms = int(term)

    termList = []

    while len(termList) < terms:
        list_terms = input("Enter terms you would like to study: ")
        termList.append(list_terms)
        print(termList)
    print("Here is your terms list")
    print(termList)

    for list_terms in termList:
        definition = input("Enter the definition for " + list_terms )

def quiz(list_terms,termList):

    points = 0

    missed_words = []

    print(" Lets Quiz!!")

    streak = 0

    for list_term in termList:
        guess= str(input("Input the definition of" + list_term))
        if guess == definition:
            points += 1
            streak += 1
        else:
            missed_words.append(defintion)
            streak = 0
    return points


     
        
                
header()
get_terms()
quiz(list_terms, termList)
