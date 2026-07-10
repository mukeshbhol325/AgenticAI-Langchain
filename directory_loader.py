from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,TextLoader

loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()
# Load all TXT files
txt_loader = DirectoryLoader(
    "documents",
    glob="**/*.txt",
    loader_cls=TextLoader
)

# Combine the documents
documents = docs + txt_loader.lazyload()
print(len(docs))