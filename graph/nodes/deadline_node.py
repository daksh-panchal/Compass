from agents.deadline_agent import assess_deadline
from graph.state import CompassState

# This function updates the deadline assessments in the Compass state.
def deadline_node(state: CompassState):
    for course in state["courses"]:
        assess_deadline(course)
    return state