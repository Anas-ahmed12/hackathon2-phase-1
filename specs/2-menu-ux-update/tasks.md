---
description: "Task list for Menu-Based In-Memory Todo App implementation"
---

# Tasks: Menu-Based In-Memory Todo App

**Input**: Design documents from `/specs/2-menu-ux-update/`
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

- [X] T001 Update existing project structure if needed for menu UX
- [X] T002 [P] Verify existing src/ directory structure exists
- [X] T003 [P] Ensure Python project configuration is in place

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Verify existing Todo data model in src/models/todo.py
- [X] T005 [P] Verify existing in-memory storage in src/state/memory_store.py
- [X] T006 [P] Verify existing todo service in src/services/todo_service.py
- [X] T007 Create new menu-driven CLI framework in src/cli/todo_app.py
- [X] T008 Configure error handling infrastructure for menu system
- [X] T009 Update project dependencies if needed

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Navigate Menu System (Priority: P1) 🎯 MVP

**Goal**: Users can interact with the todo application using a simple numeric menu system. The user starts the application and sees a numbered menu, then selects options using numbers only. The menu appears after each action to allow continued interaction.

**Independent Test**: Can be fully tested by starting the application, seeing the menu, selecting option 7 to exit, and confirming the app exits properly. This validates the basic menu navigation system.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Unit test for menu display functionality in tests/unit/test_menu.py
- [ ] T011 [P] [US1] Integration test for menu navigation in tests/integration/test_menu_nav.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement menu display function in src/cli/todo_app.py
- [X] T013 [US1] Implement main menu loop with continuous display in src/cli/todo_app.py
- [X] T014 [US1] Implement numeric input handling for menu selection in src/cli/todo_app.py
- [X] T015 [US1] Implement menu option validation (1-7) in src/cli/todo_app.py
- [X] T016 [US1] Implement graceful handling of invalid menu input in src/cli/todo_app.py
- [X] T017 [US1] Implement exit functionality (option 7) in src/cli/todo_app.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Perform Basic Todo Operations (Priority: P2)

**Goal**: Users can add, view, and exit todos using the new menu system. The user selects menu options 1, 2, and 7 to perform these core operations.

**Independent Test**: Can be tested by adding a todo using menu option 1, viewing todos using menu option 2, and exiting using menu option 7. This validates the core todo functionality with the new UX.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Unit test for add todo via menu in tests/unit/test_menu_add.py
- [ ] T019 [P] [US2] Unit test for view todos via menu in tests/unit/test_menu_view.py

### Implementation for User Story 2

- [X] T020 [P] [US2] Implement option 1: Add Todo functionality in src/cli/todo_app.py
- [X] T021 [P] [US2] Implement option 2: View Todos functionality in src/cli/todo_app.py
- [X] T022 [US2] Connect add todo to service layer in src/cli/todo_app.py
- [X] T023 [US2] Connect view todos to service layer in src/cli/todo_app.py
- [X] T024 [US2] Add input validation for todo description in src/cli/todo_app.py
- [X] T025 [US2] Add success/error messaging for basic operations in src/cli/todo_app.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Perform Advanced Todo Operations (Priority: P3)

**Goal**: Users can update, delete, and mark todos complete/incomplete using the new menu system. The user selects menu options 3, 4, 5, and 6 to perform these operations.

**Independent Test**: Can be tested by adding a todo, updating it, marking it complete, then marking it incomplete, and finally deleting it. This validates all advanced todo operations with the new UX.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T026 [P] [US3] Unit test for update todo via menu in tests/unit/test_menu_update.py
- [ ] T027 [P] [US3] Unit test for delete todo via menu in tests/unit/test_menu_delete.py
- [ ] T028 [P] [US3] Unit test for mark complete/incomplete via menu in tests/unit/test_menu_mark.py

### Implementation for User Story 3

- [X] T029 [P] [US3] Implement option 3: Update Todo functionality in src/cli/todo_app.py
- [X] T030 [P] [US3] Implement option 4: Delete Todo functionality in src/cli/todo_app.py
- [X] T031 [P] [US3] Implement option 5: Mark Todo Complete functionality in src/cli/todo_app.py
- [X] T032 [P] [US3] Implement option 6: Mark Todo Incomplete functionality in src/cli/todo_app.py
- [X] T033 [US3] Connect update/delete operations to service layer in src/cli/todo_app.py
- [X] T034 [US3] Connect mark complete/incomplete operations to service layer in src/cli/todo_app.py
- [X] T035 [US3] Add input validation for todo position and description in src/cli/todo_app.py
- [X] T036 [US3] Add success/error messaging for advanced operations in src/cli/todo_app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T037 [P] Add comprehensive error handling for all menu operations in src/cli/todo_app.py
- [X] T038 [P] Add input validation and sanitization for all user inputs
- [X] T039 [P] Add proper exit codes and graceful shutdown
- [X] T040 [P] Update README.md with menu UX instructions
- [X] T041 [P] Add documentation for menu interface in docs/menu-ux.md
- [X] T042 Run quickstart.md validation for menu UX

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
- Models before services (if needed)
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
Task: "Unit test for menu display functionality in tests/unit/test_menu.py"
Task: "Integration test for menu navigation in tests/integration/test_menu_nav.py"

# Launch all components for User Story 1 together:
Task: "Implement menu display function in src/cli/todo_app.py"
Task: "Implement main menu loop with continuous display in src/cli/todo_app.py"
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