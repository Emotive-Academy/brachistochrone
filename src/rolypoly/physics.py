# Desc: Physics classes and functions

from . import np, _type_float

class RigidBody:
    """
        A rigid body is a body that does not deform under external forces.
        The motion of a rigid body is described by the Newton's second law of motion.

        Description
        -----------
        RigidBody is a class that describes the motion of a rigid body.

        Attributes
        ----------
        mass : float
            Mass of the body
        position : ndarray
            Position of the body
        velocity : ndarray
            Velocity of the body
        acceleration : ndarray
            Acceleration of the body

        Methods
        -------
        apply_force(force)
            Applies force to the body
        update_position(time)
            Updates the position of the body

        Examples
        --------
        >>> from rolypoly.physics import RigidBody
        >>> mass = 1.0
        >>> position = np.array([0.0, 0.0], dtype=_type_float)
        >>> velocity = np.array([0.0, 0.0], dtype=_type_float)
        >>> body = RigidBody(mass, position, velocity)
        >>> body.mass
        1.0
        >>> body.position
        array([0., 0.])
        >>> body.velocity
        array([0., 0.])
        >>> body.acceleration
        array([0., 0.])
        >>> force = np.array([0.0, 1.0], dtype=_type_float)
        >>> body.apply_force(force)
        >>> body.acceleration
        array([0., 1.])
        >>> time = 1.0
        >>> body.update_position(time)
        >>> body.position
        array([0., 1.])
    """
    def __init__(
            self,
            mass: _type_float,
            position: _type_float or np.ndarray,
            velocity: _type_float or np.ndarray,
        ) -> None:
        """
            Parameters
            ----------
            mass : float
                Mass of the body in kilograms
            position : ndarray
                Position of the body in meters
            velocity : ndarray
                Velocity of the body in meters per second
        """
        assert isinstance(mass, _type_float), 'mass must be a float'
        assert isinstance(position, np.ndarray), 'position must be a numpy array'
        assert isinstance(velocity, np.ndarray), 'velocity must be a numpy array'
        assert position.dtype == _type_float, 'position must be a float numpy array'
        assert velocity.dtype == _type_float, 'velocity must be a float numpy array'
        assert mass >= 0.0, 'mass must be a non-negative float'
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def apply_force(self, force: _type_float or np.ndarray) -> None:
        """
            Applies force to the body

            Parameters
            ----------
            force : ndarray
                Force to be applied to the body in Newtons
        """
        acceleration = force / self.mass
        self.velocity += acceleration

    def update_position(self, time: _type_float) -> None:
        """
            Updates the position of the body

            Parameters
            ----------
            time : float
                Time elapsed in seconds
        """
        self.position += self.velocity * time
