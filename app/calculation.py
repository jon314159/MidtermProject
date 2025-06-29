from abc import abstractmethod
from app.operations import operations


class calculation:
        def __init__(self, a: float, b: float):
            self.a: float = a
            self.b: float = b

        @abstractmethod
        def execute(self) -> float:
            pass

        def string(self) -> str:
            return f"{self.__class__.__name__}({self.a}, {self.b})"
        
class CalculationFactory:

    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_class):
        cls._calculations[calculation_class.__name__] = calculation_class

        def decorator(cls):
            cls.register_calculation(cls)
            if cls.__name__ not in cls._calculations:
                raise ValueError(f"Calculation class {cls.__name__} is not registered.")
            if cls.__name__ in cls._calculations:
                raise ValueError(f"Calculation class {cls.__name__} is already registered.")
            return cls
        return decorator
    @classmethod
    def create_calculation(cls, calculation_name: str, a: float, b: float) -> calculation:
        if calculation_name not in cls._calculations:
            raise ValueError(f"Calculation {calculation_name} is not registered.")
        return cls._calculations[calculation_name](a, b)
    
    # Register the add calculation after CalculationFactory is defined
@CalculationFactory.register_calculation
class add(calculation):
    def execute(self) -> float:
        return operations.add(self.a, self.b)
@CalculationFactory.register_calculation
class subtract(calculation):
    def execute(self) -> float:
        return operations.subtract(self.a, self.b)
@CalculationFactory.register_calculation
class multiply(calculation):
    def execute(self) -> float:
        return operations.multiply(self.a, self.b)
@CalculationFactory.register_calculation
class divide(calculation):
    def execute(self) -> float:
        return operations.divide(self.a, self.b)
@CalculationFactory.register_calculation
class power(calculation):
    def execute(self) -> float:
        return operations.power(self.a, self.b)
@CalculationFactory.register_calculation
class modulus(calculation):
    def execute(self) -> float:
        return operations.modulus(self.a, self.b)
@CalculationFactory.register_calculation
class percentage(calculation):
    def execute(self) -> float:
        return operations.percentage(self.a, self.b)
@CalculationFactory.register_calculation
class absolute_difference(calculation):
    def execute(self) -> float:
        return operations.absolute_difference(self.a, self.b)            
