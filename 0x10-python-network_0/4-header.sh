#!/bin/bash
# Sends a GET request to a URL with a custom header & displays the body
curl -sH "x-School-User-Id: 98" "$1"
