
#importing the random module
import random

#getting input from user and converting the type to integer
user = int(input("Enter an integer number ranging 1 to 2 inclusively: "))

#generating a random integer and storing it into computerMove
computerMove = random.randint(1,2)

#checks if user input is 1
if(user == 1):
    
    #displaying what the computer stored
    print(f"Computer Move:{computerMove}")
    
    #checks if computer move is 1 when user input is 1
    if(computerMove == 1):
        print("User wins")
        
    #checks a second condition if computer move is 2 when user input is 1
    elif(computerMove == 2):
        print("Computer Wins")
        
#providing a second condition for the user    
elif(user == 2):
    
    #displaying what the computer stored
    print(f"Computer Move:{computerMove}")
    
    #checks if computer move is 1 when user input is 2
    if(computerMove == 1):
        print("Computer Wins")
        
    #checks a second condition if computer move is 2 when user input is 2
    elif(computerMove == 2):
        print("User Wins")
        
#runs the code if user do not enter an 1 or 2        
else:
    print("Invalid number")
        

