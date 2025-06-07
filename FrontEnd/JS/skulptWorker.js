importScripts('skulpt.min.js', 'skulpt-stdlib.js');

onmessage = async function (e) {
  const code = e.data.code;

  const setupCode = `
actions = []

class Player:
    def move_left(self):
        actions.append("moveLeft")

    def move_right(self):
        actions.append("moveRight")

    def move_up(self):
        actions.append("moveUp")

    def move_down(self):
        actions.append("moveDown")

    def attack(self):
        actions.append("attack")

    def use(self):
        actions.append("use")

    def scan(self):
        actions.append("scan")

    def mine(self, arg1):
        actions.append("mine")

player = Player()
data_block = None
`;

  const fullCode = setupCode + "\n" + code;

  Sk.configure({
    output: function () {},
    read: function (x) {
      if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined) {
        throw "File not found: '" + x + "'";
      }
      return Sk.builtinFiles["files"][x];
    },
    __future__: Sk.python3
  });

  Sk.globals = {};

  try {
    await Sk.misceval.asyncToPromise(() =>
      Sk.importMainWithBody("<stdin>", false, fullCode, true)
    );
    postMessage({ success: true, actions: Sk.globals.actions || [] });
  } catch (err) {
    postMessage({ success: false, error: err.toString() });
  }
};
