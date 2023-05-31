# Reassignment

Variables can also be reassigned to new values during the execution of your program. For instance:

```python
x = 5
x = x + 1  # The value of x is updated to 6
```
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

<!-- Comment about difference between single equals and double equals. -->

---
# Control Structures - Uses

Control structures help you create more dynamic and responsive programs. They allow you to handle different scenarios, handle user input, and automate repetitive tasks. By combining if statements and loops, you can create powerful algorithms and solve complex problems efficiently.

It's important to pay attention to the indentation in Python because it defines the blocks of code that belong together. Proper indentation ensures that the control structures work as expected.