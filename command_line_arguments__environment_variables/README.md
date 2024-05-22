# Command Line Arguments and Environment Variables

## Command Line Arguments

Command line arguments are parameters passed to a script at the time of execution from the command line interface. They allow you to provide input values to your script without hardcoding them.

How to Use Command Line Arguments
In Python, command line arguments are accessed using the sys module.

**Example:**

```python
import sys

# Access command line arguments
script_name = sys.argv[0]  # The name of the script
arg1 = sys.argv[1]  # The first argument
arg2 = sys.argv[2]  # The second argument

print(f"Script Name: {script_name}")
print(f"First Argument: {arg1}")
print(f"Second Argument: {arg2}")

```

**Running the Script:**
```python
python script.py Hello World
```

**Output:**

```python
Script Name: script.py
First Argument: Hello
Second Argument: World
```




## Environment Variables

Environment variables are dynamic values that affect the way running processes behave on a computer. They can be used to configure the behavior of applications and scripts.

How to Set Environment Variables
Environment variables can be set in the operating system and accessed within your Python script.

**Setting Environment Variables (on Windows):**

```shell
set MY_VARIABLE=some_value
```

**Setting Environment Variables (on macOS/Linux):**

```shell
export MY_VARIABLE=some_value
```

Accessing Environment Variables in Python
Use the os module to access environment variables.

**Example:**

```python

import os

# Access an environment variable
my_var = os.getenv('MY_VARIABLE', 'default_value')

print(f"MY_VARIABLE: {my_var}")
```

  Note: The getenv method takes two arguments: the name of the environment variable and an optional default value if the environment variable is not found.


## dotenv Module

The dotenv module in Python is used to manage environment variables from a .env file. This is especially useful for managing configuration settings and secrets (like API keys) in a project.

Why Use dotenv?
 Security: Keeps sensitive information out of your codebase.
 Convenience: Makes it easy to manage environment-specific configurations.
 Portability: Simplifies the setup of different environments (development, testing, production).


Installing dotenv
To use the dotenv module, you need to install the python-dotenv package.

```shell
pip install python-dotenv
```

Create a .env file:

Create a file named .env in the root directory of your project and add your environment variables to it.

Example .env file:

```make
DATABASE_URL=postgres://user:password@localhost/dbname
SECRET_KEY=supersecretkey
DEBUG=True
```
