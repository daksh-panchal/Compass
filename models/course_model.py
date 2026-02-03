from dataclasses import dataclass
from datetime import date
from typing import List

# I am defining a course class to represent course information.
@dataclass
class Course:
    name: str
    course_type: List[str]
    current_standing: str
    last_worked_on: date | None
    recovery_cost: str
    grading_scheme: List[str]
    cognitive_load: str
