from langchain_text_splitters import CharacterTextSplitter

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

chunks = splitter.split_text(text)

print(chunks)
print(f"Number of Chunks {len(chunks)}")