from tools.courses import get_courses
from agents.course_status_agent import assess_course_status
from agents.deadline_agent import assess_deadline

courses = get_courses() # Getting the list of courses.
statuses = [assess_course_status(c) for c in courses] # Assessing the status of each course.
deadline_reports = [assess_deadline(c) for c in courses if assess_deadline(c)] # Assessing the deadlines of each course.

# Now, I will print out the status of every course based on the calculations made by the course status agent to verify its functionality.
for s in statuses:
    print(
        s["course"].name,
        "Risk:", s["risk_score"],
        "Days Idle:", s["days_idle"]
    )

# Next, I will print out the deadline details of each course to verify the deadline agent's functionality.
for d in deadline_reports:
    print(
        d["course"].name,
        "Due in:", d["days_left"], "days,",
        "Urgency:", d["urgency"]
    )

