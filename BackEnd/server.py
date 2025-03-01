from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import os
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = ""

def ask_ai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],  
            max_tokens=150 
        )
        
        # Extrage și returnează textul generat
        return response['choices'][0]['message']['content'].strip()

    except openai.OpenAIError as e:
        return f"OpenAI API Error: {str(e)}"

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '')
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode='w') as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        result = subprocess.run(['python', tmp_path], capture_output=True, text=True, timeout=5)
        output = result.stdout + result.stderr
    except Exception as e:
        output = str(e)
    finally:
        os.remove(tmp_path)
    
    return jsonify({'output': output})

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt', '')
    response = ask_ai(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
