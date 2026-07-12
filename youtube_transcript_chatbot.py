from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

video_id = "Gfr50f6ZBvo" # only the ID, not full URL
try:
    ytt_api = YouTubeTranscriptApi()
    transcript_all = ytt_api.fetch("Gfr50f6ZBvo")

    # Flatten it to plain text
    transcript =" ".join(snippet.text for snippet in transcript_all)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_store = FAISS.from_documents(chunks, embeddings)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0.2)

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

question          = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs    = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt = prompt.invoke({"context": context_text, "question": question})


def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough(question)
})

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

main_chain.invoke('Can you summarize the video')
