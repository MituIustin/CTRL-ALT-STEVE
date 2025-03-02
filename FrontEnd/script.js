window.onload = function () {
  var workspace = Blockly.inject('blocklyDiv', {
    toolbox: document.getElementById('toolbox'),
    scrollbars: true,
    trashcan: true,
    theme: window.darkTheme
  });

  Blockly.defineBlocksWithJsonArray([
    {
      "type": "input_prompt",
      "message0": "input()",
      "output": "String",
      "colour": 160,
      "tooltip": "Enter your input",
      "helpUrl": ""
    }
  ]);

  Blockly.Python['input_prompt'] = function(block) {
    return ['input()', Blockly.Python.ORDER_ATOMIC];
  };

  function updateCode() {
    var code = Blockly.Python.workspaceToCode(workspace);
    document.getElementById('codeArea').textContent = code;
    Prism.highlightElement(document.getElementById('codeArea'));
  }

  workspace.addChangeListener(updateCode);

  function runCode() {
    var code = Blockly.Python.workspaceToCode(workspace);
    var userInput = document.getElementById('userInput').value;
    var inputs = userInput.split('\n');
    var inputCount = (code.match(/input\(\)/g) || []).length;

    if (inputCount != 0) {
      if (inputs.length != inputCount || inputs[0] == "") {
        document.getElementById('consoleOutput').textContent = 'Error: Not enough input values or too many. Expected ' + inputCount + ' values.';
        return; 
      }
    }

    code = code.replace(/input\(\)/g, function() {
      return `"${inputs.shift() || ''}"`;  
    });

    fetch('http://127.0.0.1:5000/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('consoleOutput').textContent = data.output;
    })
    .catch(error => {
      document.getElementById('consoleOutput').textContent = 'Error: ' + error.message;
    });
  }

  function checkCode() {
  }

  function askAI() {
    prompt = "Give a short hint for checking if a number 'x' is between two other numbers 'a' and 'b'. Use just words, i dont need any fancy stuff, just words, dont exceed 150 words"

    fetch('http://127.0.0.1:5000/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: prompt })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data)
    })
    .catch(error => console.error('Error: ', error));
  }  

  document.getElementById('runBtn').addEventListener('click', runCode);
  document.getElementById('askAI').addEventListener('click', askAI);
  document.getElementById('check').addEventListener('click', checkCode);

  updateCode();
};
