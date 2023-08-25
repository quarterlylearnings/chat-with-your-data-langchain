import os
import openai
from langchain.document_loaders import PyPDFLoader
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

loader = PyPDFLoader("prayer-project.pdf")

pages = loader.load()

print(len(pages))