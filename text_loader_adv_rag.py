from pprint import pp
from langchain_community.document_loaders import TextLoader
from pathlib import Path


file_path = Path("C:/Users/mukes/Downloads/langchain/transformers.txt")

print(file_path.exists())

loader=TextLoader(file_path=file_path)

documents=loader.load()

print(type(documents))

extracted_document=documents[0]
print(extracted_document.page_content)
print(extracted_document.metadata)