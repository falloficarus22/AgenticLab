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
        except requests.exceptions.ConnectionError:
            return {
                'text': "Error: Request timed out. Model might be busy.",
                'tool_calls': []
            }
        except Exceptions as e:
            return {
                'text': f"Error: {str(e)}",
                'tool_calls': []
            }

def test_connection(self):
    """Test if Ollama is accessible and model is available."""
    try:
        response = requests.get(f"{self.base_url}/api/tags", timeout=5)
        response.raise_for_status()

        models = response.json().get('models', [])
        model_names = [model["name"] for model in models]

        return self.model_name in model_names

    except Exception as e:
        return False

if __name__ == "__main__":
    llm = LLMBackend()
    print("Testing connection...")

    if llm.test_connection():
        print('Connection successful!')
        resutl = llm.generate("What is 2+2?")
        print(f"Response: {result['text']}")
    else:
        print("Connection failed. Make sure Ollama is running and the model is available.")
        