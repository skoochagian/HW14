import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        bltest = BookLover('Sara','sk2hh@virginia.edu','fiction')
        bltest.add_book('The Hobbit', 4)
        testValue = 'The Hobbit' in set(bltest.book_list['book_name'])
        message = 'Book was not added to list'
        self.assertTrue(testValue, message)
    
    def test_2_add_book(self):
        bltest = BookLover('Sara','sk2hh@virginia.edu','fiction')
        bltest.add_book('The Hobbit', 4)
        bltest.add_book('The Hobbit', 4)
        testValue = bltest.num_books
        expected = 1
        self.assertEqual(testValue, expected)
    
    def test_3_has_read(self):
        bltest = BookLover('Sara','sk2hh@virginia.edu','fiction')
        bltest.add_book('The Hobbit', 4)
        testValue = bltest.has_read('The Hobbit')
        message = 'This book is not in the list'
        self.assertTrue(testValue, message)
    
    def test_4_has_read(self):
        bltest = BookLover('Sara','sk2hh@virginia.edu','fiction')
        bltest.add_book('The Hobbit', 4)
        testValue = bltest.has_read('The Great Gatsby')
        message = 'This book is not in the list'
        self.assertFalse(testValue,message)

    def test_5_num_books_read(self):
        bltest = BookLover('Sara','sk2hh@virginia.edu','fiction')
        bltest.add_book('The Hobbit', 4)
        bltest.add_book('1984', 2)
        bltest.add_book('Of Mice and Men',5)
        bltest.add_book('The Grapes of Wrath', 4)
        bltest.add_book('To Kill a Mockingbird', 1)
        actual = bltest.num_books_read()
        expected = 5
        self.assertEqual(actual,expected)

    def test_6_fav_books(self):
        bltest = BookLover('Sara','sk2hh@virginia.edu','fiction')
        bltest.add_book('The Hobbit', 3)
        bltest.add_book('1984', 2)
        bltest.add_book('Of Mice and Men',5)
        bltest.add_book('The Grapes of Wrath', 4)
        bltest.add_book('To Kill a Mockingbird', 1)
        testValue = bltest.fav_books()['book_rating'].to_list()
        expected = [5,4]
        self.assertEqual(testValue,expected)
        #how to show these are equal?? maybe show the ratings of these books?

if __name__ == '__main__':
    unittest.main(verbosity=3)