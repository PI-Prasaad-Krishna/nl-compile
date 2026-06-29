import ast_nodes
from lexer import TokenType

class ParserError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} at line {line}, column {column}")
        self.line = line
        self.column = column

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message):
        raise ParserError(message, self.current_token.line, self.current_token.column)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Expected {token_type.name}, got {self.current_token.type.name}")

    def skip_optional(self, token_type):
        if self.current_token.type == token_type:
            self.eat(token_type)
            return True
        return False

    def parse(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        return ast_nodes.Program(statements)

    def parse_body(self):
        if self.current_token.type == TokenType.DO:
            self.eat(TokenType.DO)
            statements = []
            while self.current_token.type not in (TokenType.END, TokenType.EOF):
                stmt = self.statement()
                if stmt:
                    statements.append(stmt)
            if self.current_token.type == TokenType.END:
                self.eat(TokenType.END)
            return ast_nodes.BlockStmt(statements)
        else:
            return self.statement()

    def statement(self):
        # "create variable x and set it to 10"
        # "create list colors containing 1, 2, 3"
        # "create object user containing 'name' as 'Alice' and 'age' as 25"
        if self.current_token.type == TokenType.CREATE:
            self.eat(TokenType.CREATE)
            
            if self.current_token.type == TokenType.LIST:
                self.eat(TokenType.LIST)
                list_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.eat(TokenType.CONTAINING)
                
                items = []
                items.append(self.expr())
                while self.current_token.type == TokenType.COMMA:
                    self.eat(TokenType.COMMA)
                    items.append(self.expr())
                return ast_nodes.VarAssign(list_name, ast_nodes.ListCreateExpr(items))
                
            elif self.current_token.type == TokenType.OBJECT:
                self.eat(TokenType.OBJECT)
                obj_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.eat(TokenType.CONTAINING)
                
                pairs = []
                key = self.expr()
                self.eat(TokenType.AS)
                val = self.expr()
                pairs.append((key, val))
                while self.current_token.type == TokenType.COMMA:
                    self.eat(TokenType.COMMA)
                    key = self.expr()
                    self.eat(TokenType.AS)
                    val = self.expr()
                    pairs.append((key, val))
                return ast_nodes.VarAssign(obj_name, ast_nodes.ObjectCreateExpr(pairs))
                
            else:
                self.skip_optional(TokenType.VARIABLE)
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.skip_optional(TokenType.AND)
                self.eat(TokenType.SET)
                
                if self.current_token.type == TokenType.IDENTIFIER and self.current_token.value == 'it':
                    self.eat(TokenType.IDENTIFIER)
                elif self.current_token.type == TokenType.IDENTIFIER and self.current_token.value == var_name:
                    self.eat(TokenType.IDENTIFIER)
                    
                self.eat(TokenType.TO)
                expr = self.expr()
                return ast_nodes.VarAssign(var_name, expr)

        # "set x to 10" or "set property 'age' of user to 26"
        if self.current_token.type == TokenType.SET:
            self.eat(TokenType.SET)
            
            if self.current_token.type == TokenType.PROPERTY:
                self.eat(TokenType.PROPERTY)
                prop_expr = self.expr()
                self.eat(TokenType.OF)
                obj_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.eat(TokenType.TO)
                val_expr = self.expr()
                return ast_nodes.PropertyAssignStmt(prop_expr, obj_name, val_expr)
            else:
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.eat(TokenType.TO)
                expr = self.expr()
                return ast_nodes.VarAssign(var_name, expr)

        # "add x to colors"
        if self.current_token.type == TokenType.ADD:
            self.eat(TokenType.ADD)
            item_expr = self.expr()
            self.eat(TokenType.TO)
            list_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return ast_nodes.ListAddStmt(item_expr, list_name)

        # "remove item 1 from colors"
        if self.current_token.type == TokenType.REMOVE:
            self.eat(TokenType.REMOVE)
            self.eat(TokenType.ITEM)
            index_expr = self.expr()
            self.eat(TokenType.FROM)
            list_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return ast_nodes.ListRemoveStmt(index_expr, list_name)

        # "ask 'name?' and set it to name"
        if self.current_token.type == TokenType.ASK:
            self.eat(TokenType.ASK)
            prompt_expr = self.expr()
            self.skip_optional(TokenType.AND)
            self.eat(TokenType.SET)
            if self.current_token.type == TokenType.IDENTIFIER and self.current_token.value == 'it':
                self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.TO)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return ast_nodes.AskStmt(prompt_expr, var_name)

        # "print x" or "print 'Hello' name"
        if self.current_token.type == TokenType.PRINT:
            self.eat(TokenType.PRINT)
            exprs = [self.expr()]
            while self.current_token.type in (TokenType.NUMBER, TokenType.STRING, TokenType.IDENTIFIER, TokenType.ITEM, TokenType.PROPERTY, TokenType.READ, TokenType.RUN, TokenType.LENGTH, TokenType.SPLIT, TokenType.UPPERCASE, TokenType.LOWERCASE, TokenType.REPLACE):
                exprs.append(self.expr())
            return ast_nodes.PrintStmt(exprs)

        # "write x into file y"
        if self.current_token.type == TokenType.WRITE:
            self.eat(TokenType.WRITE)
            content_expr = self.expr()
            self.eat(TokenType.INTO)
            self.eat(TokenType.FILE)
            path_expr = self.expr()
            return ast_nodes.FileWriteStmt(content_expr, path_expr)

        # "for each color in colors print color"
        if self.current_token.type == TokenType.FOR:
            self.eat(TokenType.FOR)
            self.eat(TokenType.EACH)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.IN)
            list_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            body_stmt = self.parse_body()
            return ast_nodes.ForEachStmt(var_name, list_name, body_stmt)

        # "while count is less than 10 do ... end"
        if self.current_token.type == TokenType.WHILE:
            self.eat(TokenType.WHILE)
            condition_expr = self.expr()
            body_stmt = self.parse_body()
            return ast_nodes.WhileStmt(condition_expr, body_stmt)

        # "loop till 5 and do ... end"
        if self.current_token.type == TokenType.LOOP:
            self.eat(TokenType.LOOP)
            self.eat(TokenType.TILL)
            limit_expr = self.expr()
            self.skip_optional(TokenType.AND)
            body_stmt = self.parse_body()
            return ast_nodes.LoopStmt(limit_expr, body_stmt)

        # "if x is greater than 10 then do ... end"
        if self.current_token.type == TokenType.IF:
            self.eat(TokenType.IF)
            condition_expr = self.expr()
            self.eat(TokenType.THEN)
            body_stmt = self.parse_body()
            return ast_nodes.IfStmt(condition_expr, body_stmt)

        # "try to do ... end but if it fails do ... end"
        if self.current_token.type == TokenType.TRY:
            self.eat(TokenType.TRY)
            self.skip_optional(TokenType.TO)
            try_stmt = self.parse_body()
            self.eat(TokenType.BUT)
            self.skip_optional(TokenType.IF)
            self.eat(TokenType.IT)
            self.eat(TokenType.FAILS)
            catch_stmt = self.parse_body()
            return ast_nodes.TryCatchStmt(try_stmt, catch_stmt)

        # "define action greet with name and do ... end"
        if self.current_token.type == TokenType.DEFINE:
            self.eat(TokenType.DEFINE)
            self.eat(TokenType.ACTION)
            func_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.WITH)
            param_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.skip_optional(TokenType.AND)
            body_stmt = self.parse_body()
            return ast_nodes.FuncDefStmt(func_name, param_name, body_stmt)

        # "return x"
        if self.current_token.type == TokenType.RETURN:
            self.eat(TokenType.RETURN)
            expr = self.expr()
            return ast_nodes.ReturnStmt(expr)

        # Backwards compatibility: "run greet with 'Alice'" as standalone statement
        if self.current_token.type == TokenType.RUN:
            self.eat(TokenType.RUN)
            func_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.WITH)
            arg_expr = self.expr()
            return ast_nodes.FuncCallStmt(func_name, arg_expr)

        self.error(f"Invalid statement starting with '{self.current_token.value}'")

    def expr(self):
        node = self.expr_compare()
        
        while self.current_token.type in (TokenType.AND, TokenType.OR):
            op = self.current_token.type
            self.eat(op)
            right = self.expr_compare()
            op_str = "and" if op == TokenType.AND else "or"
            node = ast_nodes.LogicalOp(node, op_str, right)
            
        return node

    def expr_compare(self):
        node = self.term()
        
        if self.current_token.type == TokenType.IS:
            self.eat(TokenType.IS)
            if self.current_token.type == TokenType.GREATER:
                self.eat(TokenType.GREATER)
                self.skip_optional(TokenType.THAN)
                right = self.term()
                return ast_nodes.CompareOp(node, "greater", right)
            elif self.current_token.type == TokenType.LESS:
                self.eat(TokenType.LESS)
                self.skip_optional(TokenType.THAN)
                right = self.term()
                return ast_nodes.CompareOp(node, "less", right)
            elif self.current_token.type == TokenType.EQUAL:
                self.eat(TokenType.EQUAL)
                self.skip_optional(TokenType.TO)
                right = self.term()
                return ast_nodes.CompareOp(node, "equal", right)
            else:
                self.error("Expected 'greater', 'less', or 'equal' after 'is'")
                
        elif self.current_token.type == TokenType.CONTAINS:
            self.eat(TokenType.CONTAINS)
            right = self.term()
            return ast_nodes.CompareOp(node, "contains", right)
            
        return node

    def term(self):
        node = self.factor()
        
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS, TokenType.TIMES, TokenType.DIVIDED):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            elif token.type == TokenType.TIMES:
                self.eat(TokenType.TIMES)
            elif token.type == TokenType.DIVIDED:
                self.eat(TokenType.DIVIDED)
                self.eat(TokenType.BY)
                
            right = self.factor()
            node = ast_nodes.BinOp(left=node, op=token, right=right)
            
        return node

    def factor(self):
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return ast_nodes.NumberLiteral(token.value)
        elif token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return ast_nodes.StringLiteral(token.value)
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            return ast_nodes.Identifier(token.value)
        elif token.type == TokenType.ITEM:
            # "item 1 of colors"
            self.eat(TokenType.ITEM)
            index_expr = self.expr()
            self.eat(TokenType.OF)
            list_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return ast_nodes.ListAccessExpr(list_name, index_expr)
        elif token.type == TokenType.PROPERTY:
            # "property 'name' of user"
            self.eat(TokenType.PROPERTY)
            prop_expr = self.expr()
            self.eat(TokenType.OF)
            obj_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return ast_nodes.PropertyAccessExpr(prop_expr, obj_name)
        elif token.type == TokenType.READ:
            # "read file 'data.txt'"
            self.eat(TokenType.READ)
            self.eat(TokenType.FILE)
            path_expr = self.expr()
            return ast_nodes.FileReadExpr(path_expr)
        elif token.type == TokenType.RUN:
            # "run calculate with 5"
            self.eat(TokenType.RUN)
            func_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.WITH)
            arg_expr = self.expr()
            return ast_nodes.FuncCallStmt(func_name, arg_expr)
        elif token.type == TokenType.LENGTH:
            # "length of x"
            self.eat(TokenType.LENGTH)
            self.eat(TokenType.OF)
            return ast_nodes.LengthExpr(self.expr())
        elif token.type == TokenType.SPLIT:
            # "split x by y"
            self.eat(TokenType.SPLIT)
            string_expr = self.expr()
            self.eat(TokenType.BY)
            delimiter_expr = self.expr()
            return ast_nodes.SplitExpr(string_expr, delimiter_expr)
        elif token.type == TokenType.UPPERCASE:
            self.eat(TokenType.UPPERCASE)
            return ast_nodes.CasingExpr("uppercase", self.expr())
        elif token.type == TokenType.LOWERCASE:
            self.eat(TokenType.LOWERCASE)
            return ast_nodes.CasingExpr("lowercase", self.expr())
        elif token.type == TokenType.REPLACE:
            # "replace 'bad' with 'good' in x"
            self.eat(TokenType.REPLACE)
            old_expr = self.expr()
            self.eat(TokenType.WITH)
            new_expr = self.expr()
            self.eat(TokenType.IN)
            target_expr = self.expr()
            return ast_nodes.ReplaceExpr(old_expr, new_expr, target_expr)
            
        self.error(f"Unexpected factor: '{token.value}'")
