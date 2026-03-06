from fastapi import FastAPI,UploadFile,File
import shutil
from pydantic import BaseModel
from app.api.routes import router
from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.rag.embeddings import generate_embeddings, model
from app.rag.vector_score import create_index
from app.rag.retriever import search
from app.rag.generator import generate_answer
from app.rag.rag import ingest_document,rag_query


app=FastAPI()
app.include_router(router)
class Question(BaseModel):
    question:str

@app.post("/upload-document")

async def upload_document(file:UploadFile=File(...)):
    path=f"docs/file{file.filename}"

    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    ingest_document(path)

    return {"message":"document indexed"}

@app.post("/ask")

async def ask(q:Question):
    answer=rag_query(q.question)

    return {"answer":answer}

