import ast
import operator
import numpy as np

def safe_eval(expr, variables):
    tree = ast.parse(expr, mode='eval')
    
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }
    
    allowed_nodes = {
        ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant,
        ast.Name, ast.Call,
        ast.Load,
        ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
        ast.USub, ast.UAdd,
    }
    
    def eval_node(node):
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.Name):
            return variables[node.id]
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            return operators[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            op_type = type(node.op)
            return operators[op_type](operand)
            
    return eval_node(tree.body)

point_dict = {'omega_b': 0.025417209102884357, 'omega_cdm': 0.19109866676343235, 'H0': 81.29777513829538}
try:
    print(safe_eval("1.0 - (omega_b + omega_cdm) / (H0/100)**2", point_dict))
except Exception as e:
    print("ERROR:", repr(e))
