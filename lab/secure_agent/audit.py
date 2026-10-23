"""Structured audit trail with a per-request trace ID (Q8)."""

import json
import time


class AuditLog:
    def __init__(self):
        self.events: list[dict] = []

    def record(self, trace_id: str, event: str, **fields) -> None:
        self.events.append({"trace_id": trace_id, "ts": time.time(), "event": event, **fields})

    def trace(self, trace_id: str) -> list[dict]:
        return [e for e in self.events if e["trace_id"] == trace_id]

    def to_jsonl(self) -> str:
        return "\n".join(json.dumps(e, sort_keys=True) for e in self.events)
