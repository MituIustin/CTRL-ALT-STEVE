Blockly.defineBlocksWithJsonArray([
    {
      "type": "attack",
      "message0": "attack",
      "previousStatement": null,
      "nextStatement": null,
      "colour": 30,
      "tooltip": "Attack an enemy around you.",
      "helpUrl": ""
    }]
)

Blockly.Python['attack'] = function(block) {
  return "player.attack()\n";
};

Blockly.defineBlocksWithJsonArray([
  {
    "type": "use",
    "message0": "use",
    "previousStatement": null,
    "nextStatement": null,
    "colour": 30,
    "tooltip": "Use an item / Interact with somebody or someone.",
    "helpUrl": ""
  }]
)

Blockly.Python['use'] = function(block) {
return "player.use()\n";
};

Blockly.defineBlocksWithJsonArray([
  {
    "type": "scan",
    "message0": "scan",
    "previousStatement": null,
    "nextStatement": null,
    "colour": 30,
    "tooltip": "Scan a file",
    "helpUrl": ""
  }]
)

Blockly.Python['scan'] = function(block) {
return "player.scan()\n";
};

Blockly.defineBlocksWithJsonArray([
  {
    "type": "mine",
    "message0": "mine",
    "previousStatement": null,
    "nextStatement": null,
    "colour": 30,
    "tooltip": "Mine a encrypted data block",
    "helpUrl": ""
  }]
)

Blockly.Python['mine'] = function(block) {
return "player.mine(data_block)\n";
};