from langchain_community.document_loaders import PyPDFLoader,PDFMinerLoader,PDFPlumberLoader
from pathlib import Path
from pprint import pp
from langchain_community.document_loaders.parsers import TesseractBlobParser, RapidOCRBlobParser
file_path = Path("C:/Users/mukes/Downloads/langchain/attention_is_all_you_need.pdf")

"""pypdf_loader=PyPDFLoader(file_path=file_path.as_posix(),mode='page')
documents=pypdf_loader.load()

print(documents[0].page_content)
print(documents[0].metadata)"""

"""pdfminer_loader=PDFMinerLoader(file_path=file_path.as_posix(),
                               mode="page",
                               extract_images=True,
                               images_parser=RapidOCRBlobParser(),
                               images_inner_format="html-img")

documents_with_images=pdfminer_loader.load()

print(documents_with_images[3].page_content)"""


plumber_loader=PDFPlumberLoader(file_path=file_path.as_posix(),
                                mode="page")

documents_with_metadata=plumber_loader.load()

print(documents_with_metadata[0].metadata)



