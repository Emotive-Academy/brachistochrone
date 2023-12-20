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
        mass = 1.0
        position = np.array([0.0, 0.0], dtype=np.float64)
        velocity = np.array([0.0, 0.0], dtype=np.float64)
        body = RigidBody(mass, position, velocity)
        self.assertEqual(body.mass, 1.0)
        np.testing.assert_array_equal(body.position, np.array([0.0, 0.0]))
        np.testing.assert_array_equal(body.velocity, np.array([0.0, 0.0]))
        np.testing.assert_array_equal(body.acceleration, np.array([0.0, 0.0]))

    def test_apply_force(self):
        mass = 1.0
        position = np.array([0.0, 0.0], dtype=np.float64)
        velocity = np.array([0.0, 0.0], dtype=np.float64)
        body = RigidBody(mass, position, velocity)
        force = np.array([0.0, 1.0], dtype=np.float64)
        body.apply_force(force)
        np.testing.assert_array_equal(body.acceleration, np.array([0.0, 1.0]))

    def test_update_position(self):
        mass = 1.0
        position = np.array([0.0, 0.0], dtype=np.float64)
        velocity = np.array([0.0, 0.0], dtype=np.float64)
        body = RigidBody(mass, position, velocity)
        time = 1.0
        body.update_position(time)
        np.testing.assert_array_equal(body.position, np.array([0.0, 0.0]))

if __name__ == '__main__':
    unittest.main()
