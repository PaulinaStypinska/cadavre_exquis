import sys
import os
import unittest
print(sys.path)
from context import sample
from sample import wordApiCalls





class TestApiCalls(unittest.TestCase):
    def testRandom(self):
        self.assertTrue(isinstance(wordApiCalls.getRandomWord("noun"), str))

    def testCheckWordIsTrue(self):
        self.assertTrue(wordApiCalls.checkWord("coughed", "verb"))

    def testCheckWordIsFalse(self):
        self.assertFalse(wordApiCalls.checkWord("route", "adjective"))

    def testCheckCorrectWordIsTrue(self):
        self.assertEqual(wordApiCalls.checkCorrectWord("bold"), "adjective")


if __name__ == '__main__':
    unittest.main()

