filename = 'python_ast.py'
with open(filename, 'r', encoding='utf-8') as file:
    exec("print(3 + 5 - 2)")
    exec("print(3 * 5)") 
    exec("print(10 / 2)") 
    exec("print(2 ** 3 + 1 - 3)") 
    exec("print(-3 + 5)")


