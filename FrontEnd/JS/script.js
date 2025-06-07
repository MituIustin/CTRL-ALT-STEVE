window.onload = function () {
  const workspace = Blockly.inject('blocklyDiv', {
    toolbox: document.getElementById('toolbox'),
    scrollbars: true,
    trashcan: true,
    theme: window.darkTheme
  });

  function colorBlocksByCategory() {
    const toolbox = document.getElementById('toolbox');
    const categories = toolbox.getElementsByTagName('category');

    Array.from(categories).forEach(category => {
      const color = category.getAttribute('colour');
      const blocks = category.getElementsByTagName('block');

      Array.from(blocks).forEach(block => {
        const type = block.getAttribute('type');
        const blockDef = Blockly.Blocks[type];

        if (blockDef && typeof blockDef.init === 'function') {
          const originalInit = blockDef.init;
          blockDef.init = function () {
            originalInit.call(this);
            this.setColour(parseInt(color));
          };
        }
      });
    });
  }

  colorBlocksByCategory();

  let worker = null;
  let timeoutId = null;

  function sendToWorker(code, callback) {
    if (worker) {
      worker.terminate();
      worker = null;
    }

    worker = new Worker('JS/skulptWorker.js');

    timeoutId = setTimeout(() => {
      if (worker) {
        worker.terminate();
        worker = null;
        callback("Execution halted due to an infinite loop.", false);
      }
    }, 2000);

    worker.onmessage = function (e) {
      clearTimeout(timeoutId);
      if (e.data.success) {
        window.lastActions = e.data.actions;
        callback(null, true);
      } else {
        callback("Execution halted due to error: " + e.data.error, false);
      }
      worker.terminate();
      worker = null;
    };

    worker.postMessage({ code });
  }

  function generateCodeOnly() {
    const code = Blockly.Python.workspaceToCode(workspace).trim();
    const codeArea = document.getElementById('pythonCode');

    codeArea.textContent = code || "No code generated.";
    Prism.highlightElement(codeArea);

    if (!code) return;

    sendToWorker(code, (error, success) => {
      if (!success && error) {
        codeArea.textContent = error;
        Prism.highlightElement(codeArea);
      }
    });
  }

  function runCode() {
    const code = Blockly.Python.workspaceToCode(workspace).trim();
    const codeArea = document.getElementById('pythonCode');

    if (!code) {
      codeArea.textContent = "No code generated.";
      Prism.highlightElement(codeArea);
      return;
    }

    codeArea.textContent = code;
    Prism.highlightElement(codeArea);

    sendToWorker(code, (error, success) => {
      if (!success && error) {
        codeArea.textContent = error;
        Prism.highlightElement(codeArea);
      }
    });
  }

  document.getElementById("genBtn").addEventListener("click", generateCodeOnly);
  document.getElementById("runBtn").addEventListener("click", runCode);
};
