# use unittest module to write unit test and run test case
import unittest

# import be tested class User
from user import User

# write a test class
class NamesTestCases(unittest.TestCase):
    # use setUp() function to prepare test data
    def setUp(self):
        self.u1=User("san","zhang")

    ''' Must start with test_  '''
    def test_names_without_middle(self):
        # use assert function to justic result
        self.assertEqual("San Zhang",self.u1.format_username())

# run test cases
unittest.main()

