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


##Environment Variables
Environment variables are dynamic values that affect the way running processes behave on a computer. They can be used to configure the behavior of applications and scripts.

How to Set Environment Variables
Environment variables can be set in the operating system and accessed within your Python script.

**Setting Environment Variables (on Windows):**

```shell
set MY_VARIABLE=some_value
```


