"""
Command-line interface for the calculator.

Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
for commands, processes arithmetic operations, and manages calculation history.
"""

import sys
import os
import readline  # Enables command history and editing features
from typing import List, Optional
import pandas as pd
from app.calculation import Calculation, CalculationFactory
from app.logger import LoggingObserver
from app.autosave import AutoSaveObserver
from app.history import HistoryObserver
from app.calculator_memento import MementoManager
import app.calculation_operations  # Ensures all @register_calculation decorators run
import app.config as config

def display_help():
    """
    Display the help message for the calculator.
    """
    print("Welcome to the Calculator!")
    print("Available commands:")
    print("  add <a> <b>       - Add two numbers")
    print("  subtract <a> <b>  - Subtract second number from first")
    print("  multiply <a> <b>  - Multiply two numbers")
    print("  divide <a> <b>    - Divide first number by second (cannot divide by zero)")
    print("  power <a> <b>     - Raise first number to the power of second")
    print("  root <a> <b>      - Calculate the b-th root of a")
    print("  modulus <a> <b>   - Calculate the modulus of a by b")
    print("  int_divide <a> <b> - Calculate the integer division of a by b")
    print("  percent <a> <b>   - Calculate b percent of a")
    print("  abs_diff <a> <b>  - Calculate the absolute difference between a and b")
    print("  history           - Show command history")
    print("  undo              - Undo the last operation")
    print("  redo              - Redo the last undone operation")
    print("  clear             - Clear the command history")
    print("  save              - Save the command history to a file")
    print("  load              - Load command history from a file")
    print("  help              - Display this help message")
    print("  exit              - Exit the calculator")

def parse_command(command: str) -> List[str]:
    """
    Parse the command input into a list of arguments.

    :param command: The command string to parse.
    :type command: str
    :return: A list of command arguments.
    :rtype: List[str]
    """
    return command.strip().split()

def display_history(history: List[Calculation]) -> None:
    """
    Display the command history.
    """
    print("Command History:")
    for i, cmd in enumerate(
        readline.get_history_item(i) for i in range(1, readline.get_current_history_length() + 1)
    ):
        print(f"{i}: {cmd}")

def calculator() -> None:
    """
    Main calculator loop.
    Accepts user commands and executes calculations or utility actions.
    """
    history: List[Calculation] = []
    observers: List[HistoryObserver] = []
    memento_manager = MementoManager()

    if config.CALCULATOR_AUTO_SAVE:
        observers.append(AutoSaveObserver(history))

    while True:
        try:
            userinput: str = input("Enter command (or 'help' for options): ")
            if not userinput.strip():
                continue

            cmd = parse_command(userinput)
            if not cmd:
                continue #pragma: no cover

            cmd_name = cmd[0].lower()

            if cmd_name == "help":
                display_help()

            elif cmd_name == "exit":
                print("Exiting the calculator. Goodbye!")
                sys.exit(0)

            elif cmd_name == "history":
                display_history(history)

            elif cmd_name == "undo":
                if not memento_manager.can_undo():
                    print("Nothing to undo.")
                    continue
                undone_calc = memento_manager.undo()
                if undone_calc in history:
                    history.remove(undone_calc)
                    print("Undid last operation.")

            elif cmd_name == "redo":
                if not memento_manager.can_redo():
                    print("Nothing to redo.")
                    continue
                redone_calc = memento_manager.redo()
                history.append(redone_calc)
                print("Redid operation.")

            elif cmd_name == "clear":
                history.clear()
                print("History cleared.")

            elif cmd_name == "save":
                try:
                    for observer in observers:
                        if history:
                            observer.update(history[-1])
                    print("History saved.")
                except Exception as e:
                    print(f"Save failed: {e}")

            elif cmd_name == "load":
                try:
                    path = os.path.join(config.CALCULATOR_HISTORY_DIR, "history.csv")
                    df = pd.read_csv(path, encoding=config.CALCULATOR_DEFAULT_ENCODING)
                    print(df.to_string(index=False))
                except Exception as e:
                    print(f"Failed to load history: {e}")

            elif cmd_name in [
                "add", "subtract", "multiply", "divide", "power", "root",
                "modulus", "int_divide", "percent", "abs_diff"]:

                if len(cmd) != 3:
                    print(f"Usage: {cmd_name} <a> <b>")
                    continue

                try:
                    a = float(cmd[1])
                    b = float(cmd[2])
                    if abs(a) > config.CALCULATOR_MAX_INPUT_VALUE or abs(b) > config.CALCULATOR_MAX_INPUT_VALUE:
                        print("Input values exceed the maximum allowed.")
                        continue #pragma: no cover
                    calc = CalculationFactory.create_calculation(cmd_name, a, b)
                    result = round(calc.execute(), config.CALCULATOR_PRECISION)
                    calc.result = result
                    print(f"Result: {result}")
                    history.append(calc)
                    memento_manager.save_state(calc)

                    if len(history) > config.CALCULATOR_MAX_HISTORY_SIZE:
                        history.pop(0)

                    for observer in observers:
                        observer.update(calc)

                except ValueError as ve:
                    print(f"[ValueError] {ve}")
                    continue
                except Exception as e:
                    print(f"An error occurred: {e}")
                    continue

            else:
                print(f"Unknown command: {cmd_name}")

        except KeyboardInterrupt:
            print("\nExiting the calculator. Goodbye!")
            sys.exit(0)
        except EOFError:
            print("\nExiting the calculator. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    calculator() #pragma: no cover
