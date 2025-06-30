from app.calculation import Calculation

class CalculatorMemento:
    """
    Stores the state (a calculation instance).
    """
    def __init__(self, state: Calculation):
        self._state = state

    def get_state(self) -> Calculation:
        return self._state


class MementoManager:
    """
    Manages undo and redo stacks using mementos.
    """
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save_state(self, state: Calculation):
        self._undo_stack.append(CalculatorMemento(state))
        self._redo_stack.clear()  # Clear redo on new action

    def undo(self) -> Calculation:
        if not self._undo_stack:
            raise IndexError("Nothing to undo.")
        memento = self._undo_stack.pop()
        self._redo_stack.append(memento)
        return memento.get_state()

    def redo(self) -> Calculation:
        if not self._redo_stack:
            raise IndexError("Nothing to redo.")
        memento = self._redo_stack.pop()
        self._undo_stack.append(memento)
        return memento.get_state()

    def can_undo(self):
        return bool(self._undo_stack)

    def can_redo(self):
        return bool(self._redo_stack)
