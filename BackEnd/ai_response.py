import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_ai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150 
        )
        
        return {'response': response['choices'][0]['message']['content'].strip()}

    except openai.OpenAIError as e:
        return {'error': f"OpenAI API Error: {str(e)}"}
