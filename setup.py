from setuptools import setup, find_packages

setup(
    name="nl-compile",
    version="1.0.0",
    description="Natural Language Programming Interpreter",
    author="PI-Prasaad-Krishna",
    py_modules=["main", "lexer", "parser", "evaluator", "environment", "ast_nodes"],
    entry_points={
        'console_scripts': [
            'nl=main:main',
        ],
    },
    python_requires=">=3.7",
)
