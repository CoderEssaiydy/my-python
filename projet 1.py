print("""welcome to my island there are two doors in front of you :a red door and a blue door  """)
door = input (" which door do you want to open ?\n").lower()
if door == "red":
    print ("""great ! now you entered a room you found three boxes : white , black , green """)
    box = input ("which box do you open ?\n ").lower()
    if box == "white":
        print ("oops ! you opened a box filed with snakes ")
    elif box == "black":
        print ("oops ! you opened a box filed white spiders")
    elif box == " green":
        print ("congratulations! you found the treasure")
    else : 
        print ("invalid choice")
elif door == "blue" :
        print("oops ! you chose the crocodile door")
else :
     print (" invalid choice")
       