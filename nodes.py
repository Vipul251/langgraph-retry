from langchain_ollama import OllamaLLM
from state import GraphState

# Initialize Ollama LLM
llm = OllamaLLM(model="gemma3")


def answer_generator(state: GraphState) -> GraphState:
    """
    Node 1: Answer Generator
    Responsibilities:
    - Generate answer using LLM
    - Increment retry count
    """
    question = state["question"]
    retries = state["retries"]

    response = llm.invoke(question)

    return {
        **state,
        "answer": response,
        "retries": retries + 1
    }


def answer_validator(state: GraphState) -> GraphState:
    """
    Node 2: Answer Validator
    Responsibilities:
    - Validate answer quality
    - Do NOT generate or retry
    """
    answer = state["answer"]

    is_valid = bool(answer) and len(answer.strip()) >= 50

    return {
        **state,
        "is_valid": is_valid
    }
