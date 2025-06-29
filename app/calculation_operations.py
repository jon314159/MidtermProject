from app.calculation import Calculation, CalculationFactory
from app.operations import operations

@CalculationFactory.register_calculation
class add(Calculation):
    def execute(self) -> float:
        self.result = operations.add(self.a, self.b)
        return self.result

@CalculationFactory.register_calculation
class subtract(Calculation):
    def execute(self) -> float:
        self.result = operations.subtract(self.a, self.b)
        return self.result

@CalculationFactory.register_calculation
class multiply(Calculation):
    def execute(self) -> float:
        self.result = operations.multiply(self.a, self.b)
        return self.result

@CalculationFactory.register_calculation
class divide(Calculation):
    def execute(self) -> float:
        self.result = operations.divide(self.a, self.b)
        return self.result
@CalculationFactory.register_calculation
class power(Calculation):
    def execute(self) -> float:
        self.result = operations.power(self.a, self.b)
        return self.result
@CalculationFactory.register_calculation
class modulus(Calculation):
    def execute(self) -> float:
        self.result = operations.modulus(self.a, self.b)
        return self.result
@CalculationFactory.register_calculation
class percentage(Calculation):
    def execute(self) -> float:
        self.result = operations.percentage(self.a, self.b)
        return self.result
@CalculationFactory.register_calculation
class absolute_difference(Calculation):
    def execute(self) -> float:
        self.result = operations.absolute_difference(self.a, self.b)
        return self.result
@CalculationFactory.register_calculation
class square_root(Calculation):
    def execute(self) -> float:
        self.result = operations.square_root(self.a)
        return self.result
@CalculationFactory.register_calculation
class integer_division(Calculation):
    def execute(self) -> float:
        self.result = operations.integer_division(int(self.a), int(self.b))
        return self.result