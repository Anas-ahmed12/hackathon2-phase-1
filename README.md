# Menu-Driven In-Memory Console Todo App (Phase I)

A simple menu-driven console-based todo application that stores all data in memory. This is Phase I of a multi-phase todo application project with a numeric menu interface.

## Features

- Add new todos with text descriptions
- View all todos in a list format
- Update existing todo descriptions by position
- Delete todos by position
- Mark todos as complete/incomplete by position
- All data stored in memory only (no persistence)
- Menu-driven numeric UX (options 1-7)

## Requirements

- Python 3.8+

## Usage

Run the application:

```bash
python src/cli/todo_app.py
```

### Menu Options

The application presents a numeric menu with the following options:

1. **Add Todo** - Add a new todo with description
2. **View Todos** - Display all todos with their status
3. **Update Todo** - Update an existing todo by position
4. **Delete Todo** - Delete a todo by position
5. **Mark Todo Complete** - Mark a todo as complete by position
6. **Mark Todo Incomplete** - Mark a todo as incomplete by position
7. **Exit** - Quit the application

### Example Usage

```
Welcome to the Console Todo App!

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo Complete
6. Mark Todo Incomplete
7. Exit
Enter choice (1-7): 1
Enter todo description: Buy groceries
Todo added successfully!

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo Complete
6. Mark Todo Incomplete
7. Exit
Enter choice (1-7): 2
1. [ ] Buy groceries

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo Complete
6. Mark Todo Incomplete
7. Exit
Enter choice (1-7): 5
Enter todo position: 1
Todo marked as complete!

1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo Complete
6. Mark Todo Incomplete
7. Exit
Enter choice (1-7): 7
Goodbye!
```

## Architecture

The application follows a layered architecture:

- **CLI Layer**: Menu-driven interface with numeric input handling (`src/cli/todo_app.py`)
- **Service Layer**: Implements todo operations (`src/services/todo_service.py`)
- **State Layer**: In-memory todo list (single source of truth) (`src/state/memory_store.py`)
- **Model Layer**: Defines the Todo data model (`src/models/todo.py`)

## Project Structure

```
src/
├── models/
│   └── todo.py          # Todo data model
├── services/
│   └── todo_service.py  # Todo operations service
├── state/
│   └── memory_store.py  # In-memory state management
└── cli/
    └── todo_app.py      # Menu-driven CLI interface
```# hackathon2-phase-1
# hackathon2-phase-1
