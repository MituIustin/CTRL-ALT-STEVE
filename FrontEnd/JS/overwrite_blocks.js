Blockly.Extensions.unregister('controls_if_tooltip');

Blockly.Blocks['controls_if'] = {
  init: function() {
    this.jsonInit({
      "type": "controls_if",
      "message0": "if %1 then",
      "args0": [
        {
          "type": "input_value",
          "name": "IF0",
          "check": "Boolean"
        }
      ],
      "message1": "do %1",
      "args1": [
        {
          "type": "input_statement",
          "name": "DO0"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 210, 
      "tooltip": "",
      "helpUrl": ""
    });
  }
};

Blockly.Blocks['controls_ifelse'] = {
  init: function() {
    this.jsonInit({
      "type": "controls_ifelse",
      "message0": "if %1 then",
      "args0": [
        {
          "type": "input_value",
          "name": "IF0",
          "check": "Boolean"
        }
      ],
      "message1": "do %1",
      "args1": [
        {
          "type": "input_statement",
          "name": "DO0"
        }
      ],
      "message2": "else",
      "args2": [
        {
          "type": "input_statement",
          "name": "ELSE"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 210,
      "tooltip": "",
      "helpUrl": ""
    });
  }
};