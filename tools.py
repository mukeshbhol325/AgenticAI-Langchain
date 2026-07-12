from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import ShellTool
search_tool=DuckDuckGoSearchRun()

result=search_tool.invoke('latest indian news')
print(result)


shell_tool=ShellTool()

result=shell_tool.invoke('whoami')

print(result)