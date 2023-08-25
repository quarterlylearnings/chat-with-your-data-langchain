import os
import openai

from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.environ['OPENAI_API_KEY']

url="https://www.youtube.com/watch?v=dFxaEVQdFr0"
save_dir="docs/transcript/"
loader=GenericLoader(YoutubeAudioLoader([url],save_dir),OpenAIWhisperParser())
docs=loader.load()

print(docs[0].page_content[0:1000])