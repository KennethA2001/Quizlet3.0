def header():
    print("Welcome to Kenneth's Quizlet.  This program is meant to help you study for your upcoming assesment.")


def get_terms():

    global term, terms, termList, list_terms, definition


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
        definition = input("Enter the definition for " + list_terms + " " )

def quiz(list_terms,termList):

    points = 0

    missed_words = []

    print(" Lets Quiz!!")

    streak = 0

    for list_term in termList:
        
        guess= str(input("Input the definition of " + list_term))

        if guess == definition:
            points += 1
            streak += 1
        else:
            missed_words.append(definition)
            streak = 0
            
        if streak >= 2:
            if streak % 2 == 1:
                print("Wow, you must be a genius")
            else:
                print("Keep going, you're doing great")
        elif streak == 1:
            print("You're almost there")
        else:
            print("Keep studying, I know you got this")

    print(" Game over. You got, " + str(points) + "outta" + term)
    return missed_words


     
        
                
header()
get_terms()
quiz(list_terms, termList)
