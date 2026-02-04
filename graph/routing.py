from graph.state import CompassState

# This function runs the deadline agent only if at least one course has a deadline.
def route_after_status(state: CompassState) -> str:
    for c in state["courses"]:
        if c.next_deadline:
            return "deadline"
    
    return "planning" # Skip to planning if no deadlines are present.

# This function decides whether to proceed to scheduling or end the graph after planning.
def route_after_planning(state: CompassState) -> str: 
    if not state.get("priorities"): # If no priorities were generated then end the graph.
        return "end"

    if state.get("available_minutes", 0) <= 0: # If the user has no time today, skip scheduling.
        return "end"
    return "scheduling"

# This function decides whether to proceed to explanation or end the graph after scheduling.
def route_after_scheduling(state: CompassState) -> str:

    if state.get("explain", False): # Only explain if explicitly requested
        return "explanation"
    return "end"




