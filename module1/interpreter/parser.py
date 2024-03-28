from lexer import TokenType

class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right) -> None:
        self.left = left
        self.op = op
        self.right = right

class Num(AST):
    def __init__(self,token) -> None:
        self.token = token
        self.val =  token.val


class ParsingErr(Exception):
    pass

class Parser:
    def __init__(self, lexer) -> None:
        self.lexer = lexer
        self.cur_token = self.lexer.get_next_token()
    def error(self):
        raise ParsingErr('Помилка синтаксичного аналізу')
    def eat(self, token_type):
        if self.cur_token.type == token_type:
            self.cur_token = self.lexer.get_next_token()
        else:
            self.error()
    def term(self):
        token = self.cur_token
        self.eat(TokenType.INTEGER)
        return Num(token)
    def expr(self):
        node = self.term()
        while self.cur_token.type in [TokenType.MINUS, TokenType.PLUS]:
            token = self.cur_token
            if token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            elif token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            node = BinOp(left=node, op=token, right=self.term())
        return node