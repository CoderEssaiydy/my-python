your_libary = []
your_libary.append(input("enter the name of a book you own:\n"))
book = input("enter the name of another book you own (or press enter to skip)\n")
if book :
    your_libary.append(book)
    print (f"your libary : {your_libary}")
else :
    print (f"your libary {your_libary}")
your_wishlist = []
your_wishlist.append(input("enter the name of a book you wish to have in the future : \n"))
book_future = input ("enter the name of another book you wish to have ( or press enter to skip) \n")
if book_future :
    your_wishlist.append(book_future)
    print(f"your wishlist: {your_wishlist}")
else :
    print (f"your wishlist : {your_wishlist}")
updated_libary = []
updated_wishlist = []
book_quired = input ("enter the name of abook from your wishlist that you've a quired (or press enter to skip):\n")
if book_quired in your_wishlist : 
   your_libary.append(book_quired)
   your_wishlist.remove(book_quired)
   print (f"updated libary : {your_libary}")
   print (f"updated wishlist : {your_wishlist}")
else : 
    print (f"your libary : {your_libary}")
    print (f"your wishlist : { your_wishlist}")
book_donate = input ("enter the name of a book from your libary you wish to donate ( or press enter to skip):\n")
if book_donate in your_libary :
   your_libary.remove(book_donate)
   print (f"final libary after donations : {your_libary}")
else :
    print (f"final libary {your_libary}")