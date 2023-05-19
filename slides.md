# Python for Beginners

Course notes: 

---
# Intro

What's covered:
+ Variables
+ Data types
+ Operations
+ Control structures - loops, if statements

What's not covered:
+ Installation
+ Testing
+ Version Control
+ Code Hygiene

<!-- I understand that you may not be fully committed to using Python in your projects at the moment, and that's perfectly fine. The good news is that you don't need to install anything to get started with Python. If you *do* go ahead with using Python, I can help you with getting set up and moving on to the more advanced things you may want to do with it. -->

---
# What is Python?

+ popular and beginner-friendly programming language
+ simple and readable syntax, resembles **psuedo-code**
<!-- In programming, syntax refers to the set of rules and guidelines that define the structure and composition of valid code in a programming language. It determines how statements, expressions, and instructions should be written to create meaningful and executable programs. -->
+ general-purpose, can be used for a variety of applications from web development to data visualitation to generative art

---
# Why Use Python for Art?

Python offers several advantages for beginners coming from an Arts background:

+ Easy to learn

<!-- Python has a simple and intuitive syntax that is easy to grasp, even for those without a programming background. It focuses on readability and provides  a gentle learning curve, allowing beginners to quickly start writing functional code. -->

+ Expressive and versatile

<!-- Python is a versatile language that can be used for a wide range of applications. It has extensive libraries and frameworks for data visualization, image processing, multimedia, and more. This versatility allows artists to explore creative possibilities and express their ideas using code. -->

+ Interactive development

<!-- Python supports interactive development environments like Jupyter Notebook and IPython, which allow for immediate feedback and experimentation. This interactivity is beneficial for artists who want to explore visualizations, generate art, or experiment with algorithms in real-time. -->

+ Rich ecosystem

<!-- Python has a vast ecosystem of libraries and packages that cater to various domains. Artists can leverage libraries like NumPy for numerical computing, Matplotlib for data visualization, Pillow for image manipulation, and Pygame for creating interactive games and multimedia experiences. This broad range of tools empowers artists to bring their creative visions to life. -->

+ Community and resources

<!-- Python has a large and supportive community of developers, including artists and creatives. There are dedicated forums, tutorials, and online communities where beginners can seek help, share their work, and collaborate with others. The availability of resources makes it easier for artists to learn and grow their skills. -->

+ Integration with other software

<!-- Python can be seamlessly integrated with other software tools commonly used in the Arts field, such as graphic design software, video editing tools, and 3D modeling applications. Python's flexibility allows artists to automate tasks, process data, and create custom workflows that bridge different software platforms. -->

+ Job opportunities

<!--  Learning Python opens up a wide range of job opportunities in fields like data visualization, game development, multimedia production, and web development. The ability to combine artistic skills with programming knowledge can be highly valuable in creative industries that require technical expertise. -->

<!-- Python's simplicity, versatility, and vibrant community make it an excellent choice for beginners from an Arts background. It provides a powerful and accessible platform for artistic expression, experimentation, and collaboration, enabling artists to leverage the potential of programming in their creative pursuits. -->

---
# Examples

Examples of cool ways Python has been used.

---
# Variables

In Python, variables are containers that allow you to store and manipulate data. Think of them as labeled boxes that hold different types of information, such as numbers, text, or even complex data structures.

To create a variable, you simply choose a name for it and assign a value using the equals sign (=). For example, you can create a variable called "message" and assign it the value "Hello, World!":

```python
message = "Hello, World!"
print(message)
```
---
# Variables - Continued

You can then use the variable in your code by referencing its name. Variables are useful because they allow you to reuse and update values without having to repeat the actual data.

Variables can hold different types of data, including integers (whole numbers), floating-point numbers (numbers with decimals), strings (text), booleans (True or False), and more. Python is a dynamically typed language, meaning you don't need to explicitly declare the type of a variable. Python will automatically determine the type based on the assigned value.

---
# Data Types



---
# Operations

You can perform operations on variables, such as mathematical calculations, combining strings, or comparisons. For example:

```python
x = 5
y = 3
summed = x + y  # Adds the values of x and y
greeting = "Hello, " + "World!"  # Combines two strings
is_greater = x > y  # Checks if x is greater than y
```
---
# Reassignment

