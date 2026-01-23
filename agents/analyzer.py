class AnalyzerAgent(Agent):

    def run(self, results):
        prompt = f"""
        Analyze the following experimental results:
        {results}

        Return:
        - statistical_summary
        - interpretation
        - hypothesis_support (true/false/partial)
        """

        return self.llm.generate(prompt, temperature=0.2)
        