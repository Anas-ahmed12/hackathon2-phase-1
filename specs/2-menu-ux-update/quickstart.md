# Quickstart: Menu-Driven UX for Phase-1 Todo App

## Running the Application

1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project directory
3. Run the application:
   ```bash
   python src/cli/todo_app.py
   ```

## Menu Options

The application presents a numeric menu with the following options:

1. **Add Todo** - Add a new todo with description
2. **View Todos** - Display all todos with their status
3. **Update Todo** - Update an existing todo by position
4. **Delete Todo** - Delete a todo by position
5. **Mark Todo Complete** - Mark a todo as complete by position
6. **Mark Todo Incomplete** - Mark a todo as incomplete by position
7. **Exit** - Quit the application

## Example Usage

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

## Error Handling

The application provides clear error messages for invalid operations:
- Non-numeric input at menu prompt
- Menu choices outside the 1-7 range
- Invalid todo positions
- Empty todo descriptions