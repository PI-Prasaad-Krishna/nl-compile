import sys
from lexer import Lexer, LexerError
from parser import Parser, ParserError
from evaluator import Evaluator, EvaluatorError

def highlight_error(text, line, column):
    lines = text.split('\n')
    if 1 <= line <= len(lines):
        error_line = lines[line - 1]
        print(error_line)
        print(' ' * (column - 1) + '^')

def run(text, evaluator=None, is_repl=False):
    try:
        lexer = Lexer(text)
        parser = Parser(lexer)
        tree = parser.parse()
        
        if evaluator is None:
            evaluator = Evaluator(tree)
        else:
            evaluator.tree = tree
            
        result = evaluator.evaluate()
        
        if is_repl and result is not None and tree and len(tree.statements) == 1:
            stmt_type = type(tree.statements[-1]).__name__
            if stmt_type not in ('PrintStmt', 'VarAssign', 'PropertyAssignStmt', 'ListAddStmt', 'ListRemoveStmt', 'CreateObjectStmt', 'CreateListStmt', 'DefineTemplateStmt', 'CreateTemplatedObjectStmt', 'FileWriteStmt', 'BackgroundStmt', 'CreateFolderStmt', 'DeleteFileStmt'):
                print(result)
        
        return evaluator
    except LexerError as e:
        print(f"SyntaxError (Lexer): {e}")
        highlight_error(text, e.line, e.column)
    except ParserError as e:
        print(f"SyntaxError (Parser): {e}")
        highlight_error(text, e.line, e.column)
    except Exception as e:
        print(f"RuntimeError: {e}")

def main():
    if len(sys.argv) > 1:
        if sys.argv[1].endswith('.nl'):
            with open(sys.argv[1], 'r') as f:
                run(f.read())
        else:
            text = " ".join(sys.argv[1:])
            run(text)
    else:
        print("Natural Language Interpreter (REPL)")
        print("Type 'exit' to quit.")
        
        # Keep environment alive for REPL
        repl_evaluator = Evaluator(None)
        
        while True:
            try:
                text = input("nl> ")
                if text.lower() == 'exit':
                    break
                if text.strip():
                    run(text, repl_evaluator, is_repl=True)
            except EOFError:
                break
            except KeyboardInterrupt:
                print("\nType 'exit' to quit.")

if __name__ == '__main__':
    main()
