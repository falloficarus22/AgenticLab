class PlannerAgent(Agent):

    def run(self, hypothesis):
        prompt = f"""
        Design an experiment to test this hypothesis:
        {hypothesis}

        Specify:
        - variables
        - controls
        - metrics
        - execution_steps
        """

        return self.llm.generate(prompt, temperature=0.3)