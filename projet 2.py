import random 
print("welcome to the coin guessing game!")
print("choose a method to toos the coin")
print("1 : using random.random()")
print("2 : using random.randint()")
choice = input("enter your choice (1 or 2):\n")
if choice == "1" :
  number = random.random ()
  if number >= 0.5 :
    computer_result = "heads"
  else :
    computer_result = "tails" 
elif choice == "2" :
  if  random.randint(0,1) == 0 :
      computer_result = "heads" 
  else :
       computer_result = "tails" 
else :
  print ("invild choice")
user_choice = input ("enter your guess (heads or tails ) : \n")
if user_choice.lower() == computer_result.lower() :
   print ("congratulations ! you won !")
else : 
   print("sorry,you lost")
   print(f"the computer coin toss result was : {computer_result}")
