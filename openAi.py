from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API token from your .env file
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_chat_completion(prompt, model="gpt-4"):
    
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


def create_image(prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt, 
    size="1024x1024",
    quality="standard",
    n=1,
    )   

    image_url = response.data[0].url
    return image_url
