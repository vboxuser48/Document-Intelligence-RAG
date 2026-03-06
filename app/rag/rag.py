from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.rag.embeddings import generate_embeddings, model
from app.rag.vector_score import create_index
from app.rag.retriever import search
from app.rag.generator import generate_answer


index=None
chunks=None

def ingest_document(pdf_path):
    global index
    global chunks

    text=load_pdf(pdf_path)
    chunks=chunk_text(text)
    embeddings=generate_embeddings(chunks)
    index=create_index(embeddings)


def rag_query(question:str):
    
    results=search(index,model,question,chunks)
    answer=generate_answer(results,question)

    return answer
