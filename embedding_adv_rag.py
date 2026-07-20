from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings

# load env vars
load_dotenv()

# models

MODEL_LARGE = "text-embedding-3-large"

MODEL_SMALL = "text-embedding-3-small"

# create the embedder

embedder_large = OpenAIEmbeddings(
    model=MODEL_LARGE
)

embedder_small = OpenAIEmbeddings(
    model=MODEL_SMALL
)

# create embeddings from user query

query = "What is Openclaw/Moltbot and what are the major security concerns regarding this tool"

embeddings_large = embedder_large.embed_query(
    text=query
)

# size of embeddings

len(embeddings_large)

# create the loader

loader = PyPDFLoader(file_path="../Openclaw_Research_Report.pdf")

docs = loader.load()

len(docs)

# split documents

chunker = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = chunker.split_documents(docs)

len(chunks)

# embed documents

text_documents = [doc.page_content for doc in chunks]

print(len(text_documents))

document_embeddings = embedder_large.embed_documents(
    texts=text_documents
)

embedder_large_custom_dim = OpenAIEmbeddings(
    model=MODEL_LARGE,
    dimensions=256
)

query_embeddings = embedder_large_custom_dim.embed_query(text=query)