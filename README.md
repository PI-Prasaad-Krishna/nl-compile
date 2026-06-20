# Natural Language Programming Language (NL)

**NL** is a dynamically typed, AST-based interpreted programming language built entirely in Python. The core philosophy of NL is to allow users to write executable code using conversational, natural English.

---

## Features

- **Conversational Syntax:** Write code that reads like a sentence.
- **Tree-Walking Interpreter:** Fully modular architecture with a custom Lexer, Parser, Environment, and Evaluator.
- **Interactive REPL:** Type code live and see immediate results.
- **Precise Error Tracking:** Beautifully formatted syntax errors that point to the exact line and column of your mistakes.
- **File Execution:** Write robust scripts in `.nl` files and run them seamlessly.

## Getting Started

### Prerequisites
- Python 3.x (No external libraries required!)

### Installation
Clone the repository and run the interpreter directly:

```bash
git clone <your-repo-url>
cd nl-lang
```

### Running the REPL
To start the interactive Read-Eval-Print Loop (REPL), simply run `main.py` without any arguments:

```bash
python main.py
```

### Executing a Script
To run a `.nl` file, pass the file path as an argument:

```bash
python main.py test.nl
```

## Syntax & Documentation

NL is designed to be read aloud. Below is the official syntax supported by the interpreter.

### 1. Variables
Variables are dynamically typed and can be created or updated using the `set` and `to` keywords. You can optionally use `create variable <name> and set it to <value>` for a more verbose sentence.

```text
create variable x and set it to 10
set y to 20
```

### 2. Mathematics and Arithmetic
Math is done using English words (`plus`, `minus`, `times`, `divided by`) rather than symbols (`+`, `-`, `*`, `/`). Standard order of operations (PEMDAS) applies automatically.

```text
set result to 5 times 10
set z to x plus y
```

### 3. Strings & Concatenation
Text is enclosed in quotes (`"..."`). You can combine strings together, or combine strings with variables, using the `plus` keyword.

```text
set greeting to "Hello " plus "World"
print greeting
```

### 4. Printing
To output a value to the terminal, simply use the `print` keyword.

```text
print "Execution completed!"
print x
```

### 5. Conditionals (If Statements)
NL supports boolean logic using conversational comparators:
- `is greater than`
- `is less than`
- `is equal to`

```text
set age to 18
if age is greater than 10 then print "You are old enough!"
```

### 6. Loops
You can execute any valid statement repeatedly using `loop till <number> and <statement>`. The loop will execute exactly `<number>` times.

```text
set count to 0
loop till 5 and set count to count plus 1
print count
```

### 7. Actions (Functions)
You can define reusable blocks of code called `actions`. Actions create their own local scope (memory environment) so their internal variables do not overwrite global variables.

**Defining an action:**
```text
define action greet with name and do print "Hello " plus name
```

**Running an action:**
```text
run greet with "Alice"
run greet with "Bob"
```

## Architecture

The interpreter is broken down into standard compiler components:
1. **`lexer.py`:** Tokenizes the English words and tracks exact line/column details.
2. **`ast_nodes.py`:** Defines the Abstract Syntax Tree (AST) structures.
3. **`parser.py`:** A Recursive Descent Parser that understands the English grammar.
4. **`environment.py`:** Manages dynamic variables in memory and lexical scoping.
5. **`evaluator.py`:** The execution engine that walks the AST.
6. **`main.py`:** The CLI and REPL tool.

---
*Built from scratch to prove that the next programming language is English.*
