#!/bin/bash

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

npm install commitizen -g --prefix /home/vscode/node_modules
commitizen init cz-conventional-changelog --save-dev --save-exact

npm install --save-dev @commitlint/cli --prefix /home/vscode/node_modules
npm install --save-dev @commitlint/config-conventional --prefix /home/vscode/node_modules
echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js


npm install husky --save-dev --prefix /home/vscode/node_modules
npx husky install --prefix /home/vscode/node_modules


if [ ! -f ".husky/prepare-commit-msg" ]
then
    npx husky add .husky/prepare-commit-msg "exec < /dev/tty && git cz --hook || true"
fi

if [ ! -f ".husky/commit-msg" ]
then
    npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
fi

poetry install
poetry update

git config --local core.editor "vi"

/bin/bash .devcontainer/vscode_settings.sh
