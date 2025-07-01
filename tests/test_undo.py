import pytest
from unittest.mock import patch, MagicMock
from app.calculator_memento import MementoManager
import pandas as pd
from app.calculation import CalculationFactory
from app.calculator import calculator

@pytest.fixture
def manager():
    return MementoManager()

@pytest.fixture
def mock_calc():
    mock = MagicMock()
    mock.a = 5
    mock.b = 3
    mock.result = 8
    mock.__class__.__name__ = "Addition"
    return mock

def test_save_state_allows_undo(manager, mock_calc):
    assert not manager.can_undo()
    manager.save_state(mock_calc)
    assert manager.can_undo()

def test_undo_returns_last_calc(manager, mock_calc):
    manager.save_state(mock_calc)
    result = manager.undo()
    assert result == mock_calc
    assert manager.can_redo()

def test_redo_restores_calc(manager, mock_calc):
    manager.save_state(mock_calc)
    manager.undo()
    restored = manager.redo()
    assert restored == mock_calc
    assert manager.can_undo()

def test_undo_without_history_raises(manager):
    with pytest.raises(IndexError, match="Nothing to undo"):
        manager.undo()

def test_redo_without_undo_raises(manager):
    with pytest.raises(IndexError, match="Nothing to redo"):
        manager.redo()

def test_redo_stack_clears_on_new_action(manager, mock_calc):
    manager.save_state(mock_calc)
    manager.undo()
    assert manager.can_redo()
    manager.save_state(mock_calc)
    assert not manager.can_redo()

# --------- Test Save Command ---------
@patch("builtins.input", side_effect=["add 1 2", "save", "exit"])
@patch("sys.exit", side_effect=SystemExit)
def test_save_command(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "History saved." in output

# --------- Test Load Command ---------
@patch("builtins.input", side_effect=["load", "exit"])
@patch("pandas.read_csv")
@patch("sys.exit", side_effect=SystemExit)
def test_load_command(mock_exit, mock_read_csv, mock_input, capsys):
    mock_read_csv.return_value = pd.DataFrame({"operation": ["add"], "operand1": [1], "operand2": [2], "result": [3]})
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "operation" in output or "add" in output

# --------- Test Missing Argument ---------
@patch("builtins.input", side_effect=["add 1", "exit"])
@patch("sys.exit", side_effect=SystemExit)
def test_add_missing_argument(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "Usage: add <a> <b>" in output

# --------- Test Generic Exception ---------
@patch("app.calculation.CalculationFactory.create_calculation")
@patch("builtins.input", side_effect=["add 1 2", "exit"])
@patch("sys.exit", side_effect=SystemExit)
def test_generic_exception_handling(mock_exit, mock_input, mock_create):
    mock_create.side_effect = Exception("unexpected")
    with pytest.raises(SystemExit):
        calculator()

# --------- Test Unknown Command ---------
@patch("builtins.input", side_effect=["foobar", "exit"])
@patch("sys.exit", side_effect=SystemExit)
def test_unknown_command(mock_exit, mock_input, capsys):
    with pytest.raises(SystemExit):
        calculator()
    output = capsys.readouterr().out
    assert "Unknown command" in output
