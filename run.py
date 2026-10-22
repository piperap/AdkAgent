"""Usa el agente desde tu propio código (sin la UI de ADK).

    python run.py "¿Qué hora es en Madrid?"
"""

import asyncio
import sys

from google.adk.runners import InMemoryRunner
from google.genai import types

from agent.agent import root_agent


async def ask(question: str, user_id: str = "user") -> str:
    runner = InMemoryRunner(agent=root_agent, app_name="app")
    session = await runner.session_service.create_session(app_name="app", user_id=user_id)
    message = types.Content(role="user", parts=[types.Part(text=question)])

    answer = ""
    async for event in runner.run_async(user_id=user_id, session_id=session.id, new_message=message):
        if event.is_final_response() and event.content and event.content.parts:
            answer = "".join(part.text or "" for part in event.content.parts)
    return answer


if __name__ == "__main__":
    print(asyncio.run(ask(" ".join(sys.argv[1:]) or "Hola, ¿qué puedes hacer?")))
