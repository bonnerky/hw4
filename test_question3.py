import unittest
import question3

class Testquestion2(unittest.TestCase):
    def test_question3(self):
        self.assertEqual(question3.name_gen("Kyle", "Bonner"), "Kyle Bonner")
        self.assertEqual(question3.name_gen("Yes", "&/@"), "Name includes illegal characters")
        self.assertEqual(question3.name_gen("Kyle Anthony", "Bonner"), "please input just your first and last name")

if __name__ == '__main__':
    unittest.main(verbosity=2)