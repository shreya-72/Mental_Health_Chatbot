import os


import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')


def text_completion(prompt: str) -> dict:
    base_prompt = "You are a helpful and supportive counselling agent designed to assist with mental health. Please provide guidance to the user."
    full_prompt = f'{base_prompt}\nHuman: {prompt}\nAI: 
    try:
        response = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt=full_prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
        
