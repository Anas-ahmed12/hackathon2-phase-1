# Data Model: In-Memory Console Todo App (Phase I)

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
- Incomplete → Complete: When user marks todo as complete
- Complete → Incomplete: When user marks todo as incomplete

## In-Memory Storage Structure

**Name**: TodoList
**Description**: In-memory collection of Todo entities
**Structure**: List of Todo objects with integer indices serving as IDs
**Operations Supported**:
- Add new todo to the list
- Retrieve all todos
- Update todo by index
- Delete todo by index
- Mark todo as complete by index
- Mark todo as incomplete by index

**Constraints**:
- No persistence (data exists only in memory during application runtime)
- Single-user, single-session
- Maximum recommended size: 1000 items (for performance)