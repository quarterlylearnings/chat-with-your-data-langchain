from langchain.text_splitter import TokenTextSplitter
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("docs/prayer-project.pdf")
docs = loader.load()

text_splitter = TokenTextSplitter(chunk_size=1, chunk_overlap=0)

chunks = text_splitter.split_documents(docs)

print("There are", len(chunks), "chunks.")
print("first Chunk ------------:", chunks[0])
print("first Chunk ------------:", chunks[1])
print("first Chunk ------------:", chunks[2])
print("first Chunk ------------:", chunks[3])
print("first Chunk ------------:", chunks[4])
print("first Chunk ------------:", chunks[500])