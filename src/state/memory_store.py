"""
In-memory storage for the console todo application.
"""

from typing import List, Optional
from ..models.todo import Todo


class MemoryStore:
    """
    In-memory storage for todos using a list structure.
    No persistence (data exists only in memory during application runtime).
    Single-user, single-session.
    """

    def __init__(self):
        """Initialize the in-memory storage."""
        self._todos: List[Todo] = []
        self._next_id = 1

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo to the list with incomplete status.

        Args:
            title (str): The title/description of the todo

        Returns:
            Todo: The newly created Todo object
        """
        if not title or not title.strip():
            raise ValueError("Todo title cannot be empty")

        # Create a new todo with the next available ID
        new_todo = Todo(id=self._next_id, title=title.strip(), completed=False)
        self._todos.append(new_todo)

        # Increment the ID counter for the next todo
        self._next_id += 1

        return new_todo

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todos in the list.

        Returns:
            List[Todo]: A copy of the list of all todos
        """
        return self._todos.copy()

    def get_todo_by_index(self, index: int) -> Optional[Todo]:
        """
        Get a todo by its zero-based index in the list.

        Args:
            index (int): Zero-based index of the todo

        Returns:
            Todo or None: The todo at the specified index or None if index is invalid
        """
        if 0 <= index < len(self._todos):
            return self._todos[index]
        return None

    def update_todo(self, index: int, new_title: str) -> Todo:
        """
        Update the title of a todo at the specified index.

        Args:
            index (int): Zero-based index of the todo to update
            new_title (str): New title for the todo

        Returns:
            Todo: The updated Todo object

        Raises:
            IndexError: If the index is out of bounds
            ValueError: If the new title is empty
        """
        if not new_title or not new_title.strip():
            raise ValueError("Todo title cannot be empty")

        if not (0 <= index < len(self._todos)):
            raise IndexError(f"Todo at index {index} does not exist")

        self._todos[index].title = new_title.strip()
        return self._todos[index]

    def delete_todo(self, index: int) -> bool:
        """
        Delete a todo at the specified index.

        Args:
            index (int): Zero-based index of the todo to delete

        Returns:
            bool: True if deletion was successful, False if index was invalid

        Raises:
            IndexError: If the index is out of bounds
        """
        if not (0 <= index < len(self._todos)):
            raise IndexError(f"Todo at index {index} does not exist")

        self._todos.pop(index)
        return True

    def mark_complete(self, index: int) -> Todo:
        """
        Mark a todo as complete at the specified index.

        Args:
            index (int): Zero-based index of the todo to mark complete

        Returns:
            Todo: The updated Todo object

        Raises:
            IndexError: If the index is out of bounds
        """
        if not (0 <= index < len(self._todos)):
            raise IndexError(f"Todo at index {index} does not exist")

        self._todos[index].completed = True
        return self._todos[index]

    def mark_incomplete(self, index: int) -> Todo:
        """
        Mark a todo as incomplete at the specified index.

        Args:
            index (int): Zero-based index of the todo to mark incomplete

        Returns:
            Todo: The updated Todo object

        Raises:
            IndexError: If the index is out of bounds
        """
        if not (0 <= index < len(self._todos)):
            raise IndexError(f"Todo at index {index} does not exist")

        self._todos[index].completed = False
        return self._todos[index]

    def get_count(self) -> int:
        """
        Get the total number of todos.

        Returns:
            int: The count of todos in the list
        """
        return len(self._todos)