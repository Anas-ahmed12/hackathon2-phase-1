# Data Model: Menu-Driven UX for Phase-1 Todo App

## Todo Entity

**Name**: Todo
**Description**: A task item that contains a description text and a completion status
**Fields**:
- `id` (int): Unique identifier for the todo (based on position in the list)
- `title` (str): The description text of the todo
- `completed` (bool): Status indicating whether the todo is completed (True) or incomplete (False)

**Validation Rules**:
- `title` must not be empty or None
- `id` must be a positive integer
- `completed` must be a boolean value

**State Transitions**:
- Incomplete → Complete: When user marks todo as complete via menu option 5
- Complete → Incomplete: When user marks todo as incomplete via menu option 6

## Menu System Structure

**Name**: Menu System
**Description**: Interactive numeric interface for user input with options 1-7
**Structure**: Numeric input mapping to specific application functions
**Operations Supported**:
- Option 1: Add new todo
- Option 2: View all todos
- Option 3: Update existing todo
- Option 4: Delete todo
- Option 5: Mark todo as complete
- Option 6: Mark todo as incomplete
- Option 7: Exit application

**Constraints**:
- Input must be numeric (1-7 for main menu)
- Invalid input handled gracefully with error messages
- No free-text command parsing (replaced by menu system)