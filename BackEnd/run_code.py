import subprocess
import tempfile
import os

def run_code(code):
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

    return {'output': output}
