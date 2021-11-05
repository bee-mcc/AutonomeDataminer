import unittest
from unittest.main import main
from spider_utils import gen_keywords

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
        
        


    
