import unittest
import question2

class Testquestion2(unittest.TestCase):
    def test_question2(self):
        self.assertEqual(question2.average_val([2.4, 3, 8, 3.98, 6]), 4.676)
        self.assertEqual(question2.average_val([]), "empty list")
        self.assertEqual(question2.average_val([3.5]), 3.5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
