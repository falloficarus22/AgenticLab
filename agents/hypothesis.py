from core.agent import Agent

class HypothesisAgent(Agent):

    def run(self, problem):
        prompt = f"""
        Propose a falsifiable scientific hypothesis.
        Problem: {problem}

        Output JSON with:
        - hypothesis
        - assumptions
        - expected_outcomes
        """

        return self.llm.generate(prompt, temperature=0.7)
        