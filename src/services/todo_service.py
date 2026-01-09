"""
Todo service for the console todo application.
Provides business logic for todo operations.
"""

from typing import List, Optional
from ..models.todo import Todo
from ..state.memory_store import MemoryStore


class TodoService:
    """
    Service layer for todo operations.
    Handles all business logic for todo management.
    """

    def __init__(self):
        """Initialize the todo service with in-memory storage."""
        self.storage = MemoryStore()

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo to the list with incomplete status.

        Args:
            title (str): The title/description of the todo

        Returns:
            Todo: The newly created Todo object
        """
        return self.storage.add_todo(title)

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todos in the list.

        Returns:
            List[Todo]: A copy of the list of all todos
        """
        return self.storage.get_all_todos()

    def update_todo(self, position: int, new_title: str) -> Optional[Todo]:
        """
        Update the title of a todo at the specified position.

        Args:
            position (int): One-based position of the todo to update
            new_title (str): New title for the todo

        Returns:
            Todo or None: The updated Todo object or None if position is invalid

        Raises:
            ValueError: If the position is invalid (less than 1 or greater than list length)
            ValueError: If the new title is empty
        """
        if position < 1:
            raise ValueError(f"Todo at position {position} does not exist")

        # Convert from one-based position to zero-based index
        index = position - 1

        try:
            return self.storage.update_todo(index, new_title)
        except IndexError:
            raise ValueError(f"Todo at position {position} does not exist")

    def delete_todo(self, position: int) -> bool:
        """
        Delete a todo at the specified position.

        Args:
            position (int): One-based position of the todo to delete

        Returns:
            bool: True if deletion was successful, False if position was invalid

        Raises:
            ValueError: If the position is invalid (less than 1 or greater than list length)
        """
        if position < 1:
            raise ValueError(f"Todo at position {position} does not exist")

        # Convert from one-based position to zero-based index
        index = position - 1

        try:
            return self.storage.delete_todo(index)
        except IndexError:
            raise ValueError(f"Todo at position {position} does not exist")

    def mark_complete(self, position: int) -> Optional[Todo]:
        """
        Mark a todo as complete at the specified position.

        Args:
            position (int): One-based position of the todo to mark complete

        Returns:
            Todo or None: The updated Todo object or None if position is invalid

        Raises:
            ValueError: If the position is invalid (less than 1 or greater than list length)
        """
        if position < 1:
            raise ValueError(f"Todo at position {position} does not exist")

        # Convert from one-based position to zero-based index
        index = position - 1

        try:
            return self.storage.mark_complete(index)
        except IndexError:
            raise ValueError(f"Todo at position {position} does not exist")

    def mark_incomplete(self, position: int) -> Optional[Todo]:
        """
        Mark a todo as incomplete at the specified position.

        Args:
            position (int): One-based position of the todo to mark incomplete

        Returns:
            Todo or None: The updated Todo object or None if position is invalid

        Raises:
            ValueError: If the position is invalid (less than 1 or greater than list length)
        """
        if position < 1:
            raise ValueError(f"Todo at position {position} does not exist")

        # Convert from one-based position to zero-based index
        index = position - 1

        try:
            return self.storage.mark_incomplete(index)
        except IndexError:
            raise ValueError(f"Todo at position {position} does not exist")

    def get_count(self) -> int:
        """
        Get the total number of todos.

        Returns:
            int: The count of todos in the list
        """
        return self.storage.get_count()