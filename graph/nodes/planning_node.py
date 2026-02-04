from agents.planning_agent import plan_tasks
from graph.state import CompassState

# This function generates a priority plan for the Compass state.
def planning_node(state: CompassState):
    state["priorities"] = plan_tasks(state["courses"])
    return state