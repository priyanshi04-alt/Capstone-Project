# memory/session_service.py
import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict

class SessionService:
    """
    Simple JSON-backed session + memory service.
    Stores sessions in memory and persistently to disk (submission_artifacts/session_store.json).
    """

    def __init__(self, path: str = "submission_artifacts/session_store.json"):
        self.path = Path(path)
        self.sessions: Dict[str, Dict[str, Any]] = {}
        self._load()

    def _load(self):
        if self.path.exists():
            try:
                with open(self.path, "r") as f:
                    data = json.load(f)
                    self.sessions = data
            except Exception:
                self.sessions = {}
        else:
            self.sessions = {}

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.sessions, f, indent=2, default=str)

    def create_user(self, user_id: str, profile: dict):
        now = datetime.utcnow().isoformat()
        self.sessions[user_id] = {
            "profile": profile,
            "events": [],
            "created_at": now,
            "last_updated": now
        }
        self._save()

    def append_event(self, user_id: str, event_type: str, payload: dict):
        if user_id not in self.sessions:
            self.create_user(user_id, {"note": "auto-created"})
        ev = {
            "ts": datetime.utcnow().isoformat(),
            "type": event_type,
            "payload": payload
        }
        self.sessions[user_id].setdefault("events", []).append(ev)
        self.sessions[user_id]["last_updated"] = ev["ts"]
        self._save()

    def get_profile(self, user_id: str) -> dict:
        return self.sessions.get(user_id, {}).get("profile")

    def get_events(self, user_id: str) -> list:
        return self.sessions.get(user_id, {}).get("events", [])

    def save_profile(self, user_id: str, profile: dict):
        if user_id not in self.sessions:
            self.create_user(user_id, profile)
            return
        self.sessions[user_id]["profile"] = profile
        self.sessions[user_id]["last_updated"] = datetime.utcnow().isoformat()
        self._save()
