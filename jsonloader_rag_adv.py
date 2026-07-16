from langchain_community.document_loaders import JSONLoader
from pathlib import Path
from pprint import pp

file_path = Path("C:/Users/mukes/Downloads/langchain/apparels.json")
def metadat_func(record:dict,metadata:dict):
    metadata["product_name"]=record["productName"]
    metadata["category"]=record["category"]
    return metadata
loader=JSONLoader(file_path=file_path.as_posix(),
                  jq_schema=".products[]",
                  content_key="Description",
                  metadata_func=metadat_func)

documents=loader.load()

for doc in documents:
    print(doc.page_content,end="\n\n")

