import streamlit as st
from dotenv import load_dotenv
import openai
import json
from collections import namedtuple


assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-4-1106-preview",
  tools=[{"type": "code_interpreter"}]
)

