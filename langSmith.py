from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
import gradio as gr
import os
from google.colab import userdata

OPENAI_API_KEY = userdata.get("openAI")


# For Google Colab
import os

os.environ["OPENAI_API_KEY"] = openai_key               # your OpenAI key
os.environ["LANGCHAIN_API_KEY"] = langsmith_key            # your LangSmith key
os.environ["LANGCHAIN_TRACING"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "22-oct-SDA"       # project name      # any project name you like

import openai
from langsmith.wrappers import wrap_openai
from langsmith import traceable
# Auto-trace LLM calls in-context
client = wrap_openai(openai.Client(api_key=openai_key))

@traceable # Auto-trace this function
def pipeline(user_input: str):
    result = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="gpt-5-nano"
    )
    return result.choices[0].message.content

pipeline("Write a blog on AI uses")
