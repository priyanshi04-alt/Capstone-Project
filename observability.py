# utils/observability.py
import logging
from pathlib import Path
from typing import Dict
from memory.session_service import SessionService

# Configure logger
LOG_PATH = Path("submission_artifacts/fitlife_agent.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("fitlife")
logger.setLevel(logging.INFO)
if not logger.handlers:
    fh = logging.FileHandler(LOG_PATH, mode="a")
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# session service (shared)
SESSION = SessionService()

def log_event(user_id: str, event_type: str, details: Dict):
    """
    Log to file + append to session memory.
    """
    msg = f"user={user_id} event={event_type} details={details}"
    logger.info(msg)
    # add to session memory
    SESSION.append_event(user_id, event_type, details)
