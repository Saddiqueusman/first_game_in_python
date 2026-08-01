import os
import random 
choice=["rock","paper","scissor"]
comp_choice = random.choice(choice)
print(comp_choice)
def game():
 print("lets play rock, paper, scissor")
 choice=["rock","paper","scissor"]
 user_choice=input("enter you element     ")
 return user_choice
 
 
user_choice=game()
if  user_choice==comp_choice:
     print("let's play again")
     print("your choice",user_choice)
     print("computer choice",comp_choice)
elif user_choice=="rock" and comp_choice=="paper":
     print("computer win ")
     print("your choice",user_choice)
     print("computer choice",comp_choice)
elif user_choice=="paper" and comp_choice=="rock":
     print("conragulation you win")
     print("your choice",user_choice)
     print("computer choice",comp_choice)
elif user_choice=="scissor" and comp_choice=="rock":
     print("computer win you lose")
     print("your choice",user_choice)
     print("computer choice",comp_choice) 
elif user_choice=="rock" and comp_choice=="scissor":
    print("conragulation you win")
    print("your choice",user_choice)
    print("computer choice",comp_choice)
elif user_choice=="scissor" and comp_choice=="paper":
    print("conragulation you win")
    print("your choice",user_choice)
    print("computer choice",comp_choice)
elif user_choice=="paper" and comp_choice=="scissor":
    print("computer win you lose")
    print("your choice",user_choice)
    print("computer choice",comp_choice) 
else:
     print("invalid inputn")