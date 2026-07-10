from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1=PromptTemplate(
    template='write a summary for following - \n {poem}',
    input_variable=['poem']
)

parser=StrOutputParser()

loader=TextLoader('cricket.txt',encoding='utf-8')

docs=loader.load()

print(docs)

print(docs[0].page_content)

chain=prompt1|model|parser

chain.invoke({'poem':docs[0].page_content})