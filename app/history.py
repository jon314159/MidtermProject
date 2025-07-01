import os
import pandas as pd
from typing import List, Optional
from app.calculation import Calculation
from app.exceptions import FileProcessingError
from app import config
from abc import ABC, abstractmethod
from typing import Sequence
# Define HistoryObserver interface to avoid circular import
class HistoryObserver(ABC):
    @abstractmethod
    def update(self, calculation: Calculation) -> None:
        pass

class AutoSaveObserver(HistoryObserver):
    def __init__(self, history: Sequence[Calculation], output_file: Optional[str] = None):
        self.history = history

        # Resolve default output file path
        history_dir = config.CALCULATOR_HISTORY_DIR or "history"
        self.output_file = output_file or os.path.join(history_dir, "history.csv")

        # ✅ Fix: force directory creation even if history_dir is "history"
        output_dir = os.path.dirname(self.output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
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
                "result": getattr(c, "result", None)  # Use getattr to avoid crash if unset
            } for c in self.history]

            df = pd.DataFrame(data)
            df.to_csv(self.output_file, index=False, encoding=config.CALCULATOR_DEFAULT_ENCODING)
        except Exception as e:
            raise FileProcessingError(f"Error saving history to {self.output_file}: {e}")
