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

## Syntax & Examples

### Variables and Math
You can create variables and perform arithmetic operations using natural English words.

```text
create variable x and set it to 10
set y to 20
set z to x plus y
print z
```

### Loops
Loops allow you to execute any valid statement repeatedly.

```text
set count to 0
loop till 5 and set count to count plus 1
print count
```

## Architecture

The interpreter is broken down into standard compiler components:
1. **`lexer.py`:** Tokenizes the English words and tracks exact line/column details.
2. **`ast_nodes.py`:** Defines the Abstract Syntax Tree (AST) structures.
3. **`parser.py`:** A Recursive Descent Parser that understands the English grammar.
4. **`environment.py`:** Manages dynamic variables in memory.
5. **`evaluator.py`:** The execution engine that walks the AST.
6. **`main.py`:** The CLI and REPL tool.

---
*Built from scratch to prove that the next programming language is English.*
