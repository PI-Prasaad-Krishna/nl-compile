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

class WhileStmt(ASTNode):
    def __init__(self, condition_expr, body_stmt):
        self.condition_expr = condition_expr
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

class ReturnStmt(ASTNode):
    def __init__(self, expr):
        self.expr = expr

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

class LogicalOp(ASTNode):
    def __init__(self, left, op_str, right):
        self.left = left
        self.op_str = op_str # "and", "or"
        self.right = right

class ListCreateExpr(ASTNode):
    def __init__(self, items):
        self.items = items

class ListAccessExpr(ASTNode):
    def __init__(self, list_name, index_expr):
        self.list_name = list_name
        self.index_expr = index_expr

class ObjectCreateExpr(ASTNode):
    def __init__(self, pairs):
        self.pairs = pairs

class PropertyAccessExpr(ASTNode):
    def __init__(self, prop_expr, obj_name):
        self.prop_expr = prop_expr
        self.obj_name = obj_name

class FileReadExpr(ASTNode):
    def __init__(self, path_expr):
        self.path_expr = path_expr

class FileWriteStmt(ASTNode):
    def __init__(self, content_expr, path_expr):
        self.content_expr = content_expr
        self.path_expr = path_expr

class TryCatchStmt(ASTNode):
    def __init__(self, try_stmt, catch_stmt):
        self.try_stmt = try_stmt
        self.catch_stmt = catch_stmt

class NumberLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

class StringLiteral(ASTNode):
    def __init__(self, value):
        self.value = value

class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name

# Phase 5 Nodes
class LengthExpr(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class SplitExpr(ASTNode):
    def __init__(self, string_expr, delimiter_expr):
        self.string_expr = string_expr
        self.delimiter_expr = delimiter_expr

class CasingExpr(ASTNode):
    def __init__(self, op_str, expr):
        self.op_str = op_str # "uppercase" or "lowercase"
        self.expr = expr

class ReplaceExpr(ASTNode):
    def __init__(self, old_expr, new_expr, target_expr):
        self.old_expr = old_expr
        self.new_expr = new_expr
        self.target_expr = target_expr

class ListAddStmt(ASTNode):
    def __init__(self, item_expr, list_name):
        self.item_expr = item_expr
        self.list_name = list_name

class ListRemoveStmt(ASTNode):
    def __init__(self, index_expr, list_name):
        self.index_expr = index_expr
        self.list_name = list_name

class PropertyAssignStmt(ASTNode):
    def __init__(self, prop_expr, obj_name, val_expr):
        self.prop_expr = prop_expr
        self.obj_name = obj_name
        self.val_expr = val_expr

# Phase 6 Nodes
class FetchExpr(ASTNode):
    def __init__(self, url_expr):
        self.url_expr = url_expr

class CurrentTimeExpr(ASTNode):
    pass

class ExecuteExpr(ASTNode):
    def __init__(self, command_expr):
        self.command_expr = command_expr

class ConvertExpr(ASTNode):
    def __init__(self, expr, target_type):
        self.expr = expr
        self.target_type = target_type # "number" or "string"

class WaitStmt(ASTNode):
    def __init__(self, seconds_expr):
        self.seconds_expr = seconds_expr

class IncludeStmt(ASTNode):
    def __init__(self, path_expr):
        self.path_expr = path_expr

# Phase 7 Nodes
class ParseJsonExpr(ASTNode):
    def __init__(self, text_expr):
        self.text_expr = text_expr

class GetSecretExpr(ASTNode):
    def __init__(self, key_expr):
        self.key_expr = key_expr

class ShowAlertStmt(ASTNode):
    def __init__(self, message_expr):
        self.message_expr = message_expr

class PromptUserStmt(ASTNode):
    def __init__(self, message_expr, var_name):
        self.message_expr = message_expr
        self.var_name = var_name
