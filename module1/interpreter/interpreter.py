from lexer import TokenType
from parser import  Num, BinOp

def print_ast(node, level=0):
    indent = ' ' * level
    if isinstance(node, Num):
        print(f"{indent}Num({node.val})")
    elif isinstance(node, BinOp):
        print(f"{indent}BinOp:")
        print(f"{indent} left: ")
        print_ast(node.left, level + 2)
        print(f"{indent} op: {node.op.type}")
        print(f"{indent} right: ")
        print_ast(node.right, level + 2)
    else:
        print(f"{indent}Unknown node type: {type(node)}")



class Interpreter:
    def __init__(self, parser) -> None:
        self.parser = parser
    def visit_BinOp(self, node):
        if node.op.type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenType.MINUS:
            return self.visit(node.left) -  self.visit(node.right)
    def visit_Num(self, node):
        return node.val
    def interpret(self):
        tree = self.parser.expr()
        print_ast(tree)
        return self.visit(tree)
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    def generic_visit(self, node):
        raise Exception(f'Немає методу visit_{type(node).__name__}')
        
    
            