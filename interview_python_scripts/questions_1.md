##   Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz

```py
def fizz_buzz():
    for num in range(1, 101):  # Loop from 1 to 100 inclusive
        if num % 3 == 0 and num % 5 == 0:  # Check if the number is a multiple of both 3 and 5
            print("FizzBuzz")
        elif num % 3 == 0:  # Check if the number is a multiple of 3
            print("Fizz")
        elif num % 5 == 0:  # Check if the number is a multiple of 5
            print("Buzz")
        else:
            print(num)  # Print the number itself if none of the above conditions are met

# Call the function to see the output
fizz_buzz()

```
