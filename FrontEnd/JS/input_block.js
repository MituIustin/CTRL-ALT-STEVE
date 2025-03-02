Blockly.defineBlocksWithJsonArray([
    {
      "type": "input_prompt",
      "message0": "input",
      "output": "String",
      "colour": 160,
      "tooltip": "Enter your input",
      "helpUrl": ""
    }
  ]);
  
  Blockly.Python['input_prompt'] = function(block) {
    return ['input()', Blockly.Python.ORDER_ATOMIC];
  };
  