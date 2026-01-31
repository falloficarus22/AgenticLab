class Agent:

    def __init__(self, name, llm, tools=None):
        self.name = name
        self.llm = llm
        self.tools = tools or []

    def run(self, input_data):
        raise NotImplementedError