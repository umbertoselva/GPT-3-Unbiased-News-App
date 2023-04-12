import streamlit as st
import openai
import os
from unbiased_news.functions import unbiased_news

try:
  openai.api_key = os.getenv('OPENAI_KEY')
  
  if "unbiased_news" not in st.session_state:
      st.session_state["unbiased_news"] = ""
  
  st.title("Unbiased News App")
  
  input_text = st.text_area(label="Enter a news article:", value="", height=250)
  st.button(
      "Submit",
      on_click=unbiased_news,
      kwargs={"prompt": input_text},
  )
  output_text = st.text_area(label="Output:", value=st.session_state["unbiased_news"], height=250)
except:
  st.write('There was an error =(')