from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

URL = "https://b004b73a-fa64-45d4-b318-7881889680aa.europe-west3-0.gcp.cloud.qdrant.io"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.2cZN0dHlsD7TaaVHXVgUtHk-ttl6kztFjebhlI2KW8Y"

client = QdrantClient(url=URL, api_key=KEY)

def setup_db():
    client.recreate_collection(
        collection_name="robotics_textbook",
        vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
    )
    print("✅ Collection 'robotics_textbook' created successfully!")

if __name__ == "__main__":
    setup_db()
