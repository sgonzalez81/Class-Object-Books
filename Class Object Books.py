# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:35:39 2022

@author: salva
Set up a Class Object that keeps track of you books:

book title,

book author,

book length

genre (can be added)

how many books in each genre

book series
"""
class Book:
    def __init__(self, **kwargs):
        self.title  = 'None'
        self.author = 'None'
        self.length = 0
        self.genre  = 'None'
        self.set    = 'None'
        
        for arg in kwargs:
            if arg == 'title':
                self.title = kwargs['title']
            elif arg == 'author':
                self.author = kwargs['author']
            elif arg == 'length':
                self.length = kwargs['length']
            elif arg == 'genre':
                self.genre = kwargs['genre']
            elif arg == 'set':
                self.set = kwargs['set']
    
    def setTitle(self, title):
        self.title = title
        
    def getTitle(self):
        return self.title
    
    def setAuthor(self, author):
        self.author = author
    
    def getAuthor(self):
        return self.author
    
    def setLength(self, length):
        self.length = length
        
    def setGenre(self, genre):
        self.genre = genre
        
    def getGenre(self, genre):
        return self.genre
    
    def setSet(self, s):
        self.set = s
        
    def getSet(self):
        return self.set
    
    def __str__(self):
        return f"Title={self.title}, Author={self.author}, Pages={self.length}, " \
            f"Genre={self.genre}, Bookset={self.set}"


class Books:
    def __init__(self):
        self.books = []
    
    def addBook(self, **kwargs):
        b = Book(**kwargs)
        self.books.append(b)
        
    def printBooks(self):
        for book in self.books:
            print(book)
            
    def getBookByTitle(self, title):
        return [ book for book in self.books if book.title == title ]

    def getBookByGenre(self, genre):
        return [ book for book in self.books if book.genre == genre ]    



if __name__ == '__main__':   
    books = Books()   
    
    books.addBook(title = 'The Silver Eyes', author = 'Scott Cawthon', length = 400, genre = 'Horror')
    books.addBook(title = 'The Twisted Ones', author = 'Scott Cawthon', length = 304, genre = 'Horror')
    books.addBook(title = 'The Fourth Closet', author = 'Scott Cawthon', length = 352, genre = 'Horror')
    books.addBook(title = 'Five Nights at Freddys FAZBEAR Frights Into The Pit' , author = 'Scott Cawthon', length = 224, genre = 'Horror')
    books.addBook(title = 'Five Nights at Freddys FAZBEAR Frights Fetch' , author = 'Scott Cawthon', length = 272, genre = 'Horror')
    
    books.addBook(title = 'The Hunger Games', author = 'Suzanne Collins', length = 374, genre = 'Science Fiction')
    books.addBook(title = 'Catching Fire', author = 'Suzanne Collins', length = 400, genre = 'Science fiction')
    books.addBook(title = 'Mockingjay', author = 'Suzanne Collins', length = 390, genre = 'Science Fiction')
    
    print('Printing out books in collection:')
    print('-----------------------------------------------------------------------------------------')
    books.printBooks()
    
    print("\n\nListing books in the Science Fiction genre:")
    print('-----------------------------------------------------------------------------------------')
    
    for book in books.getBookByGenre('Science Fiction'):
        print(book)