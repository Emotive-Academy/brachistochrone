import unittest
import numpy as np
from rolypoly.physics import RigidBody, _GRAVITY


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

    body1 = RigidBody(mass=1.0, position=0.0, velocity=0.0, gravity_vector=-1.0)
    body2 = RigidBody(
        mass=1.0,
        position=np.array([0, 0]),
        velocity=np.array([0, 0]),
        acceleration=np.array([0, 0]),
        gravity_vector=np.array([0, -1]),
    )

    def test_initialization(self):
        """
            This method tests the initialization of the RigidBody class
        """
        self.assertEqual(self.body1.mass, 1.0)
        self.assertEqual(self.body2.mass, 1.0)
        self.body1._apply_force(force=0)
        self.body1.position, self.body1.velocity = 0.0, 0.0
        self.body2._apply_force(force=np.array([0, 0]))
        self.body2.position, self.body2.velocity = np.array([0, 0]), np.array([0, 0])
        self.assertEqual(self.body1.position, 0.0)
        self.assertEqual(self.body1.velocity, 0.0)
        self.assertEqual(self.body1.acceleration, 0.0)
        self.assertTrue(np.array_equal(self.body2.position, np.array([0, 0])))
        self.assertTrue(np.array_equal(self.body2.velocity, np.array([0, 0])))
        self.assertTrue(np.array_equal(self.body2.acceleration, np.array([0, 0])))

    def test_apply_force(self):
        """
            This method tests the apply_force() method of the RigidBody class
        """
        self.body1._apply_force(force=1.0)
        self.assertEqual(self.body1.acceleration, 1.0)
        self.body2._apply_force(force=np.array([1, 1]))
        self.assertTrue(np.array_equal(self.body2.acceleration, np.array([1, 1])))

    def test_update_position(self):
        """
            This method tests the update_position() method of the RigidBody class
        """
        self.body1.position, self.body1.velocity = 0.0, 0.0
        self.body2.position, self.body2.velocity = np.array([0, 0]), np.array([0, 0])
        self.body1._apply_force(force=1.0)
        self.body2._apply_force(force=np.array([1, 1]))
        self.body1._update_kinematics(time=1.0)
        self.assertEqual(self.body1.position, 0.5)
        self.assertEqual(self.body1.velocity, 1.0)
        self.body2._update_kinematics(time=1.0)
        self.assertTrue(np.array_equal(self.body2.position, np.array([0.5, 0.5])))
        self.assertTrue(np.array_equal(self.body2.velocity, np.array([1, 1])))
        self.__position_updated: bool = True

    def test_kinetic_energy(self):
        """
            This method tests the kinetic_energy() method of the RigidBody class
        """
        self.body1.position, self.body1.velocity = 0.0, 10.0
        self.body2.position, self.body2.velocity = np.array([0, 0]), np.array([10, 10])
        self.assertEqual(self.body1.kinetic_energy, 50)
        self.assertAlmostEqual(self.body2.kinetic_energy, 100)

    def test_potential_energy(self):
        """
            This method tests the potential_energy() method of the RigidBody class
        """
        self.body1.position, self.body1.velocity = 1.0, 10.0
        self.body2.position, self.body2.velocity = np.array([1, 1]), np.array([10, 10])
        self.assertEqual(self.body1.potential_energy, - _GRAVITY)
        self.assertAlmostEqual(self.body2.potential_energy, - _GRAVITY)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRigidBody('test_initialization'))
    suite.addTest(TestRigidBody('test_apply_force'))
    suite.addTest(TestRigidBody('test_update_position'))
    suite.addTest(TestRigidBody('test_kinetic_energy'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
