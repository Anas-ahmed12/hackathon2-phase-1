"""
Basic tests for the console todo application.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.services.todo_service import TodoService


def test_basic_functionality():
    """Test all basic functionality of the todo service."""
    service = TodoService()

    # Test 1: Add todos
    todo1 = service.add_todo("Buy groceries")
    todo2 = service.add_todo("Walk the dog")
    assert service.get_count() == 2, f"Expected 2 todos, got {service.get_count()}"

    # Test 2: List todos
    todos = service.get_all_todos()
    assert len(todos) == 2, f"Expected 2 todos in list, got {len(todos)}"

    # Test 3: Update todo
    updated = service.update_todo(1, "Buy food")
    assert updated.title == "Buy food", f"Expected 'Buy food', got '{updated.title}'"

    # Test 4: Delete todo
    result = service.delete_todo(2)
    assert result is True, f"Expected True, got {result}"
    assert service.get_count() == 1, f"Expected 1 todo after deletion, got {service.get_count()}"

    # Test 5: Mark complete
    completed = service.mark_complete(1)
    assert completed.completed is True, f"Expected True, got {completed.completed}"

    # Test 6: Mark incomplete
    incomplete = service.mark_incomplete(1)
    assert incomplete.completed is False, f"Expected False, got {incomplete.completed}"

    print("✅ All tests passed!")


if __name__ == "__main__":
    test_basic_functionality()