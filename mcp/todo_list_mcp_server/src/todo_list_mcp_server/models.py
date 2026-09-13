from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TodoItem(BaseModel):
    id: int
    title: str
    done: bool = False
    priority: Priority = Priority.medium
    created_at: datetime = Field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return self.model_dump(mode="json")

    @classmethod
    def from_dict(cls, data: dict) -> "TodoItem":
        return cls(**data)
