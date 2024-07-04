---
# 0x10. Python - Network #0

## Overview
This project is part of the ALX SE Foundations curriculum, focusing on understanding and using HTTP and cURL for various network operations. The tasks involve creating Bash scripts and Python functions to perform specific HTTP requests and manipulate URLs.

## Files

- `0-body_size.sh`: Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.
- `1-body.sh`: Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response if the status code is 200.
- `2-delete.sh`: Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
- `3-methods.sh`: Bash script that takes in a URL and displays all HTTP methods the server will accept.
- `4-header.sh`: Bash script that takes in a URL as an argument, sends a GET request to the URL with a custom header variable, and displays the body of the response.
- `5-post_params.sh`: Bash script that takes in a URL, sends a POST request to the URL with specified parameters, and displays the body of the response.
- `6-peak.py`: Python script that contains a function to find a peak in a list of unsorted integers.
- `6-peak.txt`: Text file containing the complexity of the algorithm used in `6-peak.py`.

## Tasks

### 0. cURL body size
**File**: `0-body_size.sh`

**Description**: Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response. The size must be displayed in bytes. You have to use `curl`.

### 1. cURL to the end
**File**: `1-body.sh`

**Description**: Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response. Display only the body of a 200 status code response. You have to use `curl`.

### 2. cURL Method
**File**: `2-delete.sh`

**Description**: Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response. You have to use `curl`.

### 3. cURL only methods
**File**: `3-methods.sh`

**Description**: Write a Bash script that takes in a URL and displays all HTTP methods the server will accept. You have to use `curl`.

### 4. cURL headers
**File**: `4-header.sh`

**Description**: Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`. You have to use `curl`.

### 5. cURL POST parameters
**File**: `5-post_params.sh`

**Description**: Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable `email` must be sent with the value `test@gmail.com` and a variable `subject` must be sent with the value `I will always be here for PLD`. You have to use `curl`.

### 6. Find a peak
**File**: `6-peak.py`, `6-peak.txt`

**Description**: Write a function that finds a peak in a list of unsorted integers. The algorithm must have the lowest complexity possible. There may be more than one peak in the list.

---
