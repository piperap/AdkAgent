# Agente ADK

Plantilla mínima para crear agentes con [Google ADK](https://google.github.io/adk-docs/).

## Inicio rápido

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # agrega tu GOOGLE_API_KEY
adk web                     # abre http://localhost:8000 y elige "agent"
```

Desde código: `python run.py "¿Qué hora es en Madrid?"`

## Estructura

```
agent/
  agent.py     # create_agent() + root_agent
  prompts.py   # instrucciones del agente
  config.py    # nombre y modelo (desde .env)
  tools/       # una función Python = una herramienta
run.py         # ejemplo de uso programático
```

## Adaptarlo

- **Comportamiento:** edita `agent/prompts.py`.
- **Herramienta nueva:** crea una función con docstring y type hints en `agent/tools/` y agrégala a `TOOLS` en `agent/tools/__init__.py`.
- **Otro modelo:** cambia `MODEL` en `.env`.
- **Otro agente:** `create_agent(name="soporte", instruction="...", tools=[...])`.
