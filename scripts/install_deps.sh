#!/bin/sh
# Install backend Python dependencies without proxy issues
unset https_proxy HTTP_PROXY http_proxy HTTPS_PROXY
pip install -r backend/requirements.txt
