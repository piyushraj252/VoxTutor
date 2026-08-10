import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from sentence_transformers import SentenceTransformer


load_dotenv()

qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

COLLECTION_NAME = "voxtutor_knowledge"

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read our knowledge file
with open("data/knowledge.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split the knowledge into chunks
chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

# Convert text into 384-dimensional vectors
embeddings = model.encode(chunks)

# Prepare Qdrant points
points = []

for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
    points.append(
        PointStruct(
            id=i,
            vector=embedding.tolist(),
            payload={
                "text": chunk
            }
        )
    )

# Upload vectors to Qdrant
qdrant.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print(f"Successfully added {len(points)} knowledge chunks to Qdrant!")