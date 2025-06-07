from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data['code']
    
    commands = process_code_to_commands(code)

    return jsonify({'commands': commands})

def process_code_to_commands(code):
    commands = []

    if "move_left" in code:
        commands.append("Move Left")
    

    return commands

if __name__ == '__main__':
    app.run(debug=True)
