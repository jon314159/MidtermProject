import pandas as pd
from typing import List
from app.calculation import Calculation
from app.history import HistoryObserver


class AutoSaveObserver(HistoryObserver):
    """
    Automatically saves the list of calculations to a CSV file.
    """

    def __init__(self, history: List[Calculation], output_file: str = "history.csv"):
        self.history = history
        self.output_file = output_file

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
        df.to_csv(self.output_file, index=False)
