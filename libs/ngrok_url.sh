#!/bin/bash

echo $(curl -s localhost:4040/inspect/http | grep -oP 'window.common[^;]+' | sed 's/^[^\(]*("//' | sed 's/")\s*$//' | sed 's/\\"/"/g') | jq -r ".Session.Tunnels | values | map(.URL) | .[]" | grep "^http:"
