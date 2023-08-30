from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

loader = PyPDFLoader("docs/prayer-project.pdf")
pages = loader.load()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=150,
    length_function=len
)

docs = text_splitter.split_documents(pages)

print("Number of documents", len(docs))
print("Number of pages", len(pages))

print("first chunk", docs[0:2])