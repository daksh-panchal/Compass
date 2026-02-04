from agents.course_status_agent import assess_course_status
from graph.state import CompassState

# This node function updates the course statuses in the Compass state.
def course_status_node(state: CompassState):
    for course in state["courses"]:
        assess_course_status(course)
    return state