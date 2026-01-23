from abc import ABC, abstractmethod

class Tool(ABC):
    name: str
    description: str
    input_schema: dict

    @abstractmethod
    def run(self, inputs: dict) -> dict:
        pass
        