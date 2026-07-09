from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=PromptTemplate(
    template='Generative a detailled report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a 5 pointer summary from the follwong text \n {text}',
    input_variables=['text']

)

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser=StrOutputParser()
chain=prompt1|model|parser|prompt2|model|parser
result=chain.invoke({'topic':'unemployment in india'})
##print(result)
chain.get_graph().print_ascii()