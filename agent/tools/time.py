"""Herramienta de ejemplo: el docstring y los type hints son lo que ve el modelo."""

from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def get_current_time(timezone: str = "America/Santiago") -> dict:
    """Devuelve la fecha y hora actual en una zona horaria.

    Args:
        timezone: Zona horaria IANA, por ejemplo "America/Santiago" o "Europe/Madrid".

    Returns:
        dict con "status" ("success" o "error") y "time" o "error_message".
    """
    try:
        now = datetime.now(ZoneInfo(timezone))
    except ZoneInfoNotFoundError:
        return {"status": "error", "error_message": f"Zona horaria desconocida: {timezone}"}
    return {"status": "success", "time": now.isoformat(timespec="seconds")}
