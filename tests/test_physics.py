import unittest
import numpy as np
from rolypoly.physics import RigidBody

class TestRigidBody(unittest.TestCase):
    """
        This class contains the unit tests for the RigidBody class

        Methods
        -------
        test_initialization()
            Tests the initialization of the RigidBody class
        test_apply_force()
            Tests the apply_force() method of the RigidBody class
        test_update_position()
            Tests the update_position() method of the RigidBody class
    """

    def test_initialization(self):
        """
            This method tests the initialization of the RigidBody class
        """
        body = RigidBody(mass=1.0, position=0.0, velocity=0.0)
        self.assertEqual(body.mass, 1.0)
        self.assertEqual(body.position, 0.0)
        self.assertEqual(body.velocity, 0.0)

    def test_apply_force(self):
        """
            This method tests the apply_force() method of the RigidBody class
        """
        body = RigidBody(mass=1.0, position=0.0, velocity=0.0)
        body._apply_force(force=1.0)
        self.assertEqual(body.acceleration, 1.0)

    def test_update_position(self):
        """
            This method tests the update_position() method of the RigidBody class
        """
        body = RigidBody(mass=1.0, position=0.0, velocity=0.0)
        body._apply_force(force=1.0)
        body._update_kinematics(time=1.0)
        self.assertEqual(body.position, 0.5)
        self.assertEqual(body.velocity, 1.0)

if __name__ == '__main__':
    unittest.main()
