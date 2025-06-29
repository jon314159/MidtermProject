import os
import pandas as pd
from typing import List, Optional
from app.calculation import Calculation
from app.history import HistoryObserver
from app import config
from typing import Sequence

class AutoSaveObserver(HistoryObserver):
    """
    Automatically saves the list of calculations to a CSV file.
    """

    def __init__(self, history: Sequence[Calculation], output_file: Optional[str] = None):
        """
        Initialize the AutoSaveObserver.

        :param history: List of calculations to track and save.
        :param output_file: Optional path to save the history CSV.
        """
        self.history = history
        self.output_file = output_file or os.path.join(config.CALCULATOR_HISTORY_DIR, "history.csv")

    def update(self, _: Calculation) -> None:
        """
        Save the full calculation history to a CSV file.

        :param _: The most recent Calculation (not used directly).
        """
        data = [{
            "operation": c.__class__.__name__,
            "operand1": c.a,
            "operand2": c.b,
            "result": c.result
        } for c in self.history]

        df = pd.DataFrame(data)
        df.to_csv(self.output_file, index=False, encoding=config.CALCULATOR_DEFAULT_ENCODING)
