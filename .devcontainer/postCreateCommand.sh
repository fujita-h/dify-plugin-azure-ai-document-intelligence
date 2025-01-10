#!/bin/bash

# Install Dify Plugin CLI
curl -s https://api.github.com/repos/langgenius/dify-plugin-daemon/releases/latest \
  | jq -r ".assets[] | select(.name | test(\"dify-plugin-linux-amd64\")) | .browser_download_url" \
  | xargs -n 1 sudo curl -L -o /usr/local/bin/dify
sudo chmod +x /usr/local/bin/dify

# Install python packages
if [ -f "requirements.txt" ]; then
  pip3 install --user -r requirements.txt
fi

# Avoid to create __pycache__ directory
echo 'export PYTHONDONTWRITEBYTECODE=1' >> ~/.bashrc
