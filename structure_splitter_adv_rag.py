from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

text = """Hi how are you
My name is Rahul

I am teaching RAG
We are Learning about RAG"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

splitter.split_text(text)

# create the list of documents

list_of_text = [text, example_text]

docs = [Document(page_content=text) for text in list_of_text]

print(docs)