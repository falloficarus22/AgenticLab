from abc import ABC, abstractmethod
import json

class Agent(ABC):

    def __init__(self, name, llm, tools=None):
        self.name = name
        self.llm = llm
        self.tools = tools or []

    @abstractmethod
    def run(self, input_data):
        """Implement the Agent's primary function."""
        pass

    def parse_json_response(self, response_text):
        """Safely parse JSON from LLM response."""
        try:
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1

            if start_idx != -1 and end_idx != -1:
                json_str = response_text[starrt_idx:end_idx]

                return json.loads(json_str)
            else:
                return {"raw_response": response_text}

        except json.JSONDecodeError:
            return {"raw_response": response_text, parse_error: True}                

    def _validate_response(self, response, required_fields):
        """Validate that response contains required fields."""
        return all(field in response for field in required_fields)