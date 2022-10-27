import unittest
from translator import englishToFrench,frenchToEnglis


class Test1(unittest.TestCase): 
    def test_en2fr(self):  
        self.assertEqual(englishToFrench(''), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') #test

class Test2(unittest.TestCase): #test
    def test_fr2en(self): #test
        self.assertEqual(frenchToEnglis(''), '') # test Null
        self.assertEqual(frenchToEnglis('Bonjour'), 'Hello') #test

unittest.main()
