

DEADLINE_WEIGHT = {
    "Critical": 100,
    "High": 60,
    "Medium": 30,
    "Low": 10,
    "None": 0,
}

def plan_tasks(courses):
    plan = []

    for course in courses:
        deadline_weight = DEADLINE_WEIGHT.get(course.deadline_urgency, 0)

        risk_weight = course.risk_score or 0

        cognitive_load_weight = 0 # This handles the case where cognitive load is undefined or low.
        if course.cognitive_load == "Medium":
            cognitive_load_weight = 1
        elif course.cognitive_load == "High":
            cognitive_load_weight = 2

        priority_score = deadline_weight + (risk_weight * 10) - cognitive_load_weight

        plan.append({ "course": course, "priority_score": priority_score})

    plan.sort(key=lambda x: x["priority_score"], reverse=True)

    return plan