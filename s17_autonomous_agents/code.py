#!/usr/bin/env python3
"""
s17: Autonomous Agents — idle poll + auto-claim + WORK/IDLE lifecycle.

Run:  python s17_autonomous_agents/code.py
Need: pip install anthropic + 

Changes from s16:
  - scan_unclaimed_tasks: find pending, unowned tasks with deps completed
  - idle_poll: 60s polling loop (inbox + task board), dispatches shutdown in IDLE
  - claim_task: owner check + return value verification
  - Teammate lifecycle: WORK → IDLE → SHUTDOWN
  - Teammate tools: + list_tasks, claim_task, complete_task (5→8)
  - consume_lead_inbox: unified inbox consumer for protocol + context injection
  - Identity re-injection after context compression

ASCII lifecycle:
  WORK: inbox → LLM → tools → (tool_use? loop) → (done? → IDLE)
  IDLE: 5s poll → inbox? → WORK / unclaimed? → claim → WORK / 60s? → SHUTDOWN
"""
