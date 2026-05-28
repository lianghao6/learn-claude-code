#!/usr/bin/env python3
"""
s12: Task System — file-persisted task graph with blockedBy dependencies.

Run:  python s12_task_system/code.py
Need: pip install anthropic + 

Changes from s11:
  - Task dataclass (id, subject, description, status, owner, blockedBy)
  - TASKS_DIR = .tasks/ for persistent JSON storage
  - create_task / save_task / load_task / list_tasks / get_task
  - can_start: checks blockedBy all completed (missing deps = blocked)
  - claim_task: set owner + pending -> in_progress
  - complete_task: set completed + report unblocked downstream
  - 5 new tools: create_task, list_tasks, get_task, claim_task, complete_task

Note: Teaching code keeps a basic agent loop to stay focused on the task
system. S11's full error recovery (RecoveryState, backoff, escalation,
reactive compact, fallback model) is omitted — in real CC, tasks.ts and
withRetry are independent layers that compose naturally.
"""
