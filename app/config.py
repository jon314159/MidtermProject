import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

CALCULATOR_LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
CALCULATOR_HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "history")

CALCULATOR_MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
CALCULATOR_AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"

CALCULATOR_PRECISION = int(os.getenv("CALCULATOR_PRECISION", "2"))
CALCULATOR_MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000"))
CALCULATOR_DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
