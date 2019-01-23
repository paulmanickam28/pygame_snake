# import random module 
import random
from tkinter import messagebox

  
# Print multiline instruction 
# performstring concatenation of string 
messagebox.showinfo("rules","Winning Rules of the snake water gun game as follows: \n"
                                +"snake vs water->snake wins \n"
                                + "water vs gun->water wins \n"
                                +"snake vs gun->gun wins \n") 
  
while True: 
    print("Enter choice \n 1. snake \n 2. water \n 3. gun \n") 
      
    # take the input from user 
    choice = int(input("User turn: ")) 
  
    # OR is the short-circuit operator 
    # if any one of the condition is true 
    # then it return True value 
      
    # looping until user enter invalid input 
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: ")) 
          
  
    # initialize value of choice_name variable 
    # corresponding to the choice value 
    if choice == 1: 
        choice_name = 'snake'
    elif choice == 2: 
        choice_name = 'water'
    else: 
        choice_name = 'gun'
          
    # print user choice  
    print("user choice is: " + choice_name) 
    print("\nNow its computer turn.......") 
  
    # Computer chooses randomly any number  
    # among 1 , 2 and 3. Using randint method 
    # of random module 
    comp_choice = random.randint(1, 3) 
      
    # looping until comp_choice value  
    # is equal to the choice value 
    while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 
  
    # initialize value of comp_choice_name  
    # variable corresponding to the choice value 
    if comp_choice == 1: 
        comp_choice_name = 'snake'
    elif comp_choice == 2: 
        comp_choice_name = 'water'
    else: 
        comp_choice_name = 'gun'
          
    print("Computer choice is: " + comp_choice_name) 
  
    print(choice_name + " V/s " + comp_choice_name) 
  
    # condition for winning 
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        print("snake wins => ", end = "") 
        result = "snake"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("gun wins =>", end = "") 
        result = "gun"
    else: 
        print("water wins =>", end = "") 
        result = "water"
  
    # Printing either user or computer wins 

    if result == choice_name: 
        messagebox.showinfo("result","<== User won the game ==>") 
    else: 
         messagebox.showinfo("result","<== computer won the game ==>")  
          
    print("Do you want to play again? (Y/N)") 
    ans = input() 
  
  
    # if user input n or N then condition is True 
    if ans == 'n' or ans == 'N': 
        break