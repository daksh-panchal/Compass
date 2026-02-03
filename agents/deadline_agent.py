from datetime import date

# This agent function evaluates the urgency of an upcoming deadline for a course and updates the course object accordingly.
def assess_deadline(course):

    if not course.next_deadline:
        return None

    days_left = (course.next_deadline - date.today()).days

    if days_left <= 1:
        urgency = "Critical"
    elif days_left <= 3:
        urgency = "High"
    elif days_left <= 7:
        urgency = "Medium"
    else:
        urgency = "Low"

    course.days_until_deadline = days_left
    course.deadline_urgency = urgency

    return course
"""
return {
        "course": course,
        "days_left": days_left,
        "urgency": urgency,
    }
"""

