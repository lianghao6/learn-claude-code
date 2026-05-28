#!/usr/bin/env python3
"""
s18: Worktree Isolation — git worktree + task-directory binding + event log.

Run:  python s18_worktree_isolation/code.py
Need: pip install anthropic + 

Changes from s17:
  - Task dataclass gains worktree field (str | None)
  - validate_worktree_name: reject path traversal and illegal chars
  - create_worktree: validate name, git worktree add, optional task binding
  - bind_task_to_worktree: write worktree field only, keep task pending
  - remove_worktree: safety check before force, no auto-complete
  - run_git returns (ok, output), events only on success
  - Teammate tools: + complete_task, run in worktree cwd when bound
  - scan_unclaimed_tasks: uses can_start() for dependency checking
  - idle_poll: checks claim result, dispatches shutdown in IDLE
  - consume_lead_inbox: unified inbox consumer
  - 3 new Lead tools: create_worktree, remove_worktree, keep_worktree

ASCII topology:
  Main repo (/)
    ├── .worktrees/auth/  (branch: wt/auth)  ← Task #1
    ├── .worktrees/ui/    (branch: wt/ui)     ← Task #2
    ├── .tasks/task_xxx.json (worktree: "auth")
    └── .worktrees/events.jsonl
"""
