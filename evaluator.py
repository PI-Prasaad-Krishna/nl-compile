import ast_nodes
from lexer import TokenType
from environment import Environment

class EvaluatorError(Exception):
    pass

class Evaluator:
    def __init__(self, tree):
        self.tree = tree
        self.env = Environment()

    def evaluate(self):
        if self.tree is None:
            return
        return self.visit(self.tree)

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise EvaluatorError(f"No visit_{type(node).__name__} method")

    def visit_Program(self, node):
        result = None
        for stmt in node.statements:
            result = self.visit(stmt)
        return result

    def visit_VarAssign(self, node):
        value = self.visit(node.expr)
        self.env.set(node.var_name, value)
        return value

    def visit_PrintStmt(self, node):
        value = self.visit(node.expr)
        print(value)
        return value

    def visit_LoopStmt(self, node):
        limit = self.visit(node.limit_expr)
        if not isinstance(limit, int):
            raise EvaluatorError("Loop limit must be an integer")
        for i in range(limit):
            self.visit(node.body_stmt)
        return None

    def visit_BinOp(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        
        if node.op.type == TokenType.PLUS:
            return left_val + right_val
        elif node.op.type == TokenType.MINUS:
            return left_val - right_val
        elif node.op.type == TokenType.TIMES:
            return left_val * right_val
        elif node.op.type == TokenType.DIVIDED:
            if right_val == 0:
                raise EvaluatorError("Division by zero")
            return left_val / right_val
            
        raise EvaluatorError(f"Unsupported operation: {node.op.type}")

    def visit_NumberLiteral(self, node):
        return node.value

    def visit_StringLiteral(self, node):
        return node.value

    def visit_Identifier(self, node):
        return self.env.get(node.name)
