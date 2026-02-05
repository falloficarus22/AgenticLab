from tools.symbolic_math import execute_symbolic_math
import sympy as sp
from typing import Dict, Any, List

class MathToolKit:
    """Specialized mathematics tools for MASL"""
    
    @staticmethod
    def analyze_prime_gaps(limit: int = 100) -> Dict[str, Any]:
        """Analyze gaps between consecutive primes"""
        try:
            # Generate primes
            primes = list(sp.primerange(2, limit + 1))
            
            # Calculate gaps
            gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
            
            # Statistics
            gap_stats = {
                'max_gap': max(gaps),
                'min_gap': min(gaps),
                'avg_gap': sum(gaps) / len(gaps),
                'gap_distribution': {gap: gaps.count(gap) for gap in set(gaps)}
            }
            
            return {
                'success': True,
                'primes_found': len(primes),
                'gaps': gaps,
                'statistics': gap_stats,
                'conjectures': [
                    "Prime gaps tend to increase as numbers get larger",
                    "Even gaps are more common than odd gaps (except gap=1)"
                ]
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def test_goldbach_conjecture(limit: int = 100) -> Dict[str, Any]:
        """Test Goldbach's conjecture for even numbers"""
        try:
            primes = list(sp.primerange(2, limit + 1))
            prime_set = set(primes)
            
            counterexamples = []
            tested_numbers = []
            
            for n in range(4, limit + 1, 2):
                tested_numbers.append(n)
                found = False
                
                for p in primes:
                    if p > n:
                        break
                    if (n - p) in prime_set:
                        found = True
                        break
                
                if not found:
                    counterexamples.append(n)
            
            return {
                'success': True,
                'tested_range': f"4 to {limit}",
                'numbers_tested': len(tested_numbers),
                'counterexamples': counterexamples,
                'conjecture_holds': len(counterexamples) == 0,
                'prime_pairs_found': len(tested_numbers) - len(counterexamples)
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
            