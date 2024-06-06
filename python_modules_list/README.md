
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

# shutil module
```python
import shutil

# Copy a file
shutil.copy('source.txt', 'destination.txt')
```

# json module
```python
import json

# Parse JSON data
data = '{"name": "John", "age": 30}'
parsed_data = json.loads(data)
print(parsed_data)
```

# yaml module (requires pyyaml package)
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

# time module
```
import time

# Get the current time
current_time = time.time()
print("Current Time:", current_time)

# Sleep for 2 seconds
time.sleep(2)
```

# datetime module
```python
import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)
```

# pathlib module
```
from pathlib import Path

# Get current working directory
current_directory = Path.cwd()
print("Current Directory:", current_directory)
```

# configparser module
```python
import configparser

# Read a configuration file
config = configparser.ConfigParser()
config.read('config.ini')
print(config['DEFAULT']['Server'])
```

# requests module (requires requests package)
```python
import requests

# Make a GET request
response = requests.get('https://api.github.com')
print(response.json())
```

# boto3 module (requires boto3 package)
```python
import boto3

# List S3 buckets
s3 = boto3.client('s3')
buckets = s3.list_buckets()
print(buckets)
```

# paramiko module (requires paramiko package)
```python
import paramiko

# Connect to an SSH server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('hostname', username='user', password='passwd')
```

# psutil module (requires psutil package)
```python
import psutil

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print("CPU Usage:", cpu_usage)
```

# socket module
```python
import socket

# Get the hostname
hostname = socket.gethostname()
print("Hostname:", hostname)
```

# logging module
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.info('This is an info message')
```

# tarfile module
```python
import tarfile

# Create a tarball
with tarfile.open('archive.tar.gz', 'w:gz') as tar:
    tar.add('file.txt')
```

# zipfile module
```python
import zipfile

# Create a zip file
with zipfile.ZipFile('archive.zip', 'w') as zip:
    zip.write('file.txt')
```

# fnmatch module
```python
import fnmatch
import os

# Find files matching a pattern
files = fnmatch.filter(os.listdir('.'), '*.txt')
print(files)
```

# glob module
```
import glob

# Find files matching a pattern
files = glob.glob('*.txt')
print(files)
```

# hashlib module
```python
import hashlib

# Generate a hash
hash_object = hashlib.sha256(b'Hello World')
print(hash_object.hexdigest())
```

# uuid module
```
import uuid

# Generate a UUID
unique_id = uuid.uuid4()
print(unique_id)
```

# base64 module
```
import base64

# Encode data to base64
encoded = base64.b64encode(b'Hello World')
print(encoded)
```

# argparse module
```python
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Sample script')
parser.add_argument('filename', type=str, help='Filename')
args = parser.parse_args()
print(args.filename)
```

# multiprocessing module
```python
from multiprocessing import Process

def worker():
    print('Worker')

# Create and start a process
process = Process(target=worker)
process.start()
process.join()
```

# threading module
```python
import threading

def worker():
    print('Worker')

# Create and start a thread
thread = threading.Thread(target=worker)
thread.start()
thread.join()
```

# queue module
``` python
import queue

# Create a queue
q = queue.Queue()
q.put('item')
print(q.get())
```

# http.server module
```python
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Create a simple HTTP server
server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
print('Starting server...')
server.serve_forever()
```
# smtplib module
```python
import smtplib
from email.mime.text import MIMEText

# Send an email
msg = MIMEText('This is a test email')
msg['Subject'] = 'Test'
msg['From'] = 'from@example.com'
msg['To'] = 'to@example.com'

server = smtplib.SMTP('smtp.example.com')
server.send_message(msg)
server.quit()
```

# imaplib module
```python
import imaplib

# Connect to an IMAP server
mail = imaplib.IMAP4_SSL('imap.example.com')
mail.login('user@example.com', 'password')
mail.list()
mail.select('inbox')
```

# ftplib module
```python
from ftplib import FTP

# Connect to an FTP server
ftp = FTP('ftp.example.com')
ftp.login('user', 'password')
ftp.retrlines('LIST')
ftp.quit()
```

# ssl module
```python
import ssl

# Create an SSL context
context = ssl.create_default_context()
```

# pprint module
```python
import pprint

# Pretty-print a data structure
data = {'name': 'John', 'age': 30}
pprint.pprint(data)
```

# pickle module
```python
import pickle

# Serialize an object
data = {'name': 'John', 'age': 30}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
```

# csv module
```python
import csv

# Read a CSV file
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```

# sqlite3 module
```python
import sqlite3

# Create a database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
conn.commit()
conn.close()
```

# requests module for REST API (requires requests package)
```python
import requests

# Make a GET request to a REST API
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.json())

```
# docker module (requires docker package)
``` python
import docker

# Connect to Docker
client = docker.from_env()
for container in client.containers.list():
    print(container.name)
```

# kubernetes module (requires kubernetes package)
```
from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()
v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
for pod in v1.list_pod_for_all_namespaces(watch=False).items:
    print("%s\t%s" % (pod.status.pod_ip, pod.metadata.name))
```

# jinja2 module (requires jinja2 package)
```
from jinja2 import Template

# Render a template
template = Template('Hello {{ name }}!')
output = template.render(name='John')
print(output)
```

# dnspython module (requires dnspython package)
```
import dns.resolver

# Resolve a DNS query
result = dns.resolver.query('example.com', 'A')
for ipval in result:
    print('IP', ipval.to_text())
```

# paramiko module for SFTP (requires paramiko package)
```
import paramiko

# Connect to an SFTP server
transport = paramiko.Transport(('hostname', 22))
transport.connect(username='user', password='passwd')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get('remote_path', 'local_path')
sftp.put('local_path', 'remote_path')
sftp.close()
transport.close()
```

# watchdog module (requires watchdog package)
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'Event type: {event.event_type}  Path: {event.src_path}')

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

# selenium module (requires selenium package)
```python
from selenium import webdriver

# Open a web browser and navigate to a URL
driver = webdriver.Chrome()
driver.get('http://www.python.org')
print(driver.title)
driver.quit()
```

# pexpect module (requires pexpect package)
```python
import pexpect

# Automate interactive applications
child = pexpect.spawn('ssh user@hostname')
child.expect('password:')
child.sendline('passwd')
child.expect('$')
child.sendline('ls')
child.expect('$')
print(child.before.decode())
child.sendline('exit')
```

# urllib module
``` python
import urllib.request

# Fetch data from a URL
response = urllib.request.urlopen('http://www.python.org')
html = response.read()
print(html)
```


# flask module (requires flask package)
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
```

# pandas module (requires pandas package)
``` python
import pandas as pd

# Read a CSV file into a DataFrame
df = pd.read_csv('data.csv')
print(df.head())
```

# numpy module (requires numpy package)
``` python
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```


