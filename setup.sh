#!/bin/bash

set -e

python3.12 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install \
  torch==2.13.0 \
  torchvision==0.28.0 \
  --index-url https://download.pytorch.org/whl/cpu

pip install -r requirements.txt

echo "Instalación finalizada"