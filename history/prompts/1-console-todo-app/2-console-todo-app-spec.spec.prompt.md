---
id: 2
title: Console Todo App Spec
stage: spec
date: 2026-01-02
surface: agent
model: Claude Sonnet 4.5
feature: 1-console-todo-app
branch: 1-console-todo-app
user: user
command: /sp.specify
labels: [spec, todo-app, console]
links:
  spec: specs/1-console-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-console-todo-app/spec.md
  - specs/1-console-todo-app/checklists/requirements.md
tests: []
---

## Prompt

```
/sp.specify In-Memory Console Todo App (Phase I)

Target audience:
- Claude Code (AI coding agent)
- Spec-driven project reviewers

Objective:
Build a Python command-line Todo app that stores all data in memory, using Spec-Kit Plus and Claude Code only (no manual coding).

Core features (mandatory):
- Add todo
- View todos
- Update todo
- Delete todo
- Mark todo complete / incomplete

Success criteria:
- Runs in console (CLI)
- All 5 features work deterministically
- No persistence (memory only)
- Clean, modular Python structure
- Behavior matches spec exactly

Technology stack:
- Python 3.13+
- UV
- Claude Code
- Spec-Kit Plus

Constraints:
- No files, no database
- No web or GUI
- Single user, single session
- Explicit error handling for invalid input

Specification requirements:
- Define CLI commands and outputs
- Define in-memory todo data model
- Define valid state transitions
- Define failure cases and messages

Not building:
- Persistence
- AI/NLP commands
- Advanced features (priority, due dates, tags)
- Multi-user support

Scope:
- Phase I only

End Specification
```

## Response snapshot

Created comprehensive specification for the In-Memory Console Todo App (Phase I) with three user stories prioritized by importance: (P1) Add and View Todos, (P2) Update and Delete Todos, and (P3) Mark Todos Complete/Incomplete. The spec includes 10 functional requirements covering all core features, key entity definitions, measurable success criteria, and edge cases. A quality checklist was also created to validate the specification completeness.

## Outcome

- ✅ Impact: Created complete feature specification for Phase I todo app
- 🧪 Tests: No tests required for specification creation
- 📁 Files: Created spec.md and requirements checklist
- 🔁 Next prompts: Ready to proceed with planning phase
- 🧠 Reflection: Specification covers all required features with clear acceptance criteria

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementation planning