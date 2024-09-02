#!/bin/bash
# Sends a DELETE request to the URL passed as first argument & display the body of the response
curl -sX DELETE "$1"
