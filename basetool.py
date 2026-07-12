from langchain.tools import BaseTool
from typing import Type
from pydantic import Field,BaseModel


class MultiplyInput(BaseModel):
    a:int=Field(required=True,description='the first number to multiply')
    b:int=Field(required=True,description='the second number to multiply')


class MultiplyTool(BaseTool):
    name:str='multiply'
    description:str='Multiply two numbers'

    args_schema:Type[BaseModel]=MultiplyInput

    def _run(self,a:int,b:int)->int:
        return a*b
    
multiply_tool=MultiplyTool() 
print(multiply_tool.invoke({'a':2,'b':5}))   