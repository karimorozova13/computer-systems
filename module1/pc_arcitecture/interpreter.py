class  TokenType:
    INTEGER = "INTEGER"
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    EOF = 'EOF'
    
class Token:
    def __init__(self, type, val) -> None:
        self.type = type
        self.val = val
    def __str__(self) -> str:
        return f'Token({self.type}, {repr(self.val)})'
class LexicalError(Exception):
    pass

class Lexer:
    def __init__(self, text) -> None:
        self.text = text 
        self.pos = 0
        self.cur_char = self.text[self.pos]
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.cur_char = None
        else:
            self.cur_char = self.text[self.pos]
    def skip_whitespace(self):
        while self.cur_char is not None and self.cur_char.isspace():
            self.advance()
    def integer(self):
        res = ''
        while self.cur_char is not None and self.cur_char.isdigit():
            res += self.cur_char
            self.advance()
        return int(res)
    def get_next_token(self):
        while self.cur_char is not None:

            if self.cur_char.isspace():
                self.skip_whitespace()
                continue

            if self.cur_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if self.cur_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')

            if self.cur_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')

            raise LexicalError('Помилка лексичного аналізу')

        return Token(TokenType.EOF, None)
            