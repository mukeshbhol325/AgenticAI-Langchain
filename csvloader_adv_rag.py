from langchain_community.document_loaders import CSVLoader
from pathlib import Path
from pprint import pp

file_path=Path("C:/Users/mukes/Downloads/langchain/organizations.csv")

loader=CSVLoader(file_path=file_path,
                 source_column="industry",
                 metadata_columns=["Website","Founded"])

documents=loader.load()

print(documents[0].page_content)
print(documents[0].page_content)
