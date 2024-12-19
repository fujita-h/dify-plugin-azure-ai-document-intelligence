#!/bin/bash

# Repository information
REPO_OWNER="langgenius"
REPO_NAME="dify-plugin-daemon"
BINARY_NAME="dify-plugin-linux-amd64"
OUTPUT_DIR=".devcontainer/downloads"

# GitHub API URL
API_URL="https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/releases/latest"

# Create output directory
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# get latest release information
response=$(curl -s "$API_URL")
if [ $? -ne 0 ]; then
    echo "Failed to fetch release information from GitHub API."
    rm -rf "$OUTPUT_DIR"
    exit 1
fi

# get asset download URL
download_url=$(echo "$response" | jq -r ".assets[] | select(.name | contains(\"$BINARY_NAME\")) | .browser_download_url")

# if no binary found, exit
if [ -z "$download_url" ]; then
    echo "No binary matching '$BINARY_NAME' found in the latest release."
    rm -rf "$OUTPUT_DIR"
    exit 1
fi

# get binary file name
binary_file=$(basename "$download_url")

# download the binary
curl -L "$download_url" -o "$OUTPUT_DIR/$binary_file"
if [ $? -ne 0 ]; then
    echo "Failed to download the binary."
    rm -rf "$OUTPUT_DIR"
    exit 1
fi

echo "Downloaded $binary_file to $OUTPUT_DIR/$binary_file"

# install the binary
echo "Installing $binary_file..."
chmod +x "$OUTPUT_DIR/$binary_file"
sudo mv "$OUTPUT_DIR/$binary_file" /usr/local/bin/dify
rm -rf "$OUTPUT_DIR"

echo "Installation completed."
