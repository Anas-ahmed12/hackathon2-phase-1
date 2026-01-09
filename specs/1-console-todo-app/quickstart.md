# Quickstart: In-Memory Console Todo App (Phase I)

## Running the Application

1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project directory
3. Run the application:
   ```bash
   python src/cli/todo_app.py
   ```

## Available Commands

- `add "todo description"` - Add a new todo
- `list` - View all todos with their status
- `update <position> "new description"` - Update a todo at the specified position
- `delete <position>` - Delete a todo at the specified position
- `complete <position>` - Mark a todo as complete
- `incomplete <position>` - Mark a todo as incomplete
- `help` - Show available commands
- `quit` or `exit` - Exit the application

## Example Usage

```
> add "Buy groceries"
Added: Buy groceries

> add "Walk the dog"
Added: Walk the dog

> list
1. [ ] Buy groceries
2. [ ] Walk the dog

> complete 1
Todo 1 marked as complete

> list
1. [x] Buy groceries
2. [ ] Walk the dog

> update 2 "Walk the cat"
Updated: Walk the cat

> list
1. [x] Buy groceries
2. [ ] Walk the cat

> delete 2
Todo 2 deleted

> list
1. [x] Buy groceries
```

## Error Handling

The application provides clear error messages for invalid operations:
- Attempting to access a todo at an invalid position
- Using incorrect command syntax
- Providing empty todo descriptions