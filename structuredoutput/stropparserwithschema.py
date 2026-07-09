from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()



model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser=JsonOutputParser()
template=PromptTemplate(
    template="Give me the name,age and city of a fictional person \n {format_instruction}",
    input_variable=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain=template|model|parser
final_result=chain.invoke({})
print(final_result)