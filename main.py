# importing the module
import sys

# this function will be the first to run as soon as the main function executes
def initial_phonebook():
    rows, colls = int(input("Please enter the initial number of contacts")), 5
    
    # We are collecting the initial number of contacts the user wants to have in the # phonebook already. User may also enter 0 if he does not wish to enter any.
    phonebook = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" %(i+1))
        print("NOTE : indicates mandatory fields")

        print(".......................")
        temp = []
        for j in range(colls):
        # We have taken conditions for the value of j only for personalized


        # Such as name numeber, email, id, dob, category etc
        if j == 0 :
                temp.append(str(input("Enter name*  ")))
                

                if temp[j] == '' or temp[j] ==  ' ':
                     sys.exit("Name is a mandatory field. Process exiting")


        if j == 1:
                temp.append(str(input("Enter number*  ")))


        if j == 2 :
                temp.append(str(input("Enter email address*  ")))

