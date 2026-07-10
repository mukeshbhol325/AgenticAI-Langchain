from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel


load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1=PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variable=['topic']
)

parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variable=['topic']
)

chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})

print(chain.invoke({'topic':'AI'}))