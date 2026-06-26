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
        
        # Create a new local scope
        local_env = Environment(parent=self.env)
        local_env.set(func_node.param_name, arg_val)
        
        # Save old environment and inject new one
        old_env = self.env
        self.env = local_env
        
        # Execute body
        try:
            self.visit(func_node.body_stmt)
        finally:
            # Restore old environment
            self.env = old_env
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
        
        # 1-based indexing for natural language
        if idx < 1 or idx > len(lst):
            raise EvaluatorError(f"Index {idx} is out of bounds for list '{node.list_name}'")
            
        return lst[idx - 1]

    def visit_NumberLiteral(self, node):
        return node.value

    def visit_StringLiteral(self, node):
        return node.value

    def visit_Identifier(self, node):
        return self.env.get(node.name)
