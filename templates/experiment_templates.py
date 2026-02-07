from typing import Dict, Any, List

class ExperimentTemplates:
    """Pre-defined experiment templates for common scientific tasks"""
    
    @staticmethod
    def prime_number_research() -> Dict[str, Any]:
        """Template for prime number research"""
        return {
            "name": "Prime Number Research",
            "description": "Analyze patterns and conjectures in prime numbers",
            "default_problems": [
                "Find patterns in prime gaps",
                "Test Goldbach's conjecture for a range",
                "Analyze twin prime distribution",
                "Investigate prime number theorem"
            ],
            "tools_required": ["symbolic_math", "data_analysis"],
            "success_criteria": [
                "Generate falsifiable hypothesis",
                "Provide statistical evidence",
                "Compare with known results"
            ],
            "max_iterations": 4
        }
    
    @staticmethod
    def physics_simulation() -> Dict[str, Any]:
        """Template for physics simulations"""
        return {
            "name": "Physics Simulation",
            "description": "Test physical laws through simulation",
            "default_problems": [
                "Verify pendulum period formula",
                "Test projectile motion equations",
                "Analyze energy conservation",
                "Simulate orbital mechanics"
            ],
            "tools_required": ["physics_simulator", "data_analysis"],
            "success_criteria": [
                "Accurate simulation setup",
                "Comparison with theoretical predictions",
                "Error analysis within acceptable bounds"
            ],
            "max_iterations": 3
        }
    
    @staticmethod
    def ml_model_analysis() -> Dict[str, Any]:
        """Template for ML model analysis"""
        return {
            "name": "ML Model Analysis",
            "description": "Analyze machine learning model behavior",
            "default_problems": [
                "Analyze bias-variance tradeoff",
                "Test learning curve patterns",
                "Compare model architectures",
                "Investigate overfitting causes"
            ],
            "tools_required": ["data_analysis", "statistical_tools"],
            "success_criteria": [
                "Quantitative performance metrics",
                "Statistical significance testing",
                "Reproducible results"
            ],
            "max_iterations": 5
        }
    
    @classmethod
    def get_template(cls, template_name: str) -> Dict[str, Any]:
        """Get a specific template by name"""
        templates = {
            'prime_research': cls.prime_number_research(),
            'physics_simulation': cls.physics_simulation(),
            'ml_analysis': cls.ml_model_analysis()
        }
        
        return templates.get(template_name, {})
    
    @classmethod
    def list_templates(cls) -> List[str]:
        """List all available templates"""
        return ['prime_research', 'physics_simulation', 'ml_analysis']
        