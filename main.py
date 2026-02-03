from tools.courses import get_courses
from agents.course_status_agent import assess_course_status
from agents.deadline_agent import assess_deadline
from agents.planning_agent import plan_tasks

courses = get_courses() # Getting the list of courses.

for course in courses:
    assess_course_status(course) # Assessing the status of each course.
    assess_deadline(course) # Assessing the deadlines of each course.

task_plan = plan_tasks(courses) # Planning the tasks based on the analysis from the agents.

print("PRIORITIES")
for item in task_plan:
    course = item["course"]
    print(
        f"{course.name} | "
        f"deadline: {course.deadline_urgency} | "
        f"risk: {course.risk_score} | "
        f"priority_score: {item['priority_score']}"
    )


"""
PREVIOUS TEST CODE:

statuses = [assess_course_status(c) for c in courses] # Assessing the status of each course.
deadline_reports = [assess_deadline(c) for c in courses if assess_deadline(c)] # Assessing the deadlines of each course.

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
"""



