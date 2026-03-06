# Document Intelligence RAG System

A production-style **Retrieval-Augmented Generation (RAG)** system for semantic document search and question answering.
The system allows users to upload documents, convert them into vector embeddings, retrieve relevant information using similarity search, and generate accurate answers using a Large Language Model.

---

# Features

* Upload and index PDF documents
* Automatic text extraction and document chunking
* Transformer embeddings using Sentence Transformers (MiniLM)
* Vector similarity search using FAISS
* Context-aware question answering using Google Gemini
* FastAPI backend with interactive API documentation
* Scalable architecture for document intelligence applications

---

# Tech Stack

* Python
* FastAPI
* Sentence Transformers (all-MiniLM-L6-v2)
* FAISS Vector Database
* Google Gemini API
* Uvicorn

---

# Project Structure

```
Document-Intelligence-RAG/
│
├── main.py                 # FastAPI application entry point
├── rag_pipeline.py         # RAG pipeline logic
├── document_loader.py      # PDF loading and text extraction
├── chunking.py             # Document chunking
├── embeddings.py           # Transformer embeddings
├── vector_store.py         # FAISS vector database operations
│
├── data/                   # Uploaded documents
├── requirements.txt        # Project dependencies
├── README.md
└── .env                    # API keys (not committed)
```

---

# RAG Architecture

```
User Query
     │
     ▼
Query Embedding
(Sentence Transformers)
     │
     ▼
Vector Similarity Search
(FAISS)
     │
     ▼
Top Relevant Document Chunks
     │
     ▼
LLM (Google Gemini)
     │
     ▼
Generated Answer
```

The retrieved document context is passed to the LLM, enabling **grounded responses and reducing hallucination**.

---

# Installation

Clone the repository:

```
git clone https://github.com/vboxuser48/Document-Intelligence-RAG.git
cd Document-Intelligence-RAG
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key
```

---

# Running the Application

Start the FastAPI server:

```
uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

# Example Workflow

1. Upload a document to the system
2. Text is extracted from the document
3. The text is split into chunks
4. Each chunk is converted into vector embeddings
5. Embeddings are stored in the FAISS vector database
6. The user asks a question
7. Relevant document chunks are retrieved
8. Gemini generates an answer using the retrieved context

---

# Example Query

Question:

```
What are the key responsibilities mentioned in the document?
```

Answer:

```
The document outlines responsibilities including project management,
client communication, and delivery timelines.
```

---

# Future Improvements

* Web interface for document upload and chat
* Hybrid search (BM25 + vector search)
* Multi-document querying
* Streaming LLM responses
* Docker deployment
* Support for multiple document formats (DOCX, TXT)

---

# Author

**Abhay Chauhan**

AI / ML Enthusiast
