# Import the required libraries
import openai
# import os
import streamlit as st
from PIL import Image

image = Image.open('docbot.jpg')


st.set_page_config(
    page_title="DocSummarizer",
page_icon=image,
)

# Set the GPT-3 API key
openai.api_key = st.secrets["pass"]


st.image(image)
st.title("DocSummarizer : openAI GPT-3 + docs.netapp.com + Streamlit")

# Read the text of the article from a file
# with open("article.txt", "r") as f:
#     article_text = f.read()
article_text = st.text_area("Go ahead! Give me the docs.netapp.com content you need me to summarize for you, puny human.")
output_size = st.radio(label = "What do you need me to give you?", 
                    options= ["Business card edition (I'm having an important business lunch)", "3 x 5 index card edition (I need to impress my teacher)", "Page edition (Let's go wild)"])

if output_size == "To-The-Point":
    out_token = 50
elif output_size == "Concise":
    out_token = 128
else:
    out_token = 516

if len(article_text)>100:
    if st.button("Generate Summary",type='primary'):
    # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Please summarize this article in a few sentences: " + article_text,
            max_tokens = out_token,
            temperature = 0.5,
        )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.success(res)
        st.download_button('Download result', res)
else:
    st.warning("Not enough words to summarize!")
