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

### Global Installation (Recommended)
You can install NL globally on your machine using `pip`. This allows you to run the `nl` command anywhere!

```bash
pip install git+https://github.com/PI-Prasaad-Krishna/nl-compile.git
```

### Running the REPL
To start the interactive Read-Eval-Print Loop (REPL), simply type:

```bash
nl
```

### Executing a Script
To run a `.nl` file, pass the file path to the `nl` command:

```bash
nl script.nl
```

### Local Development Installation
If you want to modify the language source code, clone the repository and install it locally:

```bash
git clone https://github.com/PI-Prasaad-Krishna/nl-compile
cd nl-compile
pip install -e .
```

## Syntax & Documentation

NL is designed to be read aloud. The official syntax documentation has been moved to a dedicated, interactive website for a better reading experience!

### Viewing the Documentation
You can read the full, interactive documentation online here:
**[NL Webpage](https://nl-compile.vercel.app/)**

*(To run the documentation site locally, navigate to the `docs-site` directory and run `npm run dev`.)*

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
