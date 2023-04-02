import pandas as pd
import numpy as np
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase): 
    
    def test_1_add_book(self):
        # Create BookLover instance, adding book
        global hp1
        hp1 = BookLover('Wilmer', 'etc7fq@virginia.edu', 'fantasy')
        hp1.add_book("Sorceror's Stone", 5)
        # Test-check book is in book_list
        # unittest.TestCase brings in the assertTrue
        self.assertTrue("Sorceror's Stone" in list(hp1.book_list['book_name'][:]))
    
    def test_2_add_book(self):
        # add the same book twice.
        hp1.add_book("broadway", 1)
        hp1.add_book("broadway", 1)
        #Test if it's in `book_list` only once.
        self.assertTrue(hp1.book_list['book_name'].is_unique)
                
    def test_3_has_read(self): 
        # pass a book in the list
        #test if the answer is `True`.
        self.assertTrue(hp1.has_read("Sorceror's Stone"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list
        #test the answer is `False` using self.assertFalse.
        self.assertFalse(hp1.has_read("Half-blood Prince"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, 
        hp1.add_book("Goblet of Fire", 1)
        hp1.add_book("Prisoner of Azkaban", 5)
        #and test num_books matches expected.
        expected = 4
        # unittest.TestCase brings in the assertEqual() method
        self.assertEqual(hp1.num_books_read(), expected)
    
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3.
        hp1.add_book("Half-blood Prince", 2)
        hp1.add_book("Order of Phoenix", 4)
        hp1.add_book("Deathly Hallows", 5)
        self.assertTrue(all(x>3 for x in list(hp1.fav_books()['book_rating'][:])))
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)