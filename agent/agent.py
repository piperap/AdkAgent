"""Punto de entrada del agente. ADK busca la variable `root_agent` en este archivo."""

from google.adk.agents import Agent

from . import config
from .prompts import INSTRUCTION
from .tools import TOOLS


def create_agent(
    name: str = config.AGENT_NAME,
    model: str = config.MODEL,
    instruction: str = INSTRUCTION,
    tools: list | None = None,
) -> Agent:
    """Crea un agente ADK. Reutilízala para armar otros agentes con distinto prompt o tools."""
    return Agent(
        name=name,
        model=model,
        description="Asistente de propósito general.",
        instruction=instruction,
        tools=TOOLS if tools is None else tools,
    )


root_agent = create_agent()
