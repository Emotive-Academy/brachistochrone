# This is the __init__.py file for the test package

# Import the necessary modules for unit testing
import unittest

# Import the test modules
from .test_physics import TestRigidBody

# Create a test suite
def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRigidBody))
    return suite

# Run the test suite if this file is executed directly
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(create_test_suite())
