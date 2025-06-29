from abc import abstractmethod
from app.operations import operations


class calculation:
    """
    Abstract base class for all calculator operations.

    :param a: The first operand.
    :type a: float
    :param b: The second operand.
    :type b: float
    """

    def __init__(self, a: float, b: float):
        self.a: float = a
        self.b: float = b

    @abstractmethod
    def execute(self) -> float:
        """
        Execute the calculation. Must be implemented by subclasses.

        :return: The result of the operation.
        :rtype: float
        """
        pass

    def string(self) -> str:
        """
        Return a string representation of the calculation.

        :return: A formatted string with the class name and operands.
        :rtype: str
        """
        return f"{self.__class__.__name__}({self.a}, {self.b})"


class CalculationFactory:
    """
    Factory class to register and create calculation objects.
    """

    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_class):
        """
        Register a new calculation class in the factory.

        :param calculation_class: The class to register.
        :type calculation_class: type

        :return: A decorator that ensures the class is registered only once.
        :rtype: function
        """

        cls._calculations[calculation_class.__name__] = calculation_class

        def decorator(cls):
            cls.register_calculation(cls)
            if cls.__name__ not in cls._calculations:
                cls._calculations[cls.__name__] = cls