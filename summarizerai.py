# Import the required libraries
import openai
# import os
import streamlit as st
from PIL import Image

image = Image.open('docbot.jpg')


st.set_page_config(
    page_title="DocTranslator",
page_icon=image,
)


openai.api_key = st.secrets["pass"]


st.image(image)
st.title("DocTranslator : openAI GPT-4 + Streamlit")


article_text = st.text_area("Provide your text in English.")
output_size = st.radio(label = "What language would you like to translate?", 
                    options= ["Japanese", "French", "Spanish"])

if output_size == "Japanese":
    language = "Please translate this text from English into Japanese: "
elif output_size == "French":
    language = "Please translate this text from English into French: "
else:
    language = "Please translate this text from English into Spanish: "

   
message=[{"role": "user", "content": language + article_text}] 
print(message)

if len(article_text)>100:
    if st.button("Generate Translation",type='primary'):
    # Use GPT-4 to generate a summary of the article
        response = openai.Completion.create(
            model="gpt-4",
            #prompt= language + article_text,
            messages = message,
            max_tokens = None,
            temperature = 1,
        )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.success(res)
        st.download_button('Download result', res)
else:
    st.warning("Not enough words to translate!")
