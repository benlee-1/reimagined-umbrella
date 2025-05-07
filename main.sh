#!/bin/bash
cd "$(dirname "$0")"  # Change to the script's directory
python3 -m src.main
cd public && python3 -m http.server 8888