#Name: Nicholas Levine
#Date: 2/6/25
#Program: Module 3 Python Project

'''
this program will display the text
from a book cover on a screen and
simulate selling several copies of the book
'''

# make a multiline string to represent the book cover
cover = '''
        GEORGE ORWELL
        _____________
        NINETEEN EIGHTY-
        FOUR

'''

print(cover)
print()

# create a variable for the price of the book
# and assign it to a float value
bookprice = 19.99

#ask the user how many books they want and store it in a variable
bookQty = int(input("How many books do you want?"))
total = bookprice * bookQty
print(f"The total for {str(bookQty)} books at $ {str(bookprice)} each is ${str(total)}.")