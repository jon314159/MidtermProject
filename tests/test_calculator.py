import pytest
from unittest.mock import patch, MagicMock
from app.calculator import calculator, display_help, display_history


# --------- Helpers ---------
def infinite_inputs(*inputs):
    """Generator that supplies inputs indefinitely (prevents StopIteration)."""
    for item in inputs:
        yield item
    while True:
        yield ""  # fallback input


# --------- Basic Output Tests ---------
def test_display_help_output(capsys):
    display_help()
    output = capsys.readouterr().out
    assert "Welcome to the Calculator!" in output
    assert "add <a> <b>" in output
    assert "exit" in output


@patch("app.calculator.readline")
def test_display_history(mock_readline, capsys):
    mock_readline.get_current_history_length.return_value = 2
    mock_readline.get_history_item.side_effect = ["add 1 2", "multiply 3 4"]
    display_history([])
    output = capsys.readouterr().out
    assert "0: add 1 2" in output
    assert "1: multiply 3 4" in output


# --------- Command Handling ---------
@patch("builtins.input", side_effect=infinite_inputs("", "", "exit"))
@patch("sys.exit", side_effect=SystemExit)
def test_blank_input_then_exit(mock_exit, mock_input):
    with pytest.raises(SystemExit):
        calculator()
    mock_exit.assert_called_once()


@patch("builtins.input", side_effect=infinite_inputs("help", "exit"))
@patch("sys.exit", side_effect=SystemExit)
def test_help_then_exit(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "Welcome to the Calculator!" in output
    assert "Exiting the calculator" in output


@patch("builtins.input", side_effect=infinite_inputs("foobar 2 3", "exit"))
@patch("sys.exit", side_effect=SystemExit)
def test_unknown_command_then_exit(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "Unknown command: foobar" in output


@patch("builtins.input", side_effect=infinite_inputs("add 1", "exit"))
@patch("sys.exit", side_effect=SystemExit)
def test_missing_argument_count(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "Usage: add <a> <b>" in output


@patch("builtins.input", side_effect=infinite_inputs("add a b", "exit"))
@patch("sys.exit", side_effect=SystemExit)
def test_invalid_number_input(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "could not convert string to float" in output


@patch("app.calculation.CalculationFactory.create_calculation")
@patch("builtins.input", side_effect=infinite_inputs("add 2 3", "exit"))
@patch("sys.exit", side_effect=SystemExit)
def test_valid_add_command(mock_exit, mock_input, mock_create, capsys):
    mock_calc = MagicMock()
    mock_calc.execute.return_value = 5
    mock_create.return_value = mock_calc

    with pytest.raises(SystemExit):
        calculator()

    output = capsys.readouterr().out
    assert "Result: 5" in output
    mock_create.assert_called_once_with("add", 2.0, 3.0)
    mock_calc.execute.assert_called_once()


# --------- Interrupt Handling ---------
@patch("builtins.input", side_effect=KeyboardInterrupt)
@patch("sys.exit", side_effect=SystemExit)
def test_keyboard_interrupt_exit(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "Exiting the calculator" in output


@patch("builtins.input", side_effect=EOFError)
@patch("sys.exit", side_effect=SystemExit)
def test_eof_interrupt_exit(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "Exiting the calculator" in output

def test_observer_raises_generic_exception(monkeypatch, capsys):
    # Simulate user inputs:
    inputs = iter(["add 1 1", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Patch CalculationFactory to ensure it works
    from app.calculation import CalculationFactory
    calc = CalculationFactory.create_calculation("add", 1, 1)

    # Patch observers to raise a generic Exception
    bad_observer = MagicMock()
    bad_observer.update.side_effect = Exception("Something unexpected")

    with patch("app.calculator.LoggingObserver", return_value=bad_observer), \
         patch("app.calculator.AutoSaveObserver", return_value=bad_observer):
        with pytest.raises(SystemExit):  # exit command ends loop
            calculator()

    output = capsys.readouterr().out
    assert "An error occurred: Something unexpected" in output
