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
            position: _type_float = 0.0,
            velocity: _type_float = 0.0,
            acceleration: _type_float = 0.0,
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
        assert mass >= 0.0, 'mass must be a non-negative float'
        self.__mass, self.__position, self.__velocity, self.__acceleration = mass, position, velocity, acceleration

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
    def position(self) -> np.ndarray:
        """
            Position of the body in meters
        """
        return self.__position
    
    @position.setter
    def position(self, position: _type_float or np.ndarray) -> None:
        """
            Sets the position of the body in meters
        """
        self.__position = position

    @property
    def velocity(self) -> np.ndarray:
        """
            Velocity of the body in meters per second
        """
        return self.__velocity
    
    @velocity.setter
    def velocity(self, velocity: _type_float or np.ndarray) -> None:
        """
            Sets the velocity of the body in meters per second
        """
        self.__velocity = velocity

    @property
    def acceleration(self) -> np.ndarray:
        """
            Acceleration of the body in meters per second squared
        """
        return self.__acceleration
