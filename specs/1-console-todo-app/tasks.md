---
description: "Task list for In-Memory Console Todo App implementation"
---

# Tasks: In-Memory Console Todo App (Phase I)

**Input**: Design documents from `/specs/1-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan with src/, tests/ directories
- [X] T002 [P] Create directory structure: src/models/, src/services/, src/state/, src/cli/
- [X] T003 [P] Initialize Python project with proper configuration files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Create base Todo data model in src/models/todo.py
- [X] T005 [P] Implement in-memory storage in src/state/memory_store.py
- [X] T006 [P] Create todo service interface in src/services/todo_service.py
- [X] T007 Create basic CLI framework in src/cli/todo_app.py
- [X] T008 Configure error handling infrastructure
- [X] T009 Setup basic project configuration and dependencies

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Todos (Priority: P1) 🎯 MVP

**Goal**: Users can add new todos with text descriptions and view all todos in a list format

**Independent Test**: Can be fully tested by adding a few todos and viewing the list to verify they appear correctly. This provides the basic value of a todo application.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Unit test for Todo model in tests/unit/test_todo.py
- [ ] T011 [P] [US1] Integration test for add todo functionality in tests/integration/test_add_todo.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement Todo model with id, title, completed fields in src/models/todo.py
- [X] T013 [US1] Implement add_todo method in src/services/todo_service.py
- [X] T014 [US1] Implement get_all_todos method in src/services/todo_service.py
- [X] T015 [US1] Implement add command in src/cli/todo_app.py
- [X] T016 [US1] Implement list command in src/cli/todo_app.py
- [X] T017 [US1] Add validation for empty todo descriptions

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update and Delete Todos (Priority: P2)

**Goal**: Users can update existing todo descriptions by position and delete todos by position

**Independent Test**: Can be tested by adding a todo, updating its content, and verifying the change. Also test deleting a todo and confirming it no longer appears in the list.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Unit test for update todo functionality in tests/unit/test_todo_service.py
- [ ] T019 [P] [US2] Unit test for delete todo functionality in tests/unit/test_todo_service.py

### Implementation for User Story 2

- [X] T020 [P] [US2] Implement update_todo method in src/services/todo_service.py
- [X] T021 [P] [US2] Implement delete_todo method in src/services/todo_service.py
- [X] T022 [US2] Implement update command in src/cli/todo_app.py
- [X] T023 [US2] Implement delete command in src/cli/todo_app.py
- [X] T024 [US2] Add validation for invalid position access
- [X] T025 [US2] Add error handling for update/delete operations

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todos Complete/Incomplete (Priority: P3)

**Goal**: Users can mark todos as complete by position and mark completed todos as incomplete by position

**Independent Test**: Can be tested by marking a todo as complete, viewing the list to confirm the status is shown, then marking it incomplete again.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T026 [P] [US3] Unit test for complete todo functionality in tests/unit/test_todo_service.py
- [ ] T027 [P] [US3] Unit test for incomplete todo functionality in tests/unit/test_todo_service.py

### Implementation for User Story 3

- [X] T028 [P] [US3] Implement mark_complete method in src/services/todo_service.py
- [X] T029 [P] [US3] Implement mark_incomplete method in src/services/todo_service.py
- [X] T030 [US3] Implement complete command in src/cli/todo_app.py
- [X] T031 [US3] Implement incomplete command in src/cli/todo_app.py
- [X] T032 [US3] Update list command to show completion status in src/cli/todo_app.py
- [X] T033 [US3] Add validation for position access in complete/incomplete operations

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T034 [P] Add help command implementation in src/cli/todo_app.py
- [X] T035 [P] Add exit/quit command implementation in src/cli/todo_app.py
- [X] T036 [P] Add comprehensive error handling for all edge cases
- [X] T037 [P] Add input validation and sanitization
- [X] T038 [P] Add proper exit codes and graceful shutdown
- [X] T039 [P] Documentation updates in README.md
- [X] T040 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model in tests/unit/test_todo.py"
Task: "Integration test for add todo functionality in tests/integration/test_add_todo.py"

# Launch all models for User Story 1 together:
Task: "Implement Todo model with id, title, completed fields in src/models/todo.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence