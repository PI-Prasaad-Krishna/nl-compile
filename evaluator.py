import ast_nodes
from lexer import TokenType
from environment import Environment

class EvaluatorError(Exception):
    pass

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

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

    def visit_BlockStmt(self, node):
        result = None
        for stmt in node.statements:
            result = self.visit(stmt)
        return result

    def visit_VarAssign(self, node):
        value = self.visit(node.expr)
        self.env.set(node.var_name, value)
        return value

    def visit_AskStmt(self, node):
        prompt = self.visit(node.prompt_expr)
        user_input = input(str(prompt))
        
        try:
            if '.' in user_input:
                val = float(user_input)
            else:
                val = int(user_input)
        except ValueError:
            val = user_input
            
        self.env.set(node.var_name, val)
        return val

    def visit_PrintStmt(self, node):
        values = [str(self.visit(e)) for e in node.exprs]
        output = " ".join(values)
        print(output)
        return output

    def visit_ForEachStmt(self, node):
        lst = self.env.get(node.list_name)
        if not isinstance(lst, list):
            raise EvaluatorError(f"'{node.list_name}' is not a list")
            
        for item in lst:
            self.env.set(node.var_name, item)
            self.visit(node.body_stmt)
        return None

    def visit_LoopStmt(self, node):
        limit = self.visit(node.limit_expr)
        if not isinstance(limit, int):
            raise EvaluatorError("Loop limit must be an integer")
        for i in range(limit):
            self.visit(node.body_stmt)
        return None

    def visit_WhileStmt(self, node):
        while self.visit(node.condition_expr):
            self.visit(node.body_stmt)
        return None

    def visit_IfStmt(self, node):
        condition = self.visit(node.condition_expr)
        if condition:
            self.visit(node.body_stmt)
        return None

    def visit_FuncDefStmt(self, node):
        self.env.set(node.name, node)
        return None

    def visit_FuncCallStmt(self, node):
        func_node = self.env.get(node.name)
        if not isinstance(func_node, ast_nodes.FuncDefStmt):
            raise EvaluatorError(f"'{node.name}' is not a valid action to run")
            
        arg_val = self.visit(node.arg_expr)
        
        local_env = Environment(parent=self.env)
        local_env.set(func_node.param_name, arg_val)
        
        old_env = self.env
        self.env = local_env
        
        try:
            self.visit(func_node.body_stmt)
        except ReturnException as e:
            return e.value
        finally:
            self.env = old_env
        return None

    def visit_ReturnStmt(self, node):
        val = self.visit(node.expr)
        raise ReturnException(val)

    def visit_TryCatchStmt(self, node):
        try:
            self.visit(node.try_stmt)
        except ReturnException as e:
            raise e
        except Exception:
            self.visit(node.catch_stmt)
        return None

    def visit_CompareOp(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        
        if node.op_str == "greater":
            return left_val > right_val
        elif node.op_str == "less":
            return left_val < right_val
        elif node.op_str == "equal":
            return left_val == right_val
        raise EvaluatorError(f"Unknown comparison: {node.op_str}")

    def visit_LogicalOp(self, node):
        left_val = self.visit(node.left)
        if node.op_str == "and":
            if not left_val:
                return False
            return bool(self.visit(node.right))
        elif node.op_str == "or":
            if left_val:
                return True
            return bool(self.visit(node.right))
        raise EvaluatorError(f"Unknown logic operator: {node.op_str}")

    def visit_BinOp(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        
        if node.op.type == TokenType.PLUS:
            if isinstance(left_val, str) or isinstance(right_val, str):
                return str(left_val) + str(right_val)
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

    def visit_ListCreateExpr(self, node):
        return [self.visit(item) for item in node.items]

    def visit_ListAccessExpr(self, node):
        lst = self.env.get(node.list_name)
        if not isinstance(lst, list):
            raise EvaluatorError(f"'{node.list_name}' is not a list")
        idx = self.visit(node.index_expr)
        if not isinstance(idx, int):
            raise EvaluatorError("List index must be an integer")
        
        if idx < 1 or idx > len(lst):
            raise EvaluatorError(f"Index {idx} is out of bounds for list '{node.list_name}'")
            
        return lst[idx - 1]

    def visit_ObjectCreateExpr(self, node):
        obj = {}
        for key_expr, val_expr in node.pairs:
            key = self.visit(key_expr)
            val = self.visit(val_expr)
            obj[key] = val
        return obj

    def visit_PropertyAccessExpr(self, node):
        obj = self.env.get(node.obj_name)
        if not isinstance(obj, dict):
            raise EvaluatorError(f"'{node.obj_name}' is not an object")
        key = self.visit(node.prop_expr)
        if key not in obj:
            raise EvaluatorError(f"Property '{key}' not found in object '{node.obj_name}'")
        return obj[key]

    def visit_FileReadExpr(self, node):
        path = self.visit(node.path_expr)
        try:
            with open(path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            raise EvaluatorError(f"File not found: {path}")

    def visit_FileWriteStmt(self, node):
        content = self.visit(node.content_expr)
        path = self.visit(node.path_expr)
        with open(path, 'w') as f:
            f.write(str(content))
        return None

    def visit_NumberLiteral(self, node):
        return node.value

    def visit_StringLiteral(self, node):
        return node.value

    def visit_Identifier(self, node):
        return self.env.get(node.name)
