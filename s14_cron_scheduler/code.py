#!/usr/bin/env python3
"""
s14: Cron Scheduler — independent daemon thread + queue processor.

Run:  python s14_cron_scheduler/code.py
Need: pip install anthropic + 

Changes from s13:
  - CronJob dataclass (id, cron, prompt, recurring, durable)
  - cron_matches: 5-field cron expression matching with DOM/DOW OR semantics
  - schedule_job / cancel_job: register/remove cron jobs (with validation)
  - cron_scheduler_loop: independent daemon thread, polls every 1s
  - cron_queue: thread-safe queue, scheduler writes, queue processor delivers
  - queue_processor_loop: auto-runs agent_loop when cron_queue has work
  - Durable storage: .scheduled_tasks.json (survives restart)
  - 3 new tools: schedule_cron, list_crons, cancel_cron

Four layers:
  1. Scheduler: daemon thread checks time → fires matching jobs
  2. Queue: cron_queue decouples scheduler from agent loop
  3. Queue processor: wakes the agent when queued work exists and it is idle
  4. Consumer: agent_loop consumes queued jobs and injects them into messages
"""
