#!/bin/bash

/bin/bash .devcontainer/download_dify_tools.sh
if [ -f "requirements.txt" ]; then
  pip3 install --user -r requirements.txt
fi
