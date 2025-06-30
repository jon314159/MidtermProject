import os
import pandas as pd
from typing import List
from app.calculation import Calculation
from typing import Optional
from app.exceptions import FileProcessingError
# define HistoryObserver interface to avoid circular import
class HistoryObserver:
    def update(self, calculation: Calculation) -> None:
        """
        Called when the history changes; to be implemented by subclasses.
        """
        raise NotImplementedError
from app import config

class AutoSaveObserver(HistoryObserver):
    """
    Automatically saves the list of calculations to a CSV file whenever an update is triggered.
    """

    def __init__(self, history: List[Calculation], output_file: Optional[str] = None):
        """
        Initialize the observer with the history list and optional output file path.

        :param history: List of performed Calculation objects.
        :param output_file: Optional override for the CSV file path.
        """
        self.history = history
        self.output_file = output_file or os.path.join(config.CALCULATOR_HISTORY_DIR, "history.csv")

        # Ensure the output directory exists to prevent FileNotFoundError
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)

    def update(self, _: Calculation) -> None:
        """
        Save the full calculation history to a CSV file.

        :param _: The most recent Calculation (not used directly).
        """
        try:
            data = [{
                "operation": c.__class__.__name__,
                "operand1": c.a,
                "operand2": c.b,
                "result": c.result
                } for c in self.history]
            df = pd.DataFrame(data)
            df.to_csv(self.output_file, index=False, encoding=config.CALCULATOR_DEFAULT_ENCODING)
        except Exception as e:
            raise FileProcessingError(f"Error saving history to {self.output_file}: {e}")