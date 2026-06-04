Day 3 - Loops and Conditional Statements

Objective

Learn how to make decisions in Python programs and repeat tasks using loops.

---

Conditional Statements

Conditional statements allow a program to execute different code based on conditions.

if Statement

Executes a block of code when a condition is True.

age = 18

if age >= 18:
    print("Eligible to vote")

if-else Statement

Executes one block if the condition is True and another if it is False.

num = 5

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

if-elif-else Statement

Used when multiple conditions need to be checked.

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

---

Loops

Loops are used to execute a block of code repeatedly.

for Loop

Used when the number of iterations is known.

for i in range(1, 6):
    print(i)

Output:

1
2
3
4
5

while Loop

Used when the number of iterations is not known.

count = 1

while count <= 5:
    print(count)
    count += 1

Output:

1
2
3
4
5

---

range() Function

The range() function generates a sequence of numbers.

Examples:

range(5)

Output:

0, 1, 2, 3, 4

range(1, 6)

Output:

1, 2, 3, 4, 5

---

Nested Loops

A loop inside another loop is called a nested loop.

for i in range(1, 4):
    for j in range(i):
        print(i, end=" ")
    print()

Output:

1

2 2

3 3 3

---

Loop Control Statements

break

Terminates the loop immediately.

for i in range(1, 6):
    if i == 3:
        break
    print(i)

Output:

1
2

continue

Skips the current iteration and moves to the next iteration.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:

1
2
4
5

pass

Acts as a placeholder and does nothing.

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

Output:

1
2
3
4
5

