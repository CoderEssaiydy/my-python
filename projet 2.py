import random 
pin_code = random.randint(1000,9999)
user_pin = int(input("enter 4_digit pin code :\n"))
if len (str(user_pin))>4 or len (str(user_pin))<4:
    print ("please enter 4 digits")
elif user_pin == pin_code:
    print (" success ! pin code matched")
else :
    print ("failure ! pin did not match")
    print (f"the computer generadthis pin : {pin_code}")
