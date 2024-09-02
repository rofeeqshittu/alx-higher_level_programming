#!/bin/bash
# Sends a JSON POST request with the content of the file
curl -s -X POST -H "content-Type: application/json" -d @"$2" "$1"
