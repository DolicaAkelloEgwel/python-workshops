---
title:
- Python for Beginnenrs
author:
- Dolica Akello-Egwel (doh-lih-kah)
---

# Intro

# What is Python?

# Why Use Python to Create Art?

# Examples

# Variables

In Python, variables are containers that allow you to store and manipulate data. Think of them as labeled boxes that hold different types of information, such as numbers, text, or even complex data structures.

To create a variable, you simply choose a name for it and assign a value using the equals sign (=). For example, you can create a variable called "message" and assign it the value "Hello, World!":

```python
message = "Hello, World!"
```

You can then use the variable in your code by referencing its name. Variables are useful because they allow you to reuse and update values without having to repeat the actual data.

Variables can hold different types of data, including integers (whole numbers), floating-point numbers (numbers with decimals), strings (text), booleans (True or False), and more. Python is a dynamically typed language, meaning you don't need to explicitly declare the type of a variable. Python will automatically determine the type based on the assigned value.

## Operations

You can perform operations on variables, such as mathematical calculations, concatenation of strings, or comparisons. For example:

```python
x = 5
y = 3
summed = x + y  # Adds the values of x and y
greeting = "Hello, " + "World!"  # Concatenates two strings
is_greater = x > y  # Checks if x is greater than y
```

## Reassignment

Variables can also be reassigned to new values during the execution of your program. For instance:

```python
x = 5
x = x + 1  # The value of x is updated to 6
```

Remember, variable names should be descriptive and follow certain naming conventions. They cannot start with a number or contain spaces or special characters (except underscores).

By using variables, you can make your code more flexible, readable, and easier to maintain. They play a fundamental role in programming, allowing you to store and manipulate data in a dynamic and efficient manner.

# Control Structures

Control structures in Python are essential tools that allow you to make decisions and control the flow of your code. They determine which parts of your program are executed based on certain conditions.

The most common control structures in Python are **if statements** and **loops**. 

## If-statements

**If statements** let you check conditions and execute different blocks of code depending on whether the condition is true or false. For example, you can write an if statement to check if a number is greater than 10 and perform specific actions accordingly.

```python
steps_taken = 8000
target_steps = 10000

if steps_taken < target_steps:
    pass
else:
    pass
```

## Loops

**Loops** allow you to repeat a block of code multiple times. The two main types of loops in Python are **for loops** and **while loops**. 

**For loops** are used to iterate over a sequence of elements, such as a list or a string. They execute a block of code for each item in the sequence. For example, you can use a for loop to process each element in a list.

```python
for i in range(10):
    print(i)
```

**While loops** continue executing a block of code as long as a condition remains true. They are useful when you want to repeat an action until a specific condition is met. For example, you can use a while loop to keep asking a user for input until they provide a valid response.

```python
name = ""  # Initialise an empty string

while name == "":  # Keep looping while the name is empty
    name = input("Please enter your name: ")  # Ask for user input

print("Hello,", name + "!")  # Print a greeting with the entered name
```

Control structures help you create more dynamic and responsive programs. They allow you to handle different scenarios, handle user input, and automate repetitive tasks. By combining if statements and loops, you can create powerful algorithms and solve complex problems efficiently.

It's important to pay attention to the indentation in Python because it defines the blocks of code that belong together. Proper indentation ensures that the control structures work as expected.

# Functions and Modules

# Errors (Advanced)

When programming in Python, encountering errors is a normal part of the learning process. Understanding these errors and being able to interpret their output is crucial for debugging and improving your code. Here's some information to help you make sense of Python errors:

Error Types: Python errors can fall into different categories, such as SyntaxErrors, which occur when you violate the rules of the Python syntax, and Exceptions, which happen during runtime when an unexpected situation arises.

Error Messages: When an error occurs, Python provides an error message that gives you information about what went wrong. It typically includes the error type, a brief description of the issue, and a traceback, which shows the sequence of function calls leading to the error.

Error Locations: The traceback displays the line number and the file where the error occurred. By examining the code at that line and the surrounding context, you can identify potential causes.

Error Descriptions: The error message often provides additional details about the specific error. It might highlight a specific line of code or provide hints about the underlying issue. Reading and understanding these descriptions can guide you towards finding a solution.

Error Handling: Python allows you to handle errors using try-except blocks. By placing potentially problematic code inside a try block and providing an appropriate except block, you can catch and handle errors gracefully. This way, you can display custom error messages, take alternative actions, or log error information for future reference.

Common Errors: As a beginner, you might encounter some common errors. Examples include NameError (using an undefined variable), TypeError (incompatible data types), and IndexError (accessing a list element outside its range). Familiarizing yourself with these common errors can help you recognize them and find solutions more quickly.

Google and Stack Overflow: When faced with an error, search engines like Google and programming forums like Stack Overflow can be valuable resources. By searching for the error message or a specific symptom, you can often find explanations, solutions, or similar cases that others have encountered.

Remember, learning to interpret Python errors is a skill that develops over time. Embrace errors as learning opportunities and use them to understand your code better. Read the error messages carefully, examine the traceback, and consider the context of your code. With practice, you'll become more adept at identifying and resolving errors, making your coding journey smoother.

## Investigating an Error (Advanced)