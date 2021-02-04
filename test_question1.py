import unittest
import question1

class Testquestion1(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(question1.cube('a'), "poor input")
        self.assertEqual(question1.cube(.258), 0.017173512)
        self.assertEqual(question1.cube(-25), -15625)

if __name__ == '__main__':
    unittest.main(verbosity=2)