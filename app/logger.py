import logging
import os
from app import config
from app.calculation import Calculation
from app.history import HistoryObserver

# ✅ Ensure the log directory exists before setting up logging
os.makedirs(config.CALCULATOR_LOG_DIR, exist_ok=True)

log_file = os.path.join(config.CALCULATOR_LOG_DIR, "calculator.log")

# ✅ Configure logging once at module level
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

class LoggingObserver(HistoryObserver):
    """
    Logs calculations to a file using Python's logging module.
    """

    def __init__(self, log_file: str = log_file): # pragama: no cover
        self.log_file = log_file  # pragma: no cover

    def update(self, calc: Calculation) -> None:
        """
        Log the performed calculation to the log file.

        :param calc: The Calculation object with operands and result.
        """
        message = f"Calculation performed: {calc.__class__.__name__} ({calc.a}, {calc.b}) = {calc.result}"  # pragma: no cover
        logging.info(message)  # pragma: no cover
