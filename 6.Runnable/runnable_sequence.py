from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence


load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt=PromptTemplate(
    template='write a joke about {topic}',
    input_variable=['topic']
)

parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the joke {text}',
    input_variable=['text']
)

chain=RunnableSequence(prompt,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))