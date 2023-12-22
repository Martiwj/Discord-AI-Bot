from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API token from your .env file
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_chat_completion(prompt, model="gpt-3.5-turbo"):
    
    # Creating a message as required by the API
    messages = [{"role": "user", "content": prompt}]
  
    # Calling the ChatCompletion API
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        
    )

    # Accessing the generated content from the response
    generated_content = response.choices[0].message.content

    # Returning the extracted response
    return generated_content

