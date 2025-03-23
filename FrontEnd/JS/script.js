window.onload = function () {
  const script = document.createElement('script');
  script.src = 'JS/input_block.js';
  document.head.appendChild(script);

  script.onload = function () {
    var workspace = Blockly.inject('blocklyDiv', {
      toolbox: document.getElementById('toolbox'),
      scrollbars: true,
      trashcan: true,
      theme: window.darkTheme
    });

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

      code = code.replace(/input\(\)/g, function () {
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

    function askAI() {
      prompt = "Give a short hint for checking if a number 'x' is between two other numbers 'a' and 'b'. Use just words, i dont need any fancy stuff, just words, dont exceed 150 words";

      fetch('http://127.0.0.1:5000/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: prompt })
      })
        .then(response => response.json())
        .then(data => {
          console.log(data);
        })
        .catch(error => console.error('Error: ', error));
    }

    function checkCode() {
      var code = Blockly.Python.workspaceToCode(workspace);
      fetch('http://127.0.0.1:5000/get_test_cases', {
          method: 'GET',
          headers: { 'Content-Type': 'application/json' }
      })
      .then(response => response.json())
      .then(testCases => {
          console.log("✅ Test cases received:", testCases);
  
          var filteredTestCases = testCases.rows;
          var passedTests = 0;
          var totalTests = filteredTestCases.length;
          var testPromises = [];
  
          filteredTestCases.forEach(test => {
              var inputData = test[3]; 
              var expectedOutput = test[4]; 
  
              console.log(`Running test case: input=${inputData}, expected=${expectedOutput}`);
  
              var inputValues = inputData.split(' ').map(val => val.trim());
              var userCode = code.replace(/input\(\)/g, function () {
                  return `"${inputValues.shift() || ''}"`;
              });
  
              var testPromise = fetch('http://127.0.0.1:5000/run', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ code: userCode })
              })
              .then(response => response.json())
              .then(data => {
                  console.log("Execution result:", data);
                  var userOutput = data.output.trim();
  
                  if (userOutput === expectedOutput.trim()) {
                      passedTests++;
                  }
              })
              .catch(error => {
                  console.error('Error running test case:', error);
              });
  
              testPromises.push(testPromise);
          });
          debugger;
          Promise.all(testPromises).then(() => {
              var score = (passedTests / totalTests) * 100;
              console.log(`Final score: ${score}%`);
  
              document.getElementById('consoleOutput').textContent = 
                  `You passed ${passedTests} out of ${totalTests} tests. Score: ${score}%`;
  
              return fetch('http://127.0.0.1:5000/submit_score', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({
                      user_id: 1,
                      problem_id: 1,
                      code: code,
                      score: score
                  })
              });
              
          })
          .then(response => response.json())
          .then(data => {
              console.log('✅ Submission saved:', data);
              console.log("🚀 Page should NOT reload now!");
          })
          .catch(error => {
              console.error('Error submitting score:', error);
          });
      })
      .catch(error => {
          console.error('Error fetching test cases:', error);
          document.getElementById('consoleOutput').textContent = 
              'Error fetching test cases: ' + error.message;
      });
  }
  
    document.getElementById('runBtn').addEventListener('click', runCode);
    document.getElementById('askAI').addEventListener('click', askAI);
    document.getElementById('check').addEventListener('click', function(event) {
      console.log("🔹 Button clicked - preventing default behavior.");
      event.preventDefault();
      event.stopPropagation(); 
      checkCode();
  });

    updateCode();
  };
};
