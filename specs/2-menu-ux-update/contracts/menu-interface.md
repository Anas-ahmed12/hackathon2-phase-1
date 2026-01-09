# Menu Interface Contract: Menu-Driven UX for Phase-1 Todo App

## Menu Interface Specification

### Main Menu Display
- **Interface**: Display numbered menu options 1-7
- **Prompt**: "Enter choice (1-7):"
- **Behavior**: Shows after application start and after each operation
- **Success**: Menu options displayed clearly to user
- **Errors**: None for display

### Option 1: Add Todo
- **Input**: Menu selection (1) followed by todo description
- **Secondary Prompt**: "Enter todo description:"
- **Output**: Success message confirming addition
- **Success**: Todo added to list with incomplete status
- **Errors**:
  - Empty description: "Error: Todo description cannot be empty"

### Option 2: View Todos
- **Input**: Menu selection (2)
- **Output**: Formatted list of all todos with position and status
- **Success**: Display all todos in the format "position. [status] description"
- **Errors**: None (displays "No todos in the list." if empty)

### Option 3: Update Todo
- **Input**: Menu selection (3) followed by position and new description
- **Secondary Prompt**: "Enter todo position:" then "Enter new description:"
- **Output**: Success message confirming update
- **Success**: Todo at specified position is updated
- **Errors**:
  - Invalid position: "Error: Todo at that position does not exist"
  - Empty description: "Error: Todo description cannot be empty"

### Option 4: Delete Todo
- **Input**: Menu selection (4) followed by position
- **Secondary Prompt**: "Enter todo position:"
- **Output**: Success message confirming deletion
- **Success**: Todo at specified position is removed
- **Errors**:
  - Invalid position: "Error: Todo at that position does not exist"

### Option 5: Mark Todo Complete
- **Input**: Menu selection (5) followed by position
- **Secondary Prompt**: "Enter todo position:"
- **Output**: Success message confirming completion
- **Success**: Todo at specified position is marked as complete
- **Errors**:
  - Invalid position: "Error: Todo at that position does not exist"

### Option 6: Mark Todo Incomplete
- **Input**: Menu selection (6) followed by position
- **Secondary Prompt**: "Enter todo position:"
- **Output**: Success message confirming incompleteness
- **Success**: Todo at specified position is marked as incomplete
- **Errors**:
  - Invalid position: "Error: Todo at that position does not exist"

### Option 7: Exit
- **Input**: Menu selection (7)
- **Output**: Goodbye message
- **Success**: Application terminates gracefully
- **Errors**: None

### Error Handling
- **Invalid Menu Choice**: "Error: Please enter a number between 1 and 7"
- **Non-numeric Input**: "Error: Please enter a valid number"
- **General Error**: "An error occurred: [specific error message]"