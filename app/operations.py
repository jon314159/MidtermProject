class operations:
    
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b

    @staticmethod
    def modulus(a: float, b: float) -> float:
        return a % b

    @staticmethod
    def percentage(a: float, b: float) -> float:
        return (a / b) * 100 if b != 0 else 0

    @staticmethod
    def absolute_difference(a: float, b: float) -> float:
        return abs(a - b)
    
    @staticmethod
    def square_root(a: float) -> float:
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number")
        return a ** 0.5
    
    @staticmethod
    def integer_division(a: int, b: int) -> int:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b
    
    