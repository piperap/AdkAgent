"""Configuración del agente leída desde variables de entorno (.env)."""

import os

from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = os.getenv("AGENT_NAME", "asistente")
MODEL = os.getenv("MODEL", "gemini-2.5-flash")
