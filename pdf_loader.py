from langchain_community.document_loaders import PyPDFLoader
"""unstructuredPDFLoader for scanned/image pdf loader"""
loader=PyPDFLoader('dl-curriculum.pdf')

docs=loader.load()

print(docs[0].page_content)