from enum import Enum

from pydantic import BaseModel, Field


class DifficultyEnum(str, Enum):
    Easy = "easy"
    Medium = "medium"
    Hard = "hard"


class RoomCreate(BaseModel):
    topic: str

    difficulty: DifficultyEnum

    num_questions: int = Field(gt=0, le=100)

    time_per_question: int = Field(ge=5, le=120)