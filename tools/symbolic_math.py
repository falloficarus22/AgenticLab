import sympy as sp
from core.tools import Tool

class SymbolicMathTool(Tool):
    
    name = "symbolic_math"
    description = "Simplify or solve symbolic math expressions"
    input_schema = {
        'expression': 'string'
    }

    def run(self, inputs):
        expr = sp.sympify(inputs['expression'])
        simplified = sp.simplify(expr)

        return {
            'simplified': str(simplified)
        }
        