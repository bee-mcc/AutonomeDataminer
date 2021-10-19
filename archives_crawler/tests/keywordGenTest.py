import unittest
from unittest.main import main

target = __import__("archives_spider_lachlain.py")
gen_keywords = target.gen_keywords

class TestGenkeywords(unittest.TestCase):

    def test_keyword_list(self):
        """
        Test that it can sum a list of integers
        """
        data = ["Kartoffel", "Stein", "Fahrrad"]

        result = gen_keywords("test.txt")
        self.assertEqual(result, data)


    if __name__ == '__main__':
        unittest.main()
        
        


    
