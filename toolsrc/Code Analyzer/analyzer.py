import os
import sys
import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_FunctionDef(self, node):
        if len(node.name) < 3:
            self.errors.append(f"Function name '{node.name}' is too short at line {node.lineno}")
        self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name) and len(node.targets[0].id) < 3:
            self.errors.append(f"Variable name '{node.targets[0].id}' is too short at line {node.lineno}")
        self.generic_visit(node)

def analyze_code(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    return analyzer.errors

def main():
    if len(sys.argv) != 2:
        print("Usage: python code_analyzer.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"File '{file_path}' does not exist.")
        sys.exit(1)

    errors = analyze_code(file_path)
    if errors:
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print(f"No issues found in '{file_path}'")

if __name__ == "__main__":
    main()
