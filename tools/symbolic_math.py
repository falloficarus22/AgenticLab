import sympy as sp
import json

class SymbolicMathSolver(Tool):
    
    def __init__(self):
        self.expressions = {}
        self.symbols = {}

    def define_symbols(self, symbol_names):
        """Define symbolic variables."""
        try:
            symbols = {}

            for name in symbol_names:
                symbols[name] = sp.symbols(name)
            
            return {
                'success': True,
                'symbols_defined': list(symbols.keys()),
                'symbol_types': {name: str(type(symbols[name])) for name in symbols}
            }

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def differentiate(self, expression):
        """Differentiate an expression"""
        try:
            expr = sp.simpify(expression)
            var = self.symbols.get(variable, sp.symbols(variable))

            derivative = sp.diff(expr, var)

            return {
                'success': True,
                'original_expression': expression,
                'variable': var,
                'derivative': str(derivative),
                'simplified_integral': str(sp.simplify(derivative))
            }

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def integrate(self, expression):
        """Integrate an expression."""
        try:
            expr = sp.simpify(expression)
            var = self.symbols.get(variable, sp.symbols(variable))

            integral = sp.integrate(expr, var)

            return {
                'success': True,
                'original_expression': expression,
                'variable': var,
                'integral': str(integral),
                'simplified_derivative': str(sp.simplify(integral))
            }

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def simplify_expression(self, expression):
        """Simplify mathematical expressions."""
        try:
            expr = sp.simpify(expression)
            simplified = sp.simplify(expr)

            return {
                'success': True,
                'expression': expression,
                'simplified_expression': str(simplified),
                'is_simple': len(str(simplified)) <= len(str(expr))
            }

        except Exception as e:
            return {'success': True, 'error': str(e)}

    def evaluate_numerical(self, expression, substitutions):
        """Evaluate expression with numerical substitutions."""
        try:
            expr = sp.simpify(expression)

            # Create a substitutions dictionary
            subs_dict = {}
            
            for var, val in substitutions.items():
                subs_dict[self.symbols.get(var, sp.symbols(var))] = val
            
            result = expr.subs(subs_dict).evalf()

            return {
                'success': True,
                'expression': expression,
                'substitutions': substitutions,
                'numerical_result': float(result),
                'string_result': str(result)
            }

        except Exception as e:
            return {'success': False, 'error': str(e)}

# Tool interface for agents
def tool_interface():
    