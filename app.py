import streamlit as st
from graph import build_graph

st.set_page_config(page_title="LangGraph Retry Demo", layout="centered")

st.title("LangGraph Validation + Retry (Ollama)")
st.write("LLM answers are validated and retried once if needed.")

question = st.text_input("Ask a question:")

if st.button("Submit") and question:
    graph = build_graph()

    initial_state = {
        "question": question,
        "answer": "",
        "is_valid": False,
        "retries": 0
    }

    result = graph.invoke(initial_state)

    st.subheader("Final Answer")
    st.write(result["answer"])

    st.caption(f"Retries used: {result['retries']}")
