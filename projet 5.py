import random
rock_ascci = ("""
       _______
   ---'   ____)
         (_____)
         (_____)
         (____)
   ---.__(___) """)
paper_ascci = (""" 
       _______
   ---'    ____)____
              ______)
             _______)
            _______)
   ---.__________)""")
scissors_ascci = ("""
    _______
   ---'   ____)____
             ______)
          __________)
         (____)
   ---.__(___)
""")
print("welcome to the rock , paper, scissors game :")
choice = input("press to continue or type (help) for the rules help :\n").lower()
if choice == "help" :
       print("       ********RULES********")
       print("1) you choose and the computer chooses")
       print("2) rock smaches scissors -> rock wins")
       print("3) scissors cut paper -> scissors win")
       print("4) paper covers rock -> paper wins")

user_choice = input("enter your choice ( rock , paper , scissors ):\n").lower()
if user_choice not in ["rock" ,"paper", "scissors"] :
       print ("invalid choice . please run the program again and choose rock , paper , or scissors ")
else : 
       if user_choice == "rock" :
              print(f"your choice : \n{rock_ascci}")
       elif user_choice == "paper" :
            print(f"your choice : \n{paper_ascci}")
       else : 
            print(f"your choice : \n{scissors_ascci}")
computer_choice = random.choice(["rock", "paper", "scissors"])
if computer_choice == "rock" :
      print(f"computer_choice : \n{rock_ascci}")
elif computer_choice == "paper" :
      print (f"computer_choice : \n{paper_ascci}")
else : 
      print(f"computer_choice : \n{scissors_ascci}")

if user_choice == computer_choice :
      print(" it's a tie ")
elif ( user_choice == "rock" and computer_choice == "scissors" 
     or
     user_choice == "paper" and computer_choice == "rock"
     or
     user_choice == "scissors" and computer_choice == "paper") :
      print ("you win ...")
else : 
      print (" you loss ...")
  
