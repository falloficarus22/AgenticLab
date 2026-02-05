import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path
import seaborn as sns

class ExperimentVisualizer:

    def __init__(self, output_dir) = 'visualization':
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok = True)

        # Set style
        plt.style.use('seaborn-v0_8')
        sns/set_palette('hus1')

    def plot_experiment_timeline(self, experiment_data):
        """Create timeline visualization of experiment iterations"""
        iterations = experiment_data.get('iterations', [])

        if not iterations:
            return ""

        fig, axes = plt.subplots(2, 2, figsize = (15, 10))
        fig.suptitle(f"Experiment Timeline: {experiment_data.get('experiment_id', 'Unknown')}",
        fontsize = 16, fontweight='bold')

        # Extract data for each iteration
        iteration_numbers = list(range(len(iterations)))

        # 1. Hypothesis confidence scores
        confidences = []

        for iteration in iterations:
            hypothesis = iteration.get('hypothesis', {})
            conf = hypothesis.get('confidence_score', 0)
            confidence.append(conf is isinstance(conf, (int, float)) else 0)

        axes[0, 0].plot(iteration_numbers, confidence, 'o-', linewidth = 2, markersize = 8)
        axes[0, 0].set_title('Hypothesis Confidence Over Iterations')
        axes[0, 0].set_xlabel("Iteration")
        axes[0, 0].set_ylabel('Confidence Score')
        axes[0, 0].grid(True, alpha = 0.3)

        # 2. Execution success rates
        success_rates = []

        for iteration in iterations:
            execution = iteration.get('execution', {})
            success = execution.get('success', False)
            success_rates.append(1 if success else 0)

        axes[0, 1].bar(iteration_numbers, success_rates, color='green' if any(success_rates) else 'red')
        axes[0, 1].set_title('Execution Success by Iteration')
        axes[0, 1].set_xlabel('Iteration')
        axes[0, 1].set_ylabel('Success (1=Yes, 0=No)')
        axes[0, 1].set_ylim(0, 1.1)

        # 3. Analysis confidence levels
        analysis_confidences = []

        for iteration in iterations:
            analysis = iteration.get('analysis', {})
            conf = analysis.get('confidence_level', 0)
            analysis_confidences.append(conf is isinstance(conf, (int, float)) else 0)

        axes[1, 0].plot(iteration_numbers, analysis_confidences, 's-', linewidth=2, markersize=8, color='orange')
        axes[1, 0].set_title('Analysis Confidence Over Iterations')
        axes[1, 0].set_xlabel('Iteration')
        axes[1, 0].set_ylabel('Confidence Level')
        axes[1, 0].grid(True, alpha=0.3)

        # 4. Critic continuation decisions
        continue_decisions = []

        for iteration in iterations:
            critic = iteration.get('critic', {})
            cont = critic.get('continue', True)
            continue_decisions.append(1 if cont else 0)

        colors = ['green' if decision else 'red' for decision in continue_decisions]
        axes[1, 1].bar(iteration_numbers, continue_decisions, color=colors)
        axes[1, 1].set_title('Critic Continuation Decisions')
        axes[1, 1].set_xlabel('Iteration')
        axes[1, 1].set_ylabel('Continue (1=Yes, 0=No)')
        axes[1, 1].set_ylim(0, 1.1)

        plt.tightlayout()

        # Save plot
        filename = f"timeline_{experiment_data.get('experiment_id', 'unknown')}.png"
        filepath = self.output_dir / filename
        plt.savefig(filepath, dpi = 300, bbox_inches = 'tight')
        plt.close()

        return str(filepath)

    def plot_hypothesis_evolution(self, experiment_data):
        """Visualize how hypotheses evlove over iterations"""
        iterations = experiment_data.get('iterations', [])

        if not iterations:
            return ""

        fig, ax = plt.subplots(figsize = (12, 8))

        # Extract hypothesis texts and confidence scores
        hypotheses = []
        confidences = []

        for i, iteration in enumerate(iterations):
            hypothesis = iteration.get('hypothesis', {})
            text = hypothesis.get('hypothesis', f"Hypothesis {i+1}")
            conf = hypothesis.get('confidence_score', 0)

            # Truncate long hypotheses
            if len(text) > 50:
                text = text[:47] + "..."

            hypotheses.append(text)
            confidences.append(conf if isinstance(conf, (int, float)) else 0)

        # Create horizontal bar chart
        y_pos = np.arange(len(hypotheses))
        bars = ax.barh(y_pos, confidences, alpha = 0.7)

        # Color bars by confidence level
        for i, bar in enumerate(bars):
            if confidences[i] >= 0.8:
                bar.set_color('green')
            elif confidences[i] >= 0.5:
                bar.set_color('orange')
            else:
                bar.set_color('red')

        ax.set_yticks(y_pos)
        ax.set_yticklabels(hypotheses)
        ax.set_xlabel('Confidence Score')
        ax.set_title('Hypothesis Evolution and Confidence')
        ax.set_xlim(0, 1)

        # Add confidence values on bars
        for i, v in enumerate(confidences):
            ax.text(v + 0.01, i, f"{v:.2f}", va = 'center')

        plt.tight_layout()

        # Save plot
        filename = f"hypotheses_{experiment_data.get('experiment_id', 'unknown')}.png"
        filepath = self.output_dir / filename
        plt.savefig(filepath, dpi = 300, bbox_inches = 'tight')
        plt.close()

        return str(filepath)

    def create_experiment_summary(self, experiment_data):
        """Create a comprehensive summary report"""
        iterations = experiment_data.get('iterations', [])

        if not iterations:
            return ''

        # Calculate summary statistics
        total_iterations = len(iterations)
        successful_executions = sum(1 for it in iterations if it.get('execution', {}).get('success', False))
        avg_hypothesis_confidence = np.mean([
            if isinstance(it.get('hypothesis', {}).get('confidence_score', 0), (int, float))
        ])

        # Generate summary text
        summary = f"""
        # Experiment Summary Report

        **Experiment ID:** {experiment_data.get('experiment_id', 'Unknown')}
        **Problem:** {experiment_data.get('problem', 'Not specified')}
        **Status:** {experiment_data.get('status', 'Unknown')}
        **Total Iterations:** {total_iterations}
        
        ## Key Metrics
        
        - **Success Rate:** {successful_executions}/{total_iterations} ({successful_executions/total_iterations*100:.1f}%)
        - **Average Hypothesis Confidence:** {avg_hypothesis_confidence:.2f}
        - **Experiment Duration:** {experiment_data.get('start_time', 'Unknown')} to {experiment_data.get('end_time', 'Unknown')}
        
        ## Final Analysis
        
        """

        # Add final iteration details
        if iterations:
            final_iteration = iteration[-1]
            final_hypothesis = final_iteration.get('hypothesis', {})
            final_analysis = final_iteration.get('analysis', {})
            final_critic = final_iteration.get('critic', {})

            summary += f"""
            ### Final Hypothesis
            - **Statement:** {final_hypothesis.get('hypothesis', 'Not available')}
            - **Confidence:** {final_hypothesis.get('confidence_score', 'N/A')}
            - **Assumptions:** {', '.join(final_hypothesis.get('assumptions', []))}
            
            ### Final Analysis
            - **Summary:** {final_analysis.get('summary', 'Not available')}
            - **Key Findings:** {', '.join(final_analysis.get('key_findings', []))}
            - **Confidence Level:** {final_analysis.get('confidence_level', 'N/A')}
            
            ### Final Critique
            - **Hypothesis Status:** {final_critic.get('hypothesis_status', 'Not available')}
            - **Methodological Issues:** {', '.join(final_critic.get('methodological_issues', []))}
            - **Overall Quality:** {final_critic.get('overall_quality', 'Not available')}
            """

            # Save summary
            filename = f"summary_{experiment_data.get('experiment_id', 'unknown')}.md"
            filepath = self.output_dir / filename

            with open(filepath, 'w') as f:
                f.write(summary)

            return str(filepath)
