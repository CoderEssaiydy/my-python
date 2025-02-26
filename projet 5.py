print("welcome to place the cat : 🐈")                                                        
rond =[ [ "🐁" , "🐁" , "🐁" ] , [ "🐁" , "🐁" , "🐁" ] , [ "🐁" , "🐁" , "🐁"  ] ]
print(f"{rond[0]} \n{rond[1]} \n{rond[2]}")
print("where should the rabbit go 🐈")
chose = input ("please choose a row and a colum :\n")
row = int(chose[0])-1
colum = int(chose [1])-1 
rond[row][colum] = "🐈"
print ("you succes ....")
print (f"{rond[0]} \n{rond[1]} \n{rond[2]}")