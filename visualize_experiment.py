"""
Quick script to visualize experiment results
"""

import sys
from pathlib import Path
from core.memory import ExperimentMemory

def main():
    if len(sys.argv) != 2:
        print(f'Usage: python visualize_experiment.py {experiment_id}')
        sys.exit(1)

    experiment_id = sys.argv[1]
    memory = ExperimentMemory()

    print(f'General visualizations for experiment: {experiment_id}')

    # General visualizations
    viz_results = memory.generate_visualizations(experiment_id)

    if 'error' in viz_results:
        print(f"Error: {viz_results['error']}")
        sys.exit(1)
    
    print(f"Visualizations Created.")

    for viz_type, filepath in viz_results.items():
        print(f"{viz_type}: {filepath}")

    # Create dashboard
    dashboard_path = memory.create_visualization_dashboard(experiment_id)

    if dashboard_path:
        print(f"Dashboard: {dashboard_path}")

    print(f"Open {dashboard_path} in your browser to view full dashboard.")

if __name__ == '__main__':
    main()
    