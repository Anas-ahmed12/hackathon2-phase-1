#!/usr/bin/env python3
"""
Menu-Driven Console Todo Application
"""

import sys
from typing import Optional
from ..services.todo_service import TodoService


class TodoApp:
    """
    Menu-driven CLI application for managing todos.
    """

    def __init__(self):
        """Initialize the todo application."""
        self.service = TodoService()
        self.running = True

    def run(self):
        """Start the main application loop."""
        print("Welcome to the Console Todo App!")

        while self.running:
            try:
                # Display menu and get user choice
                self.display_menu()
                choice = self.get_numeric_input("Enter choice (1-7): ", 1, 7)

                if choice is None:
                    continue

                # Route to appropriate handler
                if choice == 1:
                    self.handle_add()
                elif choice == 2:
                    self.handle_view()
                elif choice == 3:
                    self.handle_update()
                elif choice == 4:
                    self.handle_delete()
                elif choice == 5:
                    self.handle_complete()
                elif choice == 6:
                    self.handle_incomplete()
                elif choice == 7:
                    self.handle_exit()

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def display_menu(self):
        """Display the main menu options."""
        menu_text = """
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo Complete
6. Mark Todo Incomplete
7. Exit
        """.strip()
        print(menu_text)

    def get_numeric_input(self, prompt: str, min_val: int, max_val: int) -> Optional[int]:
        """
        Get numeric input from user within specified range.

        Args:
            prompt (str): Prompt to display to user
            min_val (int): Minimum acceptable value
            max_val (int): Maximum acceptable value

        Returns:
            Optional[int]: The numeric input or None if invalid
        """
        try:
            user_input = input(prompt).strip()

            # Check if input is numeric
            if not user_input.isdigit():
                print("Error: Please enter a valid number")
                return None

            num = int(user_input)

            # Check if in valid range
            if num < min_val or num > max_val:
                print(f"Error: Please enter a number between {min_val} and {max_val}")
                return None

            return num
        except ValueError:
            print("Error: Please enter a valid number")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_text_input(self, prompt: str) -> Optional[str]:
        """
        Get text input from user.

        Args:
            prompt (str): Prompt to display to user

        Returns:
            Optional[str]: The text input or None if invalid
        """
        try:
            user_input = input(prompt).strip()
            return user_input
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def handle_add(self):
        """Handle adding a new todo."""
        description = self.get_text_input("Enter todo description: ")

        if not description:
            print("Error: Todo description cannot be empty")
            return

        try:
            todo = self.service.add_todo(description)
            print(f"Todo added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_view(self):
        """Handle viewing all todos."""
        try:
            todos = self.service.get_all_todos()

            if not todos:
                print("No todos in the list.")
                return

            for i, todo in enumerate(todos, 1):
                status = "x" if todo.completed else " "
                print(f"{i}. [{status}] {todo.title}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_update(self):
        """Handle updating a todo."""
        # Get position
        position = self.get_numeric_input("Enter todo position: ", 1, self.service.get_count())

        if position is None:
            return

        # Get new description
        new_description = self.get_text_input("Enter new description: ")

        if not new_description:
            print("Error: Todo description cannot be empty")
            return

        try:
            updated_todo = self.service.update_todo(position, new_description)
            print("Todo updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_delete(self):
        """Handle deleting a todo."""
        if self.service.get_count() == 0:
            print("No todos to delete.")
            return

        position = self.get_numeric_input("Enter todo position: ", 1, self.service.get_count())

        if position is None:
            return

        try:
            result = self.service.delete_todo(position)
            if result:
                print("Todo deleted successfully!")
            else:
                print("Error: Failed to delete todo")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_complete(self):
        """Handle marking a todo as complete."""
        if self.service.get_count() == 0:
            print("No todos to mark complete.")
            return

        position = self.get_numeric_input("Enter todo position: ", 1, self.service.get_count())

        if position is None:
            return

        try:
            todo = self.service.mark_complete(position)
            print("Todo marked as complete!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_incomplete(self):
        """Handle marking a todo as incomplete."""
        if self.service.get_count() == 0:
            print("No todos to mark incomplete.")
            return

        position = self.get_numeric_input("Enter todo position: ", 1, self.service.get_count())

        if position is None:
            return

        try:
            todo = self.service.mark_incomplete(position)
            print("Todo marked as incomplete!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def handle_exit(self):
        """Handle exiting the application."""
        print("Goodbye!")
        self.running = False


def main():
    """Main entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()