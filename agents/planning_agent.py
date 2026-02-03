# This is a dictionary that assigns weights to different deadline urgency levels.
DEADLINE_WEIGHT = {
    "Critical": 100,
    "High": 60,
    "Medium": 30,
    "Low": 10,
    "None": 0,
}

# This function generates a prioritized task plan based on the courses' deadline urgencies and risk scores.
def plan_tasks(courses):
    plan = []

    # For each course, a priority score is calculated based on deadline urgency, risk score, and cognitive load.
    for course in courses:
        deadline_weight = DEADLINE_WEIGHT.get(course.deadline_urgency, 0) # This gets the weight for deadline urgency and defaults to 0 if undefined.

        risk_weight = course.risk_score or 0

        # Cognitive load has a smaller impact on priority compared to deadline and risk, so its weight is lower.
        cognitive_load_weight = 0 # This handles the case where cognitive load is undefined or low.
        if course.cognitive_load == "Medium":
            cognitive_load_weight = 1 
        elif course.cognitive_load == "High":
            cognitive_load_weight = 2

        # Risk weight is multiplied by 10 to give it more influence in the priority calculation, but still less than deadline weight.
        # If risk weight is higher deadline weight, then the deadline urgency is probably not as critical; "Low" or Medium".
        # Cognitive load is subtracted to slightly reduce priority for high cognitive load courses.
        priority_score = deadline_weight + (risk_weight * 10) - cognitive_load_weight 

        plan.append({ "course": course, "priority_score": priority_score}) # This adds each course and its priority score to the list.

    plan.sort(key=lambda x: x["priority_score"], reverse=True) # This sorts the plan by priority score in descending order.

    return plan