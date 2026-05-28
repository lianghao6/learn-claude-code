#!/usr/bin/env python3
"""
s16: Team Protocols — request-response protocol + request_id + dispatch + state machine.

Run:  python s16_team_protocols/code.py
Need: pip install anthropic + 

Changes from s15:
  - ProtocolState dataclass (request_id, type, sender, status, created_at)
  - pending_requests dict: tracks in-flight protocol requests
  - dispatch_message: routes incoming messages by type to handlers
  - request_shutdown: Lead sends shutdown protocol request
  - request_plan: Lead asks teammate to submit plan
  - handle_shutdown_request / handle_plan_response: teammate receives & responds
  - match_response: Lead correlates response to request via request_id (with type validation)
  - Teammate idle loop: waits for inbox messages instead of exiting after 10 rounds
  - Unified consume_lead_inbox: protocol routing + injection into history
  - 3 new Lead tools: request_shutdown, request_plan, review_plan
  - 1 new teammate tool: submit_plan

ASCII flow:
  Lead: BUS.send("shutdown_request", {request_id}) ──────→ teammate inbox
  Teammate: dispatch → handler → BUS.send("shutdown_response", {request_id}) ─→ Lead inbox
  Lead: consume_lead_inbox → match_response(request_id) → pending_requests[req_id].status = approved
"""
