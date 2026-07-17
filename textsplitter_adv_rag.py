from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

text="""Artificial intelligence is transforming technology and shaping the future. 
Machine learning algorithms are becoming more sophisticated every day.
Deep learning models can now process vast amounts of data efficiently.

Natural language processing has made significant strides in recent years.
Computer vision systems can now identify objects with remarkable accuracy.
Reinforcement learning is enabling robots to learn complex tasks autonomously.

The impact of AI extends across multiple industries including healthcare, finance, and transportation.
Ethical considerations around AI development are becoming increasingly important.
Researchers are working on making AI systems more transparent and explainable."""


splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    length_function=len,
    separator=" "
)

# split the text

# create token based splitter

token_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    chunk_size=50,
    chunk_overlap=5
)

# split the text

token_splitter.split_text(text)

chunks = splitter.split_text(text)

print(chunks)
print(f"Number of Chunks {len(chunks)}")



docs = [Document(
    page_content=text,
    metadata={"source": "Text on AI"}
)]

print(docs)

# create splitter

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=""
)

chunks = splitter.split_documents(docs)

print(chunks)