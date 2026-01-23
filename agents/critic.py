class CriticAgent(Agent):

    def run(self, full_context):
        prompt = f"""
        Act as a harsh peep reviewer:

        Identify:
        - Methodical flaws
        - alternative explanations
        - overfitting or bias
        - suggestions for next experiments
        """

        return self.llm.generate(prompt, temperature=0.4)
        