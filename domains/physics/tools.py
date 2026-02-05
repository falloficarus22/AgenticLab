from tools.physics_simulator import execute_physics_simulation
import numpy as np
from typing import Dict, Any, List

class PhysicsToolKit:
    """Specialized physics tools for MASL"""
    
    @staticmethod
    def analyze_pendulum_period_vs_length() -> Dict[str, Any]:
        """Analyze how pendulum period varies with length"""
        try:
            lengths = [0.1, 0.2, 0.5, 1.0, 1.5, 2.0]  # meters
            periods = []
            
            for length in lengths:
                result = execute_physics_simulation(
                    'pendulum', 
                    length=length, 
                    initial_angle=10,  # small angle
                    duration=5.0
                )
                
                if result['success']:
                    period = result['analysis']['period']
                    periods.append(period)
                else:
                    periods.append(0)
            
            # Theoretical periods (small angle approximation)
            theoretical_periods = [2 * 3.14159 * np.sqrt(l / 9.81) for l in lengths]
            
            return {
                'success': True,
                'lengths_tested': lengths,
                'measured_periods': periods,
                'theoretical_periods': theoretical_periods,
                'analysis': {
                    'correlation': np.corrcoef(periods, theoretical_periods)[0,1],
                    'mean_error': np.mean(np.abs(np.array(periods) - np.array(theoretical_periods)))
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def test_projectile_range_formula() -> Dict[str, Any]:
        """Test projectile motion range formula"""
        try:
            v0 = 20  # m/s
            angles = [15, 30, 45, 60, 75]  # degrees
            
            measured_ranges = []
            theoretical_ranges = []
            
            for angle in angles:
                # Simulate
                result = execute_physics_simulation(
                    'projectile',
                    initial_velocity=v0,
                    angle=angle
                )
                
                if result['success']:
                    measured_range = result['metrics']['range']
                    measured_ranges.append(measured_range)
                    
                    # Theoretical: R = v0² * sin(2θ) / g
                    import math
                    theoretical_range = (v0**2 * math.sin(2 * math.radians(angle))) / 9.81
                    theoretical_ranges.append(theoretical_range)
            
            return {
                'success': True,
                'initial_velocity': v0,
                'angles_tested': angles,
                'measured_ranges': measured_ranges,
                'theoretical_ranges': theoretical_ranges,
                'accuracy': {
                    'mean_absolute_error': np.mean(np.abs(np.array(measured_ranges) - np.array(theoretical_ranges))),
                    'max_error': np.max(np.abs(np.array(measured_ranges) - np.array(theoretical_ranges)))
                }
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
            