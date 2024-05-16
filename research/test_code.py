import ast


class IfStatementExtractor(ast.NodeVisitor):
    def __init__(self):
        self.if_statements = []

    def visit_If(self, node):
        if (isinstance(node.test, ast.Compare) and
                isinstance(node.test.left, ast.Name) and
                isinstance(node.test.ops[0], ast.IsNot) and
                isinstance(node.test.comparators[0], ast.Constant) and
                node.test.comparators[0].value is None):
            self.if_statements.append((node.test.left.id, node))
        self.generic_visit(node)


def extract_if_statements(code):
    tree = ast.parse(code)
    extractor = IfStatementExtractor()
    extractor.visit(tree)
    return extractor.if_statements


class Nothing:
    def __bool__(self):
        return False

    def __str__(self):
        return ""

    def __len__(self):
        return 0

    def __iter__(self):
        return iter([])

    def __repr__(self):
        return "Nothing()"


def simulate_if_block(var_name, if_node, global_vars):
    local_vars = {var_name: Nothing()}
    if_code_ast = ast.Module(body=if_node.body, type_ignores=[])
    if_code_source = ast.unparse(if_code_ast)
    print(f"Executing the following code with '{var_name}' replaced by 'Nothing':\n{if_code_source}")
    code = compile(if_code_ast, '<string>', 'exec')
    exec(code, global_vars, local_vars)


def process_code(code):
    if_statements = extract_if_statements(code)
    for var_name, if_node in if_statements:
        global_vars = {}
        try:
            simulate_if_block(var_name, if_node, global_vars)
            print(f"Block for 'if {var_name} is not None' executed without exceptions.\n")
        except Exception as e:
            print(f"Exception in block for 'if {var_name} is not None': {e}\n")


# Example usage
code = """
x = 5
if x is not None:
    print(x)

y = None
if y is not None:
    print(y)

z = "Hello"
if z is not None:
    print(z.upper())
"""

process_code(code)
