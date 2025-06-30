import pytest
from unittest.mock import MagicMock
from app.calculator_memento import MementoManager, CalculatorMemento

# --------- Fixtures ---------
@pytest.fixture
def mock_calc():
    mock = MagicMock()
    mock.string.return_value = "MockCalculation(2, 3)"
    return mock

@pytest.fixture
def manager():
    return MementoManager()


# --------- Save & Undo ---------
def test_save_and_undo(manager, mock_calc):
    manager.save_state(mock_calc)
    assert manager.can_undo()
    undone = manager.undo()
    assert undone == mock_calc
    assert manager.can_redo()


def test_undo_then_redo(manager, mock_calc):
    manager.save_state(mock_calc)
    undone = manager.undo()
    redone = manager.redo()
    assert redone == mock_calc
    assert manager.can_undo()
    assert not manager.can_redo()


# --------- Exceptions ---------
def test_undo_empty_stack_raises(manager):
    with pytest.raises(IndexError, match="Nothing to undo"):
        manager.undo()

def test_redo_empty_stack_raises(manager):
    with pytest.raises(IndexError, match="Nothing to redo"):
        manager.redo()


# --------- Stack State Reset ---------
def test_redo_stack_clears_after_new_save(manager, mock_calc):
    manager.save_state(mock_calc)
    manager.undo()
    assert manager.can_redo()
    
    # Save a new state — redo should be cleared
    manager.save_state(mock_calc)
    assert not manager.can_redo()
