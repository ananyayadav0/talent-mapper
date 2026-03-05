import sys
print(f"Python: {sys.version}")

import fastapi; print(f"check FastAPI: {fastapi.__version__}")
import pydantic; print(f"check Pydantic: {pydantic.__version__}")
import sqlalchemy; print(f"check SQLAlchemy: {sqlalchemy.__version__}")
import spacy; print(f"check spaCy: {spacy.__version__}")
import fitz; print(f"check PyMuPDF: {fitz.__version__}")
import docx; print(f"check python-docx: OK")
import sentence_transformers; print(f"check sentence-transformers: {sentence_transformers.__version__}")
import chromadb; print(f"check ChromaDB: {chromadb.__version__}")
import celery; print(f"check Celery: {celery.__version__}")
import redis; print(f"check redis-py: {redis.__version__}")
import kafka; print(f"check kafka-python: OK")
import anthropic; print(f"check Anthropic SDK: {anthropic.__version__}")
import openai; print(f"check OpenAI SDK: {openai.__version__}")

# Test spaCy model loaded
nlp = spacy.load("en_core_web_sm")
doc = nlp("John Smith is a software engineer with Python and AWS skills.")
print(f"check spaCy model: loaded, found {len(list(doc.ents))} entities")

# Test sentence transformer
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
vec = model.encode("backend engineer with Java experience")
print(f"check Embeddings: vector shape {vec.shape}")

