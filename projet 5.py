colors = []
colors.append (input ("add the first color you like :\n"))
choice = input ("do you want to add more colors: yes or no : \n").lower()
if choice == "yes" :
    colors.append (input ("add another color like are :\n"))
    print("the colors you like are :")
    print (colors)
else : 
    print ("the color you like is :")
    print (colors)

