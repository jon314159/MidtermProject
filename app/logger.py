import logging
from app.calculation import Calculation
from app.history import HistoryObserver
import os
from app import config

log_file = os.path.join(config.CALCULATOR_LOG_DIR, "calculator.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

class LoggingObserver(HistoryObserver):
    """
    Logs calculations to a file using Python's logging module.
    """

    def __init__(self, log_file: str = "calculator.log"):
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def update(self, calc: Calculation) -> None:
        """
        Log the performed calculation to the log file.

        :param calc: The Calculation object with operands and result.
        """
        message = f"Calculation performed: {calc.__class__.__name__} ({calc.a}, {calc.b}) = {calc.result}"
        logging.info(message)
