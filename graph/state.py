from typing import TypedDict, List
from models.course_model import Course

# I am defining a class to represent the overall state of the Compass application.
class CompassState(TypedDict):
    courses: List[Course]
    priorities: list
    schedule: list
    explanation: str | None
