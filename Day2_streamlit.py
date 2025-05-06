import sys
import streamlit as st
from streamlit.logger import get_logger
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

logger = get_logger(__name__)

import os
if os.getenv('USER', "None") == 'appuser':
    ht_token = st.secrets["HF_KEY"]
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token
else:
    # ALSO ADD HERE YOUR PROXY VARS
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["HF_KEY"]
    
st.title("my Gen AI App")
repo_id = "microsoft/Phi-3-mini-4k-instruct"
temp = 1
print(repo_id, temp)
logger.info(f"{temp=}")


with st.form("sample_app"):
    txt = st.text_area("Enter text:", "what GPT stands for?")
    sub = st.form_submit_button("submit")
    if sub:
        llm = HuggingFaceEndpoint(repo_id = repo_id, 
                                  task="text_generation", 
                                  temperature=temp
                                 )
        chat = ChatHuggingFace(llm = llm, verbose=True)

        logger.info("invoking")
        ans = chat.invoke(txt)
        st.info(ans.content)
        logger.info("Done")
        
