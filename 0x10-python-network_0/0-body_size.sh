#!/bin/bash
# This script takes in a URL, sends a request, and displays the size of the body in bytes

curl -s "$1" -o /dev/null -w '%{size_download}\n'
