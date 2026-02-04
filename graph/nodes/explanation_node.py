from llm.explainer import explain_plan
from graph.state import CompassState

# This function generates an explanation based on the generated plan and schedule for the Compass state.
def explanation_node(state: CompassState):
    state["explanation"] = explain_plan(
        state["priorities"], state["schedule"]
    )
    return state