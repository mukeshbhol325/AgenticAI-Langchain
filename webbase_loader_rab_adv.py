from langchain_community.document_loaders import WebBaseLoader,RecursiveUrlLoader
from pprint import pp

url="https://docs.langchain.com/oss/python/langchain/models"

loader=RecursiveUrlLoader(url=url,max_depth=2)

documents=loader.lazy_load()

counter=0

for document in documents:
    #stop condition
    if counter == 20:
        break
    counter+=1

    print(document.page_content[0:300])    

##print(documents[0].page_content)