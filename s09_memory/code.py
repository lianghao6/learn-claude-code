#!/usr/bin/env python3
"""
s09_memory.py - Memory System

Persistent, cross-session knowledge for the coding agent.

Storage:
    .memory/
      MEMORY.md          ← index (one line per memory, ≤200 lines)
      feedback_tabs.md    ← individual memory files (Markdown + YAML frontmatter)
      user_profile.md
      project_facts.md

Flow in agent_loop:
    1. Load MEMORY.md index into SYSTEM prompt (cheap, always present)
    2. Select relevant memories by filename/description → inject content
    3. Run compression pipeline from s08
    4. After each turn ends → extract new memories from original messages
    5. Periodically consolidate (Dream)

Builds on s08 (context compact). Usage:

    python s09_memory/code.py
    Needs: pip install anthropic
"""
