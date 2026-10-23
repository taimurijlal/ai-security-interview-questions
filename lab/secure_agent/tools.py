"""Tool registry, modelled on MCP tools: name, scope, side effect, input validation (Q4, Q5)."""

import re
from dataclasses import dataclass
from typing import Callable

READ, WRITE, EXTERNAL = "read", "write", "external"


@dataclass(frozen=True)
class Tool:
    name: str
    scope: str        # permission the calling agent identity must hold
    side_effect: str  # read | write | external
    validate: Callable[[dict], str | None]  # returns an error message or None
    run: Callable[["ToolContext", dict], str]


class ToolContext:
    """Simulated downstream systems the tools act on."""

    def __init__(self):
        self.outbox: list[dict] = []
        self.records = {"R-17": "order 17", "R-18": "order 18"}


def _validate_customer(args):
    if not re.fullmatch(r"C\d{4}", str(args.get("customer_id", ""))):
        return "customer_id must match C#### (e.g. C0001)"


def _validate_record(args):
    if not re.fullmatch(r"R-\d{1,6}", str(args.get("record_id", ""))):
        return "record_id must match R-<number>"


def _validate_email(args):
    if not re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", str(args.get("to", ""))):
        return "to must be a single email address"


def _send_email(ctx, args):
    ctx.outbox.append({"to": args["to"], "body": args.get("body", "")})
    return f"sent to {args['to']}"


def _delete_record(ctx, args):
    ctx.records.pop(args["record_id"], None)
    return f"deleted {args['record_id']}"


TOOLS = {
    t.name: t
    for t in [
        Tool("lookup_customer", "customers:read", READ, _validate_customer,
             lambda ctx, a: f"customer {a['customer_id']}: status=active"),
        Tool("delete_record", "records:write", WRITE, _validate_record, _delete_record),
        Tool("send_email", "email:send", EXTERNAL, _validate_email, _send_email),
    ]
}
