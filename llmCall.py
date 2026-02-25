import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

#initialise the model
model = GoogleGenerativeAI(model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.1)
#prepare message
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of India?"}
]


#invoke the model
response = model.invoke(messages)
print(response)