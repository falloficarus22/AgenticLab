import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

class ExperimentMemory:

    def __init__(self, storage_dir = 'experiments'):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok = True)
        self.current_experiment = None
        self.experiment_log = []

    def start_experiment(self, problem, experiment_id):
        """Start a new experiment session."""
        if experiment_id is None:
            experiment_id = f"exp_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        self.current_experiment = {
            'experiment_id': experiment_id,
            'problem': problem,
            'start_time': datetime.now().isoformat(),
            'iterations': [],
            'status': 'running'
        }

        return experiment_id

    def log_iteration(self, iteration_data):
        """Log a complete iteration of a scientific method."""
        if self.current_experiment is None:
            raise ValueError("No experiment found. Call start_experiment() first")
        
        iteration_entry = {
            'iteration_number': len(self.current_experiment['iterations']),
            'timestamp': datetime.now().isoformat(),
            'hypothesis': iteration_data.get('hypothesis'),
            'planner': iteration_data.get('planner'),
            'executor': iteration_data.get('executor'),
            'analyzer': iteration_data.get('analyzer'),
            'critic': iteration_data.get('critic'),
            'continue': iteration_data.getr('critic', {}).get('continue', True)
        }

        self.current_experiment['iterations'].append(iteration_entry)

    def end_experiment(self, final_status = 'completed'):
        """End the current experiment and save to disk."""
        if self.current_experiment is None:
            raise ValueError("No experiment to end.")

        self.current_experiment['end_time'] = datetime.now().isoformat()
        self.current_experiment['status'] = final_status

        # Save to file
        filename = f"{self.current_experiment['experiment_id']}.json"
        filepath = self.storage_dir / filename

        with open(filepath, 'w') as f:
            json.dump(self.current_experiment, f, indent = 2)
        
        self.experiment_log.append(self.current_experiment)
        self.current_experiment = None

    def get_experiment(self, experiment_id):
        """Retrieve a specific experiment by ID."""
        filepath = self.storage_dir / f"{experiment_id}.json"

        if filepath.exists():
            with open(filepath, 'r') as f:
                return json.load(f)

        return None

    def list_experiments(self):
        """List all experiments"""
        experiments = []

        for filepath in self.storage_dir.glob("*.json"):
            with open(filepath, 'r') as f:
                experiments.append(json.load(f))

        return sorted(experiments, key = lambda x: x.get('start_time', ''))

    def get_last_iteration(self):
        """Get the last iteration of the current experiment."""
        if self.current_experiment and self.current_experiment['iterations']:
            return self.current_experiment['iterations'][-1]
        
        return None
    
    def save_checkpoint(self):
        """Save current state as checkpoint."""
        if self.current_experiment is None:
            raise ValueError('No current experiment to save as checkpoint.')

        checkpoint_id = f"checkpoint_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        filename = f"{checkpoint_id}.json"
        filepath = self.storage_dir / filename

        with open(filepath, 'w') as f:
            json.dump(self.current_experiment, f, indent = 2)

        return checkpoint_id
