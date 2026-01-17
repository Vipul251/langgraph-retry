from langgraph.graph import StateGraph, END
from state import GraphState
from nodes import answer_generator, answer_validator


def route_after_validation(state: GraphState):
    """
    Conditional routing logic (NO LOOPS)
    """
    if state["is_valid"]:
        return END

    if not state["is_valid"] and state["retries"] < 1:
        return "generate"

    return END


def build_graph():
    """
    Builds and compiles the LangGraph workflow
    """
    graph = StateGraph(GraphState)

    # Add nodes
    graph.add_node("generate", answer_generator)
    graph.add_node("validate", answer_validator)

    # Entry point
    graph.set_entry_point("generate")

    # Normal edges
    graph.add_edge("generate", "validate")

    # Conditional edges (KEY REQUIREMENT)
    graph.add_conditional_edges(
        "validate",
        route_after_validation,
        {
            "generate": "generate",
            END: END
        }
    )

    return graph.compile()
