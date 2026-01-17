# langgraph-retry
LangGraph Validation & Retry System

LangGraph workflow that generates answers using a local LLM (Ollama), validates response quality, and retries generation once if the answer does not meet a minimum quality bar.

This project demonstrates stateful AI workflows, conditional execution, and reliability patterns used in real-world LLM systems.


🧩 Tech Stack
| Component       | Technology        |
| --------------- | ----------------- |
| Workflow Engine | LangGraph         |
| LLM Runtime     | Ollama            |
| Models          | Gemma 3 / LLaMA 2 |
| UI              | Streamlit         |
| Language        | Python 3.13       |


🖥️ Setup Instructions
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Install & verify Ollama

Download from:
👉 https://ollama.com

Verify:

ollama --version

3️⃣ Pull a model (required)
ollama pull gemma3
# or
ollama pull llama2


Verify:

ollama list

4️⃣ Run the application
streamlit run app.py