Variables can also be reassigned to new values during the execution of your program. For instance:

```python
x = 5
x = x + 1  # The value of x is updated to 6
```

Remember, variable names should be descriptive and follow certain naming conventions. They cannot start with a number or contain spaces or special characters (except underscores).

By using variables, you can make your code more flexible, readable, and easier to maintain. They play a fundamental role in programming, allowing you to store and manipulate data in a dynamic and efficient manner.

---
# Control Structures

Control structures in Python are essential tools that allow you to make decisions and control the flow of your code. They determine which parts of your program are executed based on certain conditions.

The most common control structures in Python are **if statements** and **loops**. 

---
# If Statements

**If statements** let you check conditions and execute different blocks of code depending on whether the condition is true or false. For example, you can write an if statement to check if a number is greater than 10 and perform specific actions accordingly.

```python
steps_taken = 8000
target_steps = 10000
steps_remaining = target_steps - steps_taken

if steps_remaining > 0:
    print("You need to take " + str(steps_remaining) + " more steps to reach today's target.")
else:
    print("You reached today's target steps.")
```
---
# Loops

**Loops** allow you to repeat a block of code multiple times. The two main types of loops in Python are **for loops** and **while loops**. 

---
# For Loops

**For loops** are used to iterate over a sequence of elements, such as a list or a string. They execute a block of code for each item in the sequence. For example, you can use a for loop to process each element in a list.

```python
for i in range(10):
    print(i)
```
---
# While Loops

**While loops** continue executing a block of code as long as a condition remains true. They are useful when you want to repeat an action until a specific condition is met. For example, you can use a while loop to keep asking a user for input until they provide a valid response.

```python
name = ""  # Initialise an empty string

while name == "":  # Keep looping while the name is empty
    name = input("Please enter your name: ")  # Ask for user input

print("Hello,", name + "!")  # Print a greeting with the entered name
```
---
# Control Structures - Uses

Control structures help you create more dynamic and responsive programs. They allow you to handle different scenarios, handle user input, and automate repetitive tasks. By combining if statements and loops, you can create powerful algorithms and solve complex problems efficiently.

It's important to pay attention to the indentation in Python because it defines the blocks of code that belong together. Proper indentation ensures that the control structures work as expected.

---
# Functions
---
# Errors (Advanced)

When programming in Python, encountering errors is a normal part of the learning process. Understanding these errors and being able to interpret their output is crucial for debugging and improving your code.

<!-- Error Types: Python errors can fall into different categories, such as SyntaxErrors, which occur when you violate the rules of the Python syntax, and Exceptions, which happen during runtime when an unexpected situation arises.

Error Messages: When an error occurs, Python provides an error message that gives you information about what went wrong. It typically includes the error type, a brief description of the issue, and a traceback, which shows the sequence of function calls leading to the error.

Error Locations: The traceback displays the line number and the file where the error occurred. By examining the code at that line and the surrounding context, you can identify potential causes.

Error Descriptions: The error message often provides additional details about the specific error. It might highlight a specific line of code or provide hints about the underlying issue. Reading and understanding these descriptions can guide you towards finding a solution.

Error Handling: Python allows you to handle errors using try-except blocks. By placing potentially problematic code inside a try block and providing an appropriate except block, you can catch and handle errors gracefully. This way, you can display custom error messages, take alternative actions, or log error information for future reference.

Common Errors: As a beginner, you might encounter some common errors. Examples include NameError (using an undefined variable), TypeError (incompatible data types), and IndexError (accessing a list element outside its range). Familiarizing yourself with these common errors can help you recognize them and find solutions more quickly.

Google and Stack Overflow: When faced with an error, search engines like Google and programming forums like Stack Overflow can be valuable resources. By searching for the error message or a specific symptom, you can often find explanations, solutions, or similar cases that others have encountered. -->

Remember, learning to interpret Python errors is a skill that develops over time. Embrace errors as learning opportunities and use them to understand your code better. Read the error messages carefully, examine the traceback, and consider the context of your code. With practice, you'll become more adept at identifying and resolving errors, making your coding journey smoother.

---
# Investigating an Error (Advanced)

<!-- Explain None? -->
<!-- Explain continue/break? -->

# Recap

Review what has been covered up to this point.

# Further Reading

Resources for learning Python and doing stuff with it.