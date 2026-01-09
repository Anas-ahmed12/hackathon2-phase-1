"""
Todo data model for the console todo application.
"""

class Todo:
    """
    Represents a todo item with an ID, title, and completion status.
    """

    def __init__(self, id: int, title: str, completed: bool = False):
        """
        Initialize a Todo object.

        Args:
            id (int): Unique identifier for the todo (based on position in the list)
            title (str): The description text of the todo
            completed (bool): Status indicating whether the todo is completed (True) or incomplete (False)
        """
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID must be a positive integer")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")
        if not isinstance(completed, bool):
            raise ValueError("Completed must be a boolean value")

        self.id = id
        self.title = title.strip()
        self.completed = completed

    def __repr__(self):
        return f"Todo(id={self.id}, title='{self.title}', completed={self.completed})"

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return False
        return self.id == other.id and self.title == other.title and self.completed == other.completed