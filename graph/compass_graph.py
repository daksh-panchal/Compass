from langgraph.graph import StateGraph, END
from graph.state import CompassState

from graph.nodes.course_status_node import course_status_node
from graph.nodes.deadline_node import deadline_node
from graph.nodes.planning_node import planning_node
from graph.nodes.scheduling_node import scheduling_node
from graph.nodes.explanation_node import explanation_node

# This function generates the Compass graph by adding nodes and defining their order of execution using edges.
def build_compass_graph():
    graph = StateGraph(CompassState)

    graph.add_node("course_status", course_status_node)
    graph.add_node("deadline", deadline_node)
    graph.add_node("planning", planning_node)
    graph.add_node("scheduling", scheduling_node)
    graph.add_node("explanation", explanation_node)

    graph.set_entry_point("course_status") # The starting node of the graph is the course status node.

    graph.add_edge("course_status", "deadline")
    graph.add_edge("deadline", "planning")
    graph.add_edge("planning", "scheduling")
    graph.add_edge("scheduling", "explanation")
    graph.add_edge("explanation", END)

    return graph.compile()
