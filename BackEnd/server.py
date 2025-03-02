from flask import Flask, request, jsonify
from flask_cors import CORS
from crud_table import *  
from crud_row import *  
from run_code import run_code  
from ai_response import ask_ai  

app = Flask(__name__)
CORS(app)

# Run Python Code
@app.route('/run', methods=['POST'])
def run_code_request():
    data = request.get_json()
    code = data.get('code', '')

    try:
        result = run_code(code) 
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Get HINT from AI
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    try:
        result = ask_ai(prompt)  
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Create Table
@app.route('/tables', methods=['POST'])
def create_new_table():
    data = request.get_json()
    table_name = data.get('table_name')
    columns = data.get('columns')

    if not table_name or not columns:
        return jsonify({'error': 'Table name and columns are required'}), 400

    try:
        result = create_table(table_name, columns)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Read Table
@app.route('/tables', methods=['GET'])
def get_all_tables():
    try:
        tables = list_tables()
        return jsonify(tables)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Edit Table
@app.route('/tables/<table_name>', methods=['PUT'])
def modify_existing_table(table_name):
    data = request.get_json()
    add_columns = data.get("add_columns")
    drop_columns = data.get("drop_columns")

    try:
        result = modify_table(table_name, add_columns=add_columns, drop_columns=drop_columns)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Delete Table
@app.route('/tables/<table_name>', methods=['DELETE'])
def delete_table_by_name(table_name):
    try:
        result = delete_table(table_name)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Create Row
@app.route('/tables/<table_name>/rows', methods=['POST'])
def create_row(table_name):
    data = request.get_json()
    row_data = data.get('row')  

    if not row_data:
        return jsonify({'error': 'Row data is required'}), 400

    try:
        result = insert_row(table_name, row_data)  
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Read Row
@app.route('/tables/<table_name>/rows', methods=['GET'])
def get_rows(table_name):
    try:
        rows = select_rows(table_name) 
        return jsonify(rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Edit Row
@app.route('/tables/<table_name>/rows/<row_id>', methods=['PUT'])
def modify_row(table_name, row_id):
    data = request.get_json()
    updated_data = data.get('updated_row')  

    if not updated_data:
        return jsonify({'error': 'Updated row data is required'}), 400

    try:
        result = update_row(table_name, row_id, updated_data)  
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Delete Row
@app.route('/tables/<table_name>/rows/<row_id>', methods=['DELETE'])
def delete_row(table_name, row_id):
    try:
        result = delete_row(table_name, row_id)  
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
