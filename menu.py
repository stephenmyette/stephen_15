def menu():
    print("welcome to my program!")
    print("please enter a choice:")
    print("1. tell me a funny joke:")
    print("2. tell me a riddle:")
    print("3. exit:")
    print("please enter your choice:")
    
    choice = input()
    return choice 

#main program

menuChoice = 0 

while menuChoice != 3:

    menuChoice = menu() 

    if menuChoice == 1:
        print("why did the chicken cross the rode?")
    
    elif menuChoice == 2:
        print("little red riding hood")
        
