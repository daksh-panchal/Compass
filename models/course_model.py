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
    next_deadline: date | None

# These parameters are used to store the assessment results of each course so that the planning agent can read everything from one object.
    risk_score: int | None = None
    days_idle: int | None = None

    days_until_deadline: int | None = None
    deadline_urgency: str | None = None
