"""A deliberately small AI agent used to demonstrate AI security controls.

The same agent runs in two modes:
  secure=False  the naive build (vulnerable on purpose)
  secure=True   controls enforced outside the model
"""

from .agent import Agent, AgentResult
from .policy import AgentIdentity, PolicyEngine

__all__ = ["Agent", "AgentResult", "AgentIdentity", "PolicyEngine"]
