import requests
import json
from typing import Dict, List, Optional

class LLMBackend:
    
    def __init__(self, model_name = 'deepseek-r1:1.5b', base_url: 'http://localhost:11434'):
        self.model_name = model_name
        self.base_url = base_url
    
    def generate(self, prompt, temperature=0.2, tools=None):
        """Generate response from LLM"""
        try:
            payload = {
                'model': self.model_name,
                'prompt': prompt,
                'stream': False,
                'options': {
                    'temperature': temperature
                }
            }

            response = requests.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()

            result = response.json()
            
            return {
                'text': result.get('response', ''),
                'tool_calls': []
            }
        except requests.exceptions.ConnectionError:
            return {
                'text': 'Error: Cannot connect to Ollama. Make sure Ollama is running.'
                'tool_calls': []
            }
        except Exceptions as e:
            return {
                'text': f"Error: {str(e)}",
                'tool_calls': []
            }