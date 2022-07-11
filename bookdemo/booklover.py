import pandas as pd 
class BookLover():
     
    book_list = pd.DataFrame({'book_name':[],'book_rating':[]})
    num_books = 0
    def __init__(self,name,email,fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

    def add_book(self,title, rating):
        if title in set(self.book_list['book_name']):
            print('Book already in list')
        else:
            new_book = pd.DataFrame({'book_name': [title], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        return self.book_list
        
    def has_read(self,name):
        if name in self.book_list.values:
            return True
        else:
            return False

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        favorite = self.book_list[self.book_list['book_rating'] > 3]
        return favorite
