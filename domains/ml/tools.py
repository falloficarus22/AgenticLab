import numpy as np
from typing import Dict, Any, List
import random

class MLToolKit:
    """Specialized machine learning tools for MASL"""
    
    @staticmethod
    def analyze_learning_curves() -> Dict[str, Any]:
        """Analyze learning curves for different model complexities"""
        try:
            # Simulate training data
            np.random.seed(42)
            
            complexities = ['simple', 'medium', 'complex']
            results = {}
            
            for complexity in complexities:
                # Simulate training and validation loss curves
                epochs = 50
                
                if complexity == 'simple':
                    # Underfitting model
                    train_loss = [2.0 * np.exp(-0.1 * e) + 0.5 + 0.1 * np.random.normal() for e in range(epochs)]
                    val_loss = [2.2 * np.exp(-0.08 * e) + 0.6 + 0.15 * np.random.normal() for e in range(epochs)]
                elif complexity == 'medium':
                    # Good fit
                    train_loss = [2.0 * np.exp(-0.15 * e) + 0.1 + 0.05 * np.random.normal() for e in range(epochs)]
                    val_loss = [2.1 * np.exp(-0.12 * e) + 0.15 + 0.08 * np.random.normal() for e in range(epochs)]
                else:
                    # Overfitting model
                    train_loss = [2.0 * np.exp(-0.2 * e) + 0.05 * np.random.normal() for e in range(epochs)]
                    val_loss = [2.0 * np.exp(-0.1 * e) + 0.3 + 0.1 * np.random.normal() for e in range(epochs)]
                
                results[complexity] = {
                    'train_loss': train_loss,
                    'val_loss': val_loss,
                    'final_train_loss': train_loss[-1],
                    'final_val_loss': val_loss[-1],
                    'overfitting_gap': val_loss[-1] - train_loss[-1]
                }
            
            # Analysis
            best_model = min(results.keys(), key=lambda x: results[x]['final_val_loss'])
            overfitting_detected = any(results[x]['overfitting_gap'] > 0.2 for x in results)
            
            return {
                'success': True,
                'results': results,
                'analysis': {
                    'best_model': best_model,
                    'overfitting_detected': overfitting_detected,
                    'recommendation': 'Use medium complexity model' if not overfitting_detected else 'Reduce model complexity'
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def test_bias_variance_tradeoff() -> Dict[str, Any]:
        """Test bias-variance tradeoff with different model complexities"""
        try:
            np.random.seed(42)
            
            # Generate synthetic data
            X = np.linspace(0, 10, 100)
            y_true = 2 * X + 1 + np.sin(X)  # True function
            y_noisy = y_true + np.random.normal(0, 0.5, len(X))
            
            models = ['linear', 'polynomial_degree_3', 'polynomial_degree_10']
            results = {}
            
            for model in models:
                if model == 'linear':
                    # High bias, low variance
                    bias = 0.8
                    variance = 0.1
                elif model == 'polynomial_degree_3':
                    # Good balance
                    bias = 0.2
                    variance = 0.3
                else:
                    # Low bias, high variance
                    bias = 0.05
                    variance = 0.8
                
                # Simulate multiple training runs
                errors = []
                for _ in range(50):
                    # Simulate model prediction with bias and variance
                    prediction = y_true + bias * np.random.normal(0, 1, len(X)) + variance * np.random.normal(0, 1, len(X))
                    mse = np.mean((prediction - y_noisy)**2)
                    errors.append(mse)
                
                results[model] = {
                    'bias_estimate': bias,
                    'variance_estimate': variance,
                    'mean_squared_error': np.mean(errors),
                    'std_error': np.std(errors)
                }
            
            # Find optimal model
            optimal_model = min(results.keys(), key=lambda x: results[x]['mean_squared_error'])
            
            return {
                'success': True,
                'models_tested': models,
                'results': results,
                'optimal_model': optimal_model,
                'insight': f"{optimal_model} provides the best bias-variance tradeoff"
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
            