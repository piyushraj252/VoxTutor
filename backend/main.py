import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from google import genai


load_dotenv()


# Gemini
gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Qdrant
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)


# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "VoxTutor backend is working!"
    }


@app.post("/search")
def search_knowledge(user_message: UserMessage):

    query_embedding = model.encode(
        user_message.message
    ).tolist()

    results = qdrant.query_points(
        collection_name="voxtutor_knowledge",
        query=query_embedding,
        limit=3
    ).points

    return {
        "results": [
            {
                "text": result.payload["text"],
                "score": result.score
            }
            for result in results
        ]
    }


@app.post("/chat")
def chat(user_message: UserMessage):

    # 1. Convert the question into an embedding
    query_embedding = model.encode(
        user_message.message
    ).tolist()

    # 2. Retrieve relevant knowledge from Qdrant
    results = qdrant.query_points(
        collection_name="voxtutor_knowledge",
        query=query_embedding,
        limit=3
    ).points

    # 3. Combine retrieved knowledge
    context = "\n\n".join(
        result.payload["text"]
        for result in results
    )

    # 4. Give the retrieved knowledge to Gemini
    prompt = f"""
You are VoxTutor, a friendly AI tutor.

Explain concepts clearly and simply for beginners.
Use examples when helpful.
Keep the answer concise.

Use the following knowledge retrieved from VoxTutor's knowledge base:

--- KNOWLEDGE ---
{context}
--- END KNOWLEDGE ---

Student's question:
{user_message.message}

Answer the student's question using the retrieved knowledge.
"""

    response = gemini_client.models.generate_content(
model="gemini-3.6-flash",
        contents=prompt
    )

    return {
        "reply": response.text
    }