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

    def parse(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            stmt = self.statement()
            if stmt:
                statements.append(stmt)
        return ast_nodes.Program(statements)

    def statement(self):
        # "create variable x and set it to 10"
        if self.current_token.type == TokenType.CREATE:
            self.eat(TokenType.CREATE)
            self.skip_optional(TokenType.VARIABLE)
            if self.current_token.type == TokenType.IDENTIFIER:
                var_name = self.current_token.value
                self.eat(TokenType.IDENTIFIER)
                self.skip_optional(TokenType.AND)
                self.eat(TokenType.SET)
                
                # Check for "it" or the variable name again
                if self.current_token.type == TokenType.IDENTIFIER and self.current_token.value == 'it':
                    self.eat(TokenType.IDENTIFIER)
                elif self.current_token.type == TokenType.IDENTIFIER and self.current_token.value == var_name:
                    self.eat(TokenType.IDENTIFIER)
                    
                self.eat(TokenType.TO)
                expr = self.expr()
                return ast_nodes.VarAssign(var_name, expr)

        # "set x to 10"
        if self.current_token.type == TokenType.SET:
            self.eat(TokenType.SET)
            var_name = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            self.eat(TokenType.TO)
            expr = self.expr()
            return ast_nodes.VarAssign(var_name, expr)

        # "print x"
        if self.current_token.type == TokenType.PRINT:
            self.eat(TokenType.PRINT)
            expr = self.expr()
            return ast_nodes.PrintStmt(expr)

        # "loop till 10 and print x" or "loop till 5 and set z to 10"
        if self.current_token.type == TokenType.LOOP:
            self.eat(TokenType.LOOP)
            self.eat(TokenType.TILL)
            limit_expr = self.expr()
            self.skip_optional(TokenType.AND)
            
            # The body of the loop can be any valid statement!
            body_stmt = self.statement()
            return ast_nodes.LoopStmt(limit_expr, body_stmt)

        self.error(f"Invalid statement starting with '{self.current_token.value}'")

    def expr(self):
        return self.term()

    def term(self):
        node = self.factor()
        
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
                
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
            
        self.error(f"Unexpected factor: '{token.value}'")
