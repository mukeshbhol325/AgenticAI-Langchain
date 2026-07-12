from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from dotenv import load_dotenv

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two input a and b"""
    return a * b

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage(content="can you multiply 4 with 8")
message = [query]

result = llm_with_tools.invoke(message)

message.append(result)

tool_result = multiply.invoke(result.tool_calls[0]["args"])

tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=result.tool_calls[0]["id"]
)

message.append(tool_message)

final_result = llm_with_tools.invoke(message)

print(final_result.content)