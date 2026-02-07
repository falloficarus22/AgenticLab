import numpy as np
from pathlib import pathlib

class MetaAnalyzer:
    """Analyze and compare multiple experiments"""

    def __init__(self, memory):
        self.memory = memory

    def compare_experiments(self, experiment_ids):
        """Compare multiple experiments"""
        experiments = []

        for exp_id in experiments_ids:
            exp_data = self.memory.get_experiment(exp_id)

            if exp_data:
                experiments.append(exp_data)

        if not experiments:
            return {'error': 'No valid experiments found'}

        comparison = {
            'experiment_count': len(experiments),
            'experiments': experiment_ids,
            'metrics': self._calculate_comparison_metrics(experiments),
            'hypothesis_evolution': self._analyze_hypothesis_evolution(experiments),
            'success_patterns': self._identify_success_patterns(experiments)
        }

        return comparison

    def _calculate_comparison_metrics(self, experiments):
        """Calculate comparative metrics"""
        metrics = {
            'avg_iteration': np.mean([len(exp.get('iterations', [])) for exp in experiments]),
            'success_rates': [],
            'confidence_trends': [],
            'provblem_domains': []
        }

        for exp in experiments:
            iterations = exp.get('iterations', [])

            if iterations:
                # Success rate
                successful = sum(1 for it in iterations if it.get('execution', {}).get('success', False))
                success_rate = successful / len(iterations)
                metrics['success_rates'].append(success_rate)

                # Confidence trends
                confidences = [
                    it.get('hypothesis', {}).get('confidence_score', 0) for it in iterations

                    if isinstance(it.get('hypothesis', {}).get('confidence_score', 0), (int, float))
                ]
                metrics['confidnce_trends'].append(confidences)
        return metrics

    def _analyze_hypothesis_evolution(self, experiments):
        """Analyze how hypotheses evolve across experiments"""
        evolution_patterns = {
            'convergence_rate': 0,
            'common_themes': [],
            'improvement_rate': 0
        }

        # Analyze hypothesis themes
        all_hypotheses = []

        for exp in experiments:
            for iteration in exp.get('iterations', []):
                hypothesis = iteration.get('hypothesis', {}).get('hypothesis', '')

                if hypothesis:
                    all_hypotheses.append(hypothesis)

        # Extract common keywords/themes
        from collections import Counter
        words = ' '.join(all_hypotheses).lower().split()
        common_words = Counter(words).most_common(10)
        evolution_patterns['common_themes'] = [word for word, count in common_words if len(word) > 3]

        return evolution_patterns
    
    def _identify_success_patterns(self, experiments):
        """Identify patterns that lead to successful experiments"""
        success_experiments = []
        failed_experiments = []

        for exp in experiments:
            iterations = exp.get('iterations', [])

            if iterations:
                final_critic = iterations[-1].get('critic', {})

                if final_critic.get('hypothesis_status') in ['supported', 'conclusive']:
                    successful_experiments.append(exp)
                else:
                    failed_experiments.append(exp)

        patterns = {
            'success_factors': [],
            'failure_patterns': [],
            'optimal_iterations': 0
        }

        if successful_experiments:
            # Analyze what makes experiments successful
            success_iterations = [len(exp.get('iterations', [])) for exp in successful_experiments]
            patterns['optimal_iterations'] = int(np.mean(success_iterations))

        return patterns
