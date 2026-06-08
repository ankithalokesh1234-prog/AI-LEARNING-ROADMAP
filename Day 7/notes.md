# Day 7 - File Handling in Python

## File Handling
File handling is used to create, read, write, and modify files.

## Opening a File
The open() function is used to open a file.

Example:
file = open("sample.txt", "r")

## Reading a File
Used to read the contents of a file.

Methods:
- read()
- readline()
- readlines()

Example:
file.read()

## Writing to a File
Used to write data into a file.

Mode:
- w (Write)

Example:
file.write("Hello World")

## Appending to a File
Used to add data at the end of a file.

Mode:
- a (Append)

Example:
file.write("New Data")

## Closing a File
A file should be closed after use.

Example:
file.close()

## File Modes

r  - Read
w  - Write
a  - Append
x  - Create

## Benefits of File Handling
- Stores data permanently
- Helps manage records
- Useful in real-world applications
- Easy data storage and retrieval
