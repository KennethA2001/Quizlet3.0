def header():
    print("Welcome to Kenneth's Quizlet.  This program is meant to help you study for your upcoming assesment.")


def get_num_terms():


    term = input("Enter the number of terms you would like to study ")
    terms = int(term)

    shopList = []

    while len(shopList) < terms:
        list_terms = input("Enter terms you would like to study: ")
        shopList.append(list_terms)
        print (shopList)
        print ("That's your shopping List")
        print (shopList)

    



                
header()
get_num_terms()

