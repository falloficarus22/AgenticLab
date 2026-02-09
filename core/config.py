import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

class MASLConfig:
    """Centralized configuration management for MASL"""
    
    def __init__(self, config_file: str = "masl_config.json"):
        self.config_file = Path(config_file)
        self.config = self._load_default_config()
        self.load_config()
    
    def _load_default_config(self) -> Dict[str, Any]:
        """Load default configuration"""
        return {
            "llm": {
                "model_name": "deepseek-r1:1.5b",
                "base_url": "http://localhost:11434",
                "timeout": 30,
                "max_retries": 3
            },
            "agents": {
                "hypothesis": {
                    "temperature": 0.7,
                    "max_tokens": 1000,
                    "max_retries": 3
                },
                "planner": {
                    "temperature": 0.3,
                    "max_tokens": 1500,
                    "max_retries": 2
                },
                "executor": {
                    "timeout": 60,
                    "max_retries": 2
                },
                "analyzer": {
                    "temperature": 0.2,
                    "max_tokens": 2000,
                    "max_retries": 2
                },
                "critic": {
                    "temperature": 0.1,
                    "max_tokens": 1500,
                    "max_retries": 1
                }
            },
            "orchestrator": {
                "max_iterations": 5,
                "timeout_seconds": 300,
                "parallel_workers": 3,
                "enable_monitoring": True
            },
            "memory": {
                "storage_dir": "experiments",
                "auto_save": True,
                "compression": False
            },
            "visualization": {
                "output_dir": "visualizations",
                "dpi": 300,
                "style": "seaborn-v0_8",
                "interactive": False
            },
            "logging": {
                "level": "INFO",
                "structured_logging": True,
                "log_dir": "logs"
            },
            "optimization": {
                "auto_optimize": True,
                "target_success_rate": 0.8,
                "target_confidence": 0.7,
                "optimization_interval": 10
            }
        }
    
    def load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    user_config = json.load(f)
                self._merge_config(self.config, user_config)
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")
    
    def save_config(self):
        """Save current configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def _merge_config(self, default: Dict, user: Dict):
        """Recursively merge user config with defaults"""
        for key, value in user.items():
            if key in default and isinstance(default[key], dict) and isinstance(value, dict):
                self._merge_config(default[key], value)
            else:
                default[key] = value
    
    def get(self, key_path: str, default=None):
        """Get configuration value using dot notation"""
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def set(self, key_path: str, value: Any):
        """Set configuration value using dot notation"""
        keys = key_path.split('.')
        config = self.config
        
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        config[keys[-1]] = value
    
    def get_agent_config(self, agent_name: str) -> Dict[str, Any]:
        """Get configuration for a specific agent"""
        return self.get(f'agents.{agent_name}', {})
    
    def get_llm_config(self) -> Dict[str, Any]:
        """Get LLM configuration"""
        return self.get('llm', {})
    
    def is_monitoring_enabled(self) -> bool:
        """Check if performance monitoring is enabled"""
        return self.get('orchestrator.enable_monitoring', True)
    
    def validate_config(self) -> List[str]:
        """Validate configuration and return list of issues"""
        issues = []
        
        # Check LLM config
        llm_config = self.get_llm_config()
        if not llm_config.get('model_name'):
            issues.append("LLM model name not specified")
        
        # Check agent configs
        for agent_name in ['hypothesis', 'planner', 'executor', 'analyzer', 'critic']:
            agent_config = self.get_agent_config(agent_name)
            if 'temperature' not in agent_config:
                issues.append(f"Temperature not specified for {agent_name} agent")
        
        # Check directories
        memory_dir = Path(self.get('memory.storage_dir'))
        if not memory_dir.exists():
            try:
                memory_dir.mkdir(parents=True, exist_ok=True)
            except Exception:
                issues.append(f"Cannot create memory directory: {memory_dir}")
        
        return issues

# Global config instance
config = MASLConfig()
