import sys
import readline  # Enables command history and editing features
from typing import List
from app.calculation import Calculation, CalculationFactory
from app.logger import LoggingObserver
from app.autosave import AutoSaveObserver


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
    print("  help              - Display this help message")
    print("  exit              - Exit the calculator")


def parse_command(command: str) -> List[str]:
    """
    Parse the command input into a list of arguments.

    :param command: The command string to parse.
    :return: A list of command arguments.
    """
    return command.strip().split()


def display_history(history: List[Calculation]) -> None:
    """
    Display the command history using readline module.

    :param history: List of Calculation objects (not used directly here).
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
    observers = [LoggingObserver(), AutoSaveObserver(history)]

    while True:
        try:
            userinput: str = input("Enter command (or 'help' for options): ")
            if not userinput.strip():
                continue

            cmd = parse_command(userinput)
            if not cmd:
                continue

            cmd_name = cmd[0].lower()

            if cmd_name == "help":
                display_help()

            elif cmd_name == "exit":
                print("Exiting the calculator. Goodbye!")
                sys.exit(0)

            elif cmd_name in ["add", "subtract", "multiply", "divide"]:
                if len(cmd) != 3:
                    print(f"Usage: {cmd_name} <a> <b>")
                    continue

                try:
                    a = float(cmd[1])
                    b = float(cmd[2])
                    calc = CalculationFactory.create_calculation(cmd_name, a, b)
                    result = calc.execute()
                    calc.result = result  # Attach result dynamically
                    print(f"Result: {result}")
                    history.append(calc)

                    for observer in observers:
                        observer.update(calc)

                except ValueError:
                    print("Invalid numbers provided.")
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
    calculator()
