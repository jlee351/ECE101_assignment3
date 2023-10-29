# Import random number generator package
import random

def randomNumberGenerator( size, data=[] ):
    # Generate a random number
    randNum = int( random.random() * size )

    # If user provided data, make sure this random
    # number does not already exist 
    if data:
        while randNum in data:
            randNum = int( random.random() * size )

    # return new random number
    return( randNum )


def createDatabase( num ):
    num_list = []

    print ("Generating " + str(num) + " random integers between 1 and 100")
    
    while len(num_list) < num :
        ran = randomNumberGenerator(100)

        if ran not in num_list:
            num_list.append(ran)
            
    print("Done generating random integers!")

    return num_list



def displayDatabase(a_list):

    print("Values in this dataset")
    
    counter_1 = 0
    temp = ""
    
    while counter_1<len(a_list):
        temp += "\ndata[" + str(counter_1) +"] = " + str(a_list[counter_1])
        counter_1 += 1

    return temp



def searchDatabase(b_list,value):

    result_list = []
    
    if value in b_list:
        result_list = [True, b_list.index(value)]
               
    else:
        result_list = [False, 99]

    return result_list



def myMain(val):

    new_list = createDatabase(val)
    tries = int( random.randint(1, val) )
    
    counter_2 = 0    
    while counter_2 < tries:
        
        answer = input("\nEnter a number to find: ")
        
        if searchDatabase(new_list, int(answer))[0] == True:
            print ("Congratulations! Found " + answer + " in my database after "+ str(counter_2 + 1) + " tries" )

        else:
            print ("Oops, " + answer + " isn't in my database")

        counter_2 += 1
    
    print("\nTime is up! Values in this database are: ")
    print(displayDatabase(new_list))

    again = input("\nDo you want to continue playing? (Y or N): ")
    if again == "Y":
        
        myMain(val)
        
                 
    elif again == "N":
        exit()
