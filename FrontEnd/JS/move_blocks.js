Blockly.defineBlocksWithJsonArray([
    {
      "type": "move_down",
      "message0": "move down",
      "previousStatement": null,
      "nextStatement": null,
      "colour": 30,
      "tooltip": "Move the character down",
      "helpUrl": ""
    }]
)

Blockly.Python['move_down'] = function(block) {
  return "player.move_down()\n";
};


Blockly.defineBlocksWithJsonArray([
    {
      "type": "move_left",
      "message0": "move left",
      "previousStatement": null,
      "nextStatement": null,
      "colour": 30,
      "tooltip": "Move the character left",
      "helpUrl": ""
    }]
)

Blockly.Python['move_left'] = function(block) {
  return "player.move_left()\n";
};


Blockly.defineBlocksWithJsonArray([
    {
      "type": "move_right",
      "message0": "move right",
      "previousStatement": null,
      "nextStatement": null,
      "colour": 30,
      "tooltip": "Move the character right",
      "helpUrl": ""
    }]
)

Blockly.Python['move_right'] = function(block) {
  return "player.move_right()\n";
};


Blockly.defineBlocksWithJsonArray([
    {
      "type": "move_up",
      "message0": "move up",
      "previousStatement": null,
      "nextStatement": null,
      "colour": 30,
      "tooltip": "Move the character up",
      "helpUrl": ""
    }]
)

Blockly.Python['move_up'] = function(block) {
  return "player.move_up()\n";
};
