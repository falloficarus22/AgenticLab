import time
import psutil
import threading
from typing import Dict, Any, List
from collections import deque
import json
from pathlib import Path

class PerformanceMonitor:
    """Monitor system and experiment performance"""
    
    def __init__(self, history_size: int = 1000):
        self.history_size = history_size
        self.metrics = {
            'experiment_durations': deque(maxlen=history_size),
            'agent_response_times': deque(maxlen=history_size),
            'system_resources': deque(maxlen=history_size),
            'error_rates': deque(maxlen=history_size)
        }
        self.start_times = {}
        self.lock = threading.Lock()
    
    def start_experiment_timer(self, experiment_id: str):
        """Start timing an experiment"""
        with self.lock:
            self.start_times[experiment_id] = time.time()
    
    def end_experiment_timer(self, experiment_id: str) -> float:
        """End timing and record duration"""
        with self.lock:
            if experiment_id in self.start_times:
                duration = time.time() - self.start_times[experiment_id]
                del self.start_times[experiment_id]
                self.metrics['experiment_durations'].append({
                    'experiment_id': experiment_id,
                    'duration': duration,
                    'timestamp': time.time()
                })
                return duration
        return 0.0
    
    def record_agent_response(self, agent_name: str, duration: float, success: bool):
        """Record agent response time"""
        with self.lock:
            self.metrics['agent_response_times'].append({
                'agent': agent_name,
                'duration': duration,
                'success': success,
                'timestamp': time.time()
            })
    
    def record_system_resources(self):
        """Record current system resource usage"""
        with self.lock:
            self.metrics['system_resources'].append({
                'cpu_percent': psutil.cpu_percent(),
                'memory_percent': psutil.virtual_memory().percent,
                'disk_usage': psutil.disk_usage('/').percent,
                'timestamp': time.time()
            })
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary statistics"""
        with self.lock:
            summary = {}
            
            # Experiment durations
            if self.metrics['experiment_durations']:
                durations = [m['duration'] for m in self.metrics['experiment_durations']]
                summary['experiments'] = {
                    'count': len(durations),
                    'avg_duration': sum(durations) / len(durations),
                    'min_duration': min(durations),
                    'max_duration': max(durations)
                }
            
            # Agent performance
            if self.metrics['agent_response_times']:
                agent_stats = {}
                for record in self.metrics['agent_response_times']:
                    agent = record['agent']
                    if agent not in agent_stats:
                        agent_stats[agent] = []
                    agent_stats[agent].append(record['duration'])
                
                summary['agents'] = {}
                for agent, times in agent_stats.items():
                    summary['agents'][agent] = {
                        'avg_response_time': sum(times) / len(times),
                        'total_calls': len(times),
                        'success_rate': sum(1 for r in self.metrics['agent_response_times'] 
                                        if r['agent'] == agent and r['success']) / len(times)
                    }
            
            # System resources
            if self.metrics['system_resources']:
                recent = list(self.metrics['system_resources'])[-10:]  # Last 10 measurements
                summary['system'] = {
                    'avg_cpu': sum(r['cpu_percent'] for r in recent) / len(recent),
                    'avg_memory': sum(r['memory_percent'] for r in recent) / len(recent),
                    'disk_usage': recent[-1]['disk_usage'] if recent else 0
                }
            
            return summary
    
    def save_metrics(self, filepath: str = None):
        """Save metrics to file"""
        if filepath is None:
            filepath = f"metrics_{int(time.time())}.json"
        
        with open(filepath, 'w') as f:
            json.dump(dict(self.metrics), f, indent=2, default=list)

# Global monitor instance
performance_monitor = PerformanceMonitor()
