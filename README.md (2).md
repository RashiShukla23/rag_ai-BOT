# RAG AI Bot

A chatbot that answers questions based on your own documents. Instead of relying on what the LLM already knows, it retrieves relevant information from your files before generating a response — so answers are actually grounded in your content.

---

## What it does

- Indexes your documents and stores them as vector embeddings in ChromaDB
- Retrieves the most relevant chunks when you ask a question
- Passes the retrieved context to GPT-4.1 to generate accurate, grounded answers
- Separates the indexing pipeline from the chat interface cleanly

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | GPT-4.1 (OpenAI) |
| Embeddings | OpenAI Embeddings |
| Vector Store | ChromaDB |
| RAG Framework | LangChain |
| Frontend | Streamlit |
| Language | Python |

---

## Project Structure

```
rag_ai-BOT/
├── app.py         # Streamlit UI and chat interface
├── chat.py        # RAG chain — retrieval + LLM response
├── indexing.py    # Document loading, chunking, and embedding
└── .gitignore
```

---

## Getting Started

Prerequisites: Python 3.10+, OpenAI API key

```bash
git clone https://github.com/RashiShukla23/rag_ai-BOT.git
cd rag_ai-BOT

py -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_key
```

Step 1 — index your documents:

```bash
python indexing.py
```

Step 2 — run the chatbot:

```bash
streamlit run app.py
```

---

## How it works

Documents are loaded, split into chunks, and embedded using OpenAI Embeddings, then stored in ChromaDB. When a user asks a question, the query is embedded and matched against the stored chunks. The top results are passed to GPT-4.1 along with the question, and the model generates a response grounded in your actual documents.

---

## Author

**Rashi Shukla** — [GitHub](https://github.com/RashiShukla23)
