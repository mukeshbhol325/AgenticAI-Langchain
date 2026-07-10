from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch


def word_counter(text):
    return len(text.split())

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1=PromptTemplate(
    template='write a detailled report on {topic}',
    input_variable=['topic']
)

prompt2=PromptTemplate(
    template='summarize the following \n {text}',
    input_variable=['text']
)

parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({'topic':'Russia Vs Ukraine'}))

