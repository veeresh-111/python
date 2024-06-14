## Read the Json file and find the heighest slary of the employee

``` python
import json  # To read the JSON file

def find_highest_salary(file_path):
    # Open and read the file
    with open(file_path, 'r') as file:
        data = json.load(file)  # Turn the file content into a dictionary

    highest_salary = 0  # Start with the lowest possible salary
    highest_paid_employee = ""  # Start with no employee

    # Go through each employee and their salary
    for employee in data:
        salary = data[employee]  # Get the salary of this employee
        if salary > highest_salary:  # If this salary is higher than our current highest
            highest_salary = salary  # Update the highest salary
            highest_paid_employee = employee  # Update the name of the highest-paid employee

    return highest_paid_employee, highest_salary  # Return the name and salary of the highest-paid employee

# Example usage
file_path = 'salaries.json'  # Path to your JSON file
employee, salary = find_highest_salary(file_path)  # Find the highest-paid employee
print(f"The highest paid employee is {employee} with a salary of {salary}.")  # Print the result
```


Steps in Simple Terms:
Read the File:

We open a file that has the names and salaries of employees.
We read it and turn it into a format we can use (like a list).
Find the Highest Salary:

We start by thinking the highest salary is zero and we don't know who has it yet.
We look at each employee's salary one by one.
If we find someone with a higher salary than what we thought was the highest, we update our highest salary and remember their name.
Print the Result:

Finally, we print out the name of the employee who earns the most and how much they earn.
Example of the JSON File (salaries.json):

``` json
{
    "emp1": 50000,
    "emp2": 60000,
    "emp3": 55000
}
```

When you run the script, it will tell you who has the highest salary and how much it is.

Super Simple Explanation:
We open the file to see the list of employees and their salaries.
We check each salary to find out who gets paid the most.
We print the name and salary of the employee with the highest pay.
