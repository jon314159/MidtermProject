from abc import ABC, abstractmethod
from app.calculation import Calculation

class HistoryObserver(ABC):
    """
    Abstract base class for calculator observers.
    """

    @abstractmethod
    def update(self, calculation: Calculation) -> None:
        """
        React to a new calculation event.

        :param calculation: The Calculation instance to observe.
        """
        pass  # pragma: no cover
