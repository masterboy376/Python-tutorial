# create a library class 
# display book 
# lend book (who owns the book if not present in library - maitain a list for this)
# add book
# return book 
# instance = Library(listOfBook, libraryName)

# create a main function and run an infinite while loop asking users for their input 

from numpy import append


class Library:
    __listOfBorrowers = [];
    def __init__(self, list_of_books, library_name):
        self.listOfBooks = list_of_books
        self.libraryName = library_name

    def displayBooks(self):
        __i=0
        print(f"{self.libraryName} holds the following books:")
        for item in self.listOfBooks:
            print(f'{__i+1}. {item["name"]} witten by {item["author"]}')
            __i+=1
        __i=0

    def lendBook(self, bookToBeLended, borrower):
        for item in self.listOfBooks:
            if(bookToBeLended["name"]==item["name"]):
                (self.listOfBooks).remove(item)
                self.__listOfBorrowers.append({'borrower':borrower, 'book':item})
                return f'{item["name"]} written by {item["author"]} has been lended to {borrower}'
        return f"{bookToBeLended} is not available"

    def addBook(self, newBook):
        (self.listOfBooks).append(newBook)
        print(f'{newBook["name"]} witten by {newBook["author"]} is now added to the library')

    def returnBook(self, lendedBook, borrower):
        for item in self.__listOfBorrowers:
            if (lendedBook["name"] == item["book"]["name"] and borrower == item["borrower"]):
                (self.listOfBooks).append(lendedBook)
                return f'{lendedBook["name"]} witten by {lendedBook["author"]} is now returned to the library by {borrower}'
        return f'{lendedBook["name"]} witten by {lendedBook.auther} was never lended'
            

books = [
    {'name':'13 reasons why',
    'author': 'sam holland'},
    {'name':'earth',
    'author': 'sambhav kaushik'},
]            
myLib = Library(books,'myLib')

while(True):
        action = input('What action wuld you like to perform( displayBook, lendBook, addBook, returnBook or exit): ')
        if (action == 'displayBook'):
            myLib.displayBooks()
            continue
        elif(action == 'lendBook'):
            lend_Name: input('Enter your name: ')
            lend_Book = input('Enter the name of the book you would like to borrow: ')
            lend_Author: input('Enter the name of the author of the book: ')
            print(myLib.lendBook({'name':lend_Book, 'author': lend_Author}, lend_Name))
            continue
        elif(action == 'addBook'):
            add_Book = input('Enter the name of the book you would like to add: ')
            add_Author: input('Enter the name of the author of the book: ')
            myLib.addBook({'name':add_Book,'author': add_Author})
            continue
        elif(action == 'returnBook'):
            return_Name: input('Enter your name: ')
            return_Book = input('Enter the name of the book you would like to add: ')
            return_Author: input('Enter the name of the author of the book: ')
            print(myLib.returnBook({'name':return_Book, 'author': return_Author}, return_Name))
            continue
        elif(action =='exit'):
            break




# print(myLib.listOfBooks)
# print(myLib.libraryName)

# myLib.displayBooks()

# print(myLib.lendBook({'name':'13 reasons why','author': 'sam holland'}, "hanna"))

# myLib.displayBooks()

# myLib.addBook({'name':'program','author': 'sam'})
# myLib.addBook({'name':'13 reasons why','author': 'sam holland'})

# myLib.displayBooks()

# print(myLib.returnBook({'name':'13 reasons why','author': 'sam holland'}, "hanna"))

# myLib.displayBooks()


