from typing_extensions import TypedDict

class GraphState(TypedDict):
    """
    Shared state passed between LangGraph nodes
    """
    question: str
    answer: str
    is_valid: bool
    retries: int
