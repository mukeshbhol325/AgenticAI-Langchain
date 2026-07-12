from langchain_core.tools import tool

@tool
def multiply(a:int,b:int)->int:
    """Multiply two number"""
    return a*b

result=multiply.invoke({'a':2,'b':5})

print(result)
print(multiply.name,multiply.description,multiply.args)