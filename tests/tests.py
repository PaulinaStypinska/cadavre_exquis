import unittest
import sys
from context import sample
from sample.sample import Cadavre_Exquis


class TestHelperFunctions(unittest.TestCase):
    def test_game(self):
        cadavre = Cadavre_Exquis()
        self.assertEqual(cadavre.check_progress(), "adjective")
        cadavre.add_to_sentence("trombone")
        self.assertEqual(cadavre.sentence,['The', 'trombone'])



if __name__ == '__main__':
    unittest.main()
