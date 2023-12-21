# Desc: Physics classes and functions

from . import _type_float, _type_array


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
        _apply_force(force)
            Applies force to the body
        _update_kinematics(time)
            Updates the position of the body

        Examples
        --------
        >>> from rolypoly.physics import RigidBody
        >>> body = RigidBody(mass=1.0, position=0.0, velocity=0.0)
        >>> body.mass
        1.0
        >>> body.position
        0.0
        >>> body.velocity
        0.0
        >>> body.apply_force(1.0)
        >>> body.acceleration
        1.0
        >>> body.update_position(1.0)
        >>> body.position
        0.5
        >>> body.velocity
        1.0
    """
    def __init__(
        self,
        mass: _type_float,
        position: _type_float | _type_array = 0.0,
        velocity: _type_float | _type_array = 0.0,
        acceleration: _type_float | _type_array = 0.0,
    ) -> None:
        """
            Parameters
            ----------
            mass : float
                Mass of the body in kilograms
            position : float or ndarray
                Position of the body in meters
            velocity : float or ndarray
                Velocity of the body in meters per second
        """
        assert mass >= 0.0, 'mass must be a non-negative float'
        try:
            assert (
                position.size == 2 | position.size == 3
                & velocity.size == 2 | velocity.size == 3
                & acceleration.size == 2 | acceleration.size == 3
            ), 'position, velocity, and acceleration must be scalars or 3D vectors'
            assert position.size == velocity.size == acceleration.size, \
                'position, velocity, and acceleration must be of the same size'
        except AttributeError:
            assert (
                isinstance(position, float) | isinstance(position, int)
                & isinstance(velocity, float) | isinstance(velocity, int)
                & isinstance(acceleration, float) | isinstance(acceleration, int)
            ), 'position, velocity, and acceleration must be scalars or 3D vectors'
        self.__mass, self.__position, self.__velocity, self.__acceleration = \
            mass, position, velocity, acceleration

    def _apply_force(self, force: _type_float) -> None:
        """
            Applies force to the body

            Parameters
            ----------
            force : ndarray
                Force to be applied to the body in Newtons
        """
        self.__acceleration += force / self.mass

    def _update_kinematics(self, time: _type_float) -> None:
        """
            Updates the kinematics of the body

            Parameters
            ----------
            time : float
                Time elapsed in seconds
        """
        self.__position += self.__velocity * time
        self.__velocity += self.__acceleration * time
        self.__position += self.__acceleration * time ** 2 / 2

    @property
    def mass(self) -> _type_float:
        """
            Mass of the body in kilograms
        """
        return self.__mass

    @property
    def position(self) -> _type_float | _type_array:
        """
            Position of the body in meters
        """
        return self.__position

    @position.setter
    def position(self, position: _type_float | _type_array) -> None:
        """
            Sets the position of the body in meters
        """
        self.__position = position

    @property
    def velocity(self) -> _type_float | _type_array:
        """
            Velocity of the body in meters per second
        """
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: _type_float or _type_array) -> None:
        """
            Sets the velocity of the body in meters per second
        """
        self.__velocity = velocity

    @property
    def acceleration(self) -> _type_array:
        """
            Acceleration of the body in meters per second squared
        """
        return self.__acceleration
