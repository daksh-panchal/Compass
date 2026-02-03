from datetime import date

# This agent function assesses the status of a course and returns relevant details about the course.
def assess_course_status(course):

    days_idle = (
        (date.today() - course.last_worked_on).days
        if course.last_worked_on else 999
    )

    risk_score = 0

    if days_idle > 7:
        risk_score += 2

    if course.recovery_cost == "High":
        risk_score += 2
    elif course.recovery_cost == "Medium":
        risk_score += 1

    if course.cognitive_load == "High":
        risk_score += 1

    if course.current_standing in ("Behind", "At Risk"):
        risk_score += 2

    return {
        "course": course,
        "risk_score": risk_score,
        "days_idle": days_idle,
        "cognitive_load": course.cognitive_load,
        "recovery_cost": course.recovery_cost,
    }
