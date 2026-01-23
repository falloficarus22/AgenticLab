class LLMBackend:
    
    def __init__(self, model_name):
        self.model_name = model_name
    
    def generate(self, prompt, temperature=0.2, tools=None):
        # stub: Swap with Ollama / API / vLLM later
        return {
            "text": "return llm output here",
            "tool_calls": []
        }
        