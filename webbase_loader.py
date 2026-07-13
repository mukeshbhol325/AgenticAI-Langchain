from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
vall=0
prompt1=PromptTemplate(
    template='Answer the following \n {question} from the following -\n {text}',
    input_variable=['question','text']
)

parser=StrOutputParser()

url='https://www.gsmarena.com/apple_iphone_17-14050.php'

loader=WebBaseLoader(url)

docs=loader.load()

chain=prompt1|model|parser

print(chain.invoke({'question':'What is the RAM of the product','text':docs[0].page_content}))

