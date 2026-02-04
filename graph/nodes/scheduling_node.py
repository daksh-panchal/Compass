from agents.scheduling_agent import allocate_time
from graph.state import CompassState

# This function creates a schedule based on the priority plan and available minutes.
def scheduling_node(state: CompassState, available_minutes=180):
    state["schedule"] = allocate_time(
        state["priorities"], available_minutes
    )
    return state