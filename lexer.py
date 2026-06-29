import enum

class TokenType(enum.Enum):
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    EOF = 'EOF'
    COMMA = 'COMMA'
    
    # Keywords
    SET = 'SET'
    TO = 'TO'
    CREATE = 'CREATE'
    VARIABLE = 'VARIABLE'
    PRINT = 'PRINT'
    LOOP = 'LOOP'
    TILL = 'TILL'
    AND = 'AND'
    EVERY = 'EVERY'
    VALUE = 'VALUE'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    TIMES = 'TIMES'
    DIVIDED = 'DIVIDED'
    BY = 'BY'
    
    # Phase 2 Keywords
    IF = 'IF'
    THEN = 'THEN'
    IS = 'IS'
    GREATER = 'GREATER'
    LESS = 'LESS'
    THAN = 'THAN'
    EQUAL = 'EQUAL'
    DEFINE = 'DEFINE'
    ACTION = 'ACTION'
    WITH = 'WITH'
    DO = 'DO'
    RUN = 'RUN'
    
    # Phase 3 Keywords
    END = 'END'
    LIST = 'LIST'
    CONTAINING = 'CONTAINING'
    ITEM = 'ITEM'
    OF = 'OF'
    ASK = 'ASK'
    FOR = 'FOR'
    EACH = 'EACH'
    IN = 'IN'

    # Phase 4 Keywords
    OBJECT = 'OBJECT'
    AS = 'AS'
    PROPERTY = 'PROPERTY'
    OR = 'OR'
    READ = 'READ'
    FILE = 'FILE'
    WRITE = 'WRITE'
    INTO = 'INTO'
    RETURN = 'RETURN'
    WHILE = 'WHILE'
    TRY = 'TRY'
    BUT = 'BUT'
    IT = 'IT'
    FAILS = 'FAILS'

    # Phase 5 Keywords
    LENGTH = 'LENGTH'
    SPLIT = 'SPLIT'
    UPPERCASE = 'UPPERCASE'
    LOWERCASE = 'LOWERCASE'
    REPLACE = 'REPLACE'
    CONTAINS = 'CONTAINS'
    ADD = 'ADD'
    REMOVE = 'REMOVE'
    FROM = 'FROM'

KEYWORDS = {
    'set': TokenType.SET,
    'to': TokenType.TO,
    'create': TokenType.CREATE,
    'variable': TokenType.VARIABLE,
    'print': TokenType.PRINT,
    'loop': TokenType.LOOP,
    'till': TokenType.TILL,
    'and': TokenType.AND,
    'every': TokenType.EVERY,
    'value': TokenType.VALUE,
    'plus': TokenType.PLUS,
    'minus': TokenType.MINUS,
    'times': TokenType.TIMES,
    'divided': TokenType.DIVIDED,
    'by': TokenType.BY,
    'if': TokenType.IF,
    'then': TokenType.THEN,
    'is': TokenType.IS,
    'greater': TokenType.GREATER,
    'less': TokenType.LESS,
    'than': TokenType.THAN,
    'equal': TokenType.EQUAL,
    'define': TokenType.DEFINE,
    'action': TokenType.ACTION,
    'with': TokenType.WITH,
    'do': TokenType.DO,
    'run': TokenType.RUN,
    'end': TokenType.END,
    'list': TokenType.LIST,
    'containing': TokenType.CONTAINING,
    'item': TokenType.ITEM,
    'of': TokenType.OF,
    'ask': TokenType.ASK,
    'for': TokenType.FOR,
    'each': TokenType.EACH,
    'in': TokenType.IN,
    'object': TokenType.OBJECT,
    'as': TokenType.AS,
    'property': TokenType.PROPERTY,
    'or': TokenType.OR,
    'read': TokenType.READ,
    'file': TokenType.FILE,
    'write': TokenType.WRITE,
    'into': TokenType.INTO,
    'return': TokenType.RETURN,
    'while': TokenType.WHILE,
    'try': TokenType.TRY,
    'but': TokenType.BUT,
    'it': TokenType.IT,
    'fails': TokenType.FAILS,
    'length': TokenType.LENGTH,
    'split': TokenType.SPLIT,
    'uppercase': TokenType.UPPERCASE,
    'lowercase': TokenType.LOWERCASE,
    'replace': TokenType.REPLACE,
    'contains': TokenType.CONTAINS,
    'add': TokenType.ADD,
    'remove': TokenType.REMOVE,
    'from': TokenType.FROM,
}

class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)}, line={self.line}, col={self.column})"

class LexerError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} at line {line}, column {column}")
        self.line = line
        self.column = column

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.column = 0
        self.pos += 1
        self.column += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ''
        start_col = self.column
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        
        if '.' in result:
            return Token(TokenType.NUMBER, float(result), self.line, start_col)
        return Token(TokenType.NUMBER, int(result), self.line, start_col)

    def string(self):
        result = ''
        start_col = self.column
        quote_type = self.current_char
        self.advance() # Skip opening quote
        
        while self.current_char is not None and self.current_char != quote_type:
            result += self.current_char
            self.advance()
            
        if self.current_char == quote_type:
            self.advance() # Skip closing quote
            return Token(TokenType.STRING, result, self.line, start_col)
        else:
            raise LexerError("Unterminated string literal", self.line, start_col)

    def word(self):
        result = ''
        start_col = self.column
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
            
        lower_result = result.lower()
        if lower_result in KEYWORDS:
            return Token(KEYWORDS[lower_result], lower_result, self.line, start_col)
        return Token(TokenType.IDENTIFIER, result, self.line, start_col)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
                
            if self.current_char == ',':
                start_col = self.column
                self.advance()
                return Token(TokenType.COMMA, ',', self.line, start_col)
                
            if self.current_char.isdigit():
                return self.number()
                
            if self.current_char.isalpha() or self.current_char == '_':
                return self.word()
                
            if self.current_char in ("'", '"'):
                return self.string()
                
            raise LexerError(f"Unexpected character '{self.current_char}'", self.line, self.column)
            
        return Token(TokenType.EOF, None, self.line, self.column)
