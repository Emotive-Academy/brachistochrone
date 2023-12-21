# Import the test modules
from . import unittest
from .test_physics import TestRigidBody


# Create a test suite
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRigidBody))
    return suite


# Run the test suite if this file is executed directly
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
