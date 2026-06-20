class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class VarAssign(ASTNode):
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

class PrintStmt(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class LoopStmt(ASTNode):
    def __init__(self, limit_expr, body_stmt):
        self.limit_expr = limit_expr
        self.body_stmt = body_stmt

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumberLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

class StringLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name
