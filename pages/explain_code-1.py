
import streamlit as st
from dotenv import load_dotenv
import openai
import json
from collections import namedtuple
# import os 
# from myutility import parse_json
# from utility.py import parse_json(a)

load_dotenv(".streamlit/secrets.toml")

api_key_2 =os.environ['OPENAI_API_KEY']

# st.write(api_key_1)
# st.write(api_key_2)

# def main():
    
client = openai.OpenAI(api_key=api_key_2) 
 
with st.form(key = 'userdata'):
        st.write('data')
        prompt=st.text_area(label = "Enter the python code :")
        
        submit_form = st.form_submit_button(label="submit", help="Click to submit")
        if submit_form:
         response = client.chat.completions.create( 
         model="gpt-4",
         messages=[{
           "role": "system",
           "content": "You will be provided with a piece of code, and your task is to explain it in a concise way.."
                },
              {
                 "role": "user",
                "content": prompt
                }],
     temperature=0,
     max_tokens=1024,
     top_p=1,
    frequency_penalty=0,
     presence_penalty=0
)
         st.write(response.choices[0].message.content)

# if __name__ == '__main__':
#     main()