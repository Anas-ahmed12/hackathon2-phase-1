# CLI Command Contracts: In-Memory Console Todo App (Phase I)

## Command Interface Specification

### Add Todo Command
- **Command**: `add "description"`
- **Input**: String description of the todo
- **Output**: Confirmation message with added todo
- **Success**: Todo is added to the list with incomplete status
- **Errors**:
  - Empty description: "Error: Todo description cannot be empty"

### List Todos Command
- **Command**: `list`
- **Input**: None
- **Output**: Formatted list of all todos with position and status
- **Success**: Display all todos in the format "position. [status] description"
- **Errors**: None

### Update Todo Command
- **Command**: `update <position> "new description"`
- **Input**: Integer position and string new description
- **Output**: Confirmation message with updated todo
- **Success**: Todo at specified position is updated
- **Errors**:
  - Invalid position: "Error: Todo at position X does not exist"
  - Empty description: "Error: Todo description cannot be empty"

### Delete Todo Command
- **Command**: `delete <position>`
- **Input**: Integer position
- **Output**: Confirmation message
- **Success**: Todo at specified position is removed
- **Errors**:
  - Invalid position: "Error: Todo at position X does not exist"

### Complete Todo Command
- **Command**: `complete <position>`
- **Input**: Integer position
- **Output**: Confirmation message
- **Success**: Todo at specified position is marked as complete
- **Errors**:
  - Invalid position: "Error: Todo at position X does not exist"

### Incomplete Todo Command
- **Command**: `incomplete <position>`
- **Input**: Integer position
- **Output**: Confirmation message
- **Success**: Todo at specified position is marked as incomplete
- **Errors**:
  - Invalid position: "Error: Todo at position X does not exist"

### Help Command
- **Command**: `help`
- **Input**: None
- **Output**: List of all available commands with descriptions
- **Success**: Display help information
- **Errors**: None

### Exit Command
- **Command**: `exit` or `quit`
- **Input**: None
- **Output**: Exit confirmation
- **Success**: Application terminates
- **Errors**: None