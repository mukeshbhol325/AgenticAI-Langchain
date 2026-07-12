from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]
embedding_model=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vectorestore=Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name='my_collection'
)

retriver=vectorestore.as_retriever(
    search_type="mmr",
    serach_kwargs={'k':2,"lambda_mult":1}) #k=top results,lambda_mult=relevance diversity balance

query="WHat is Chroma used for ?"

result=retriver.invoke(query)

print(result[0])