window.darkTheme = Blockly.Theme.defineTheme('dark', {
    base: Blockly.Themes.Classic,
    blockStyles: {
      logic_blocks: { colourPrimary: '#2196F3', colourSecondary: '#1976D2', colourTertiary: '#0D47A1' },
      loop_blocks: { colourPrimary: '#f05b63', colourSecondary: '#00ACC1', colourTertiary: '#0097A7' },
      math_blocks: { colourPrimary: '#4CAF50', colourSecondary: '#388E3C', colourTertiary: '#2E7D32' },
      text_blocks: { colourPrimary: '#9C27B0', colourSecondary: '#8E24AA', colourTertiary: '#7B1FA2' },
      list_blocks: { colourPrimary: '#E91E63', colourSecondary: '#D81B60', colourTertiary: '#C2185B' },
      variable_blocks: { colourPrimary: '#3F51B5', colourSecondary: '#303F9F', colourTertiary: '#1A237E' },
      function_blocks: { colourPrimary: '#8E24AA', colourSecondary: '#7B1FA2', colourTertiary: '#6A1B9A' },
      control_blocks: { colourPrimary: '#faac78', colourSecondary: '#E64A19', colourTertiary: '#D32F2F' } 
    },
    categoryStyles: {
      logic_category: { colour: '#2196F3' },
      loop_category: { colour: '#00BCD4' },
      math_category: { colour: '#4CAF50' },
      text_category: { colour: '#9C27B0' },
      list_category: { colour: '#E91E63' },
      variable_category: { colour: '#3F51B5' },
      function_category: { colour: '#8E24AA' },
      control_category: { colour: '#FF5722' } 
    },
    componentStyles: {
      workspaceBackgroundColour: '#1e1e1e',
      toolboxBackgroundColour: '#2a2a2a',
      toolboxForegroundColour: '#fff',
      flyoutBackgroundColour: '#252526',
      flyoutForegroundColour: '#ccc',
      flyoutOpacity: 1,
      scrollbarColour: '#797979',
      insertionMarkerColour: '#fff',
      insertionMarkerOpacity: 0.3,
      scrollbarOpacity: 0.4,
      cursorColour: '#d0d0d0'
    }
});
