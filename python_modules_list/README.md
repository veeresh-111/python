
# os module

```python
import os

# Get current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List files in current directory
files = os.listdir(current_directory)
print("Files:", files)
```

# sys module
```python
import sys

# Print command-line arguments
print("Command-line arguments:", sys.argv)

# Exit the program
# sys.exit()
```

# subprocess module

```python
import subprocess

# Run a command and get its output
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(result.stdout.decode())
```

#shutil module
```python
import shutil

# Copy a file
shutil.copy('source.txt', 'destination.txt')
```

#json module
```python
import json

# Parse JSON data
data = '{"name": "John", "age": 30}'
parsed_data = json.loads(data)
print(parsed_data)
```

#yaml module (requires pyyaml package)
```python
import yaml

# Parse YAML data
data = """
name: John
age: 30
"""
parsed_data = yaml.safe_load(data)
print(parsed_data)
```

#time module
```
import time

# Get the current time
current_time = time.time()
print("Current Time:", current_time)

# Sleep for 2 seconds
time.sleep(2)
```

#datetime module
```python
import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)
```

#pathlib module
```
from pathlib import Path

# Get current working directory
current_directory = Path.cwd()
print("Current Directory:", current_directory)
```

#configparser module
```python
import configparser

# Read a configuration file
config = configparser.ConfigParser()
config.read('config.ini')
print(config['DEFAULT']['Server'])
```

#requests module (requires requests package)
```python
import requests

# Make a GET request
response = requests.get('https://api.github.com')
print(response.json())
```

#boto3 module (requires boto3 package)
```python
import boto3

# List S3 buckets
s3 = boto3.client('s3')
buckets = s3.list_buckets()
print(buckets)
```

#paramiko module (requires paramiko package)
```python
import paramiko

# Connect to an SSH server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('hostname', username='user', password='passwd')
```

#psutil module (requires psutil package)
```python
import psutil

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print("CPU Usage:", cpu_usage)
```

#socket module
```python
import socket

# Get the hostname
hostname = socket.gethostname()
print("Hostname:", hostname)
```

#logging module
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.info('This is an info message')
```

