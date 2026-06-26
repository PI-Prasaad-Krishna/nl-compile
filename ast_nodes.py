class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class BlockStmt(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class VarAssign(ASTNode):
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

class AskStmt(ASTNode):
    def __init__(self, prompt_expr, var_name):
        self.prompt_expr = prompt_expr
        self.var_name = var_name

class PrintStmt(ASTNode):
    def __init__(self, exprs):
        self.exprs = exprs

class LoopStmt(ASTNode):
    def __init__(self, limit_expr, body_stmt):
        self.limit_expr = limit_expr
        self.body_stmt = body_stmt

class ForEachStmt(ASTNode):
    def __init__(self, var_name, list_name, body_stmt):
        self.var_name = var_name
        self.list_name = list_name
        self.body_stmt = body_stmt

class IfStmt(ASTNode):
    def __init__(self, condition_expr, body_stmt):
        self.condition_expr = condition_expr
        self.body_stmt = body_stmt

class FuncDefStmt(ASTNode):
    def __init__(self, name, param_name, body_stmt):
        self.name = name
        self.param_name = param_name
        self.body_stmt = body_stmt

class FuncCallStmt(ASTNode):
    def __init__(self, name, arg_expr):
        self.name = name
        self.arg_expr = arg_expr

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class CompareOp(ASTNode):
    def __init__(self, left, op_str, right):
        self.left = left
        self.op_str = op_str # "greater", "less", "equal"
        self.right = right

class ListCreateExpr(ASTNode):
    def __init__(self, items):
        self.items = items

class ListAccessExpr(ASTNode):
    def __init__(self, list_name, index_expr):
        self.list_name = list_name
        self.index_expr = index_expr

class NumberLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

class StringLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name
