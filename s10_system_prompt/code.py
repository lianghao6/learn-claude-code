#!/usr/bin/env python3
"""
s10: System Prompt — Runtime prompt assembly with caching.

Run:  python s10_system_prompt/code.py
Need: pip install anthropic + 

Changes from s09:
  - PROMPT_SECTIONS: topic-keyed dict of prompt fragments
  - assemble_system_prompt(context): select + join sections by real state
  - get_system_prompt(context): deterministic cache via json.dumps
  - agent_loop uses get_system_prompt(context) instead of hardcoded SYSTEM

Memory section loads when .memory/MEMORY.md exists (real state, not keywords).
"""
