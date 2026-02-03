from agents.course_status_agent import assess_course_status
from agents.deadline_agent import assess_deadline
from agents.planning_agent import plan_tasks
from agents.scheduling_agent import allocate_time

# This supervisor agent function orchestrates the workflow of assessing course status, evaluating deadlines, and generating a priority-based schedule.
def run_supervisor(courses, available_minutes):

    # Assessing the status of each course using the course status agent.
    for course in courses:
        assess_course_status(course)

    # Assessing the next deadline of each course using the deadline agent.
    for course in courses:
        assess_deadline(course)

    # Generating a prioritized task plan based on the courses' deadlines and risk scores using the planning agent.
    priority_plan = plan_tasks(courses)

    # Allocating time based on the planned tasks, risk scores, and deadline urgencies using the scheduling agent.
    schedule = allocate_time(priority_plan, available_minutes)

    # Returning the priority plan and the schedule.
    return {
        "priorities": priority_plan,
        "schedule": schedule,
    }