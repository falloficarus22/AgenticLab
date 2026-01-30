from core.agent import Agent

class HypothesisAgent(Agent):

    def run(self, context):
        problem = context.get('problem', '')
        previous_analysis = context.get('previous_analysis', {})
        previous_critique = context.get('previous_critique', {})

        # Build context aware prompt
        context_info = ""

        if previous_analysis:
            context_info += f"\nPrevious Analysis: {preivous_analysis.get('summary', '')}"
        if previous_critique:
            context_info += f"\nPrevious Critique: {previous_critique.get('feedback', '')}"

        prompt = f"""
        You are a scientific hypothesis generator. Propose a falsifiable hypothesis based on the problem.

        Problem: {problem}
        {context_info}

        Requirements:
        1. Hypothesis must be falsifiable. (Clear testable predictions)
        2. Include specific assumptions.
        3. Define expected outcomes that can be measured.
        4. Be specific and quantitative wherever possible.
        
        Output JSON format:
        {{
            'hypothesis': 'Clear, falsifiable statement.',
            'assumptions': ['assumption1', 'assuimption2'],
            'expected_outcomes': ['measurable outcome 1', 'measurable outcome 2'],
            'falsification_criteria': 'what would prove this false?',
            'confidence_score': 0.7
        }}
        """

        response = self.llm.generate(prompt, temperature = 0.7)
        parsed = self._parse_json_response(response['text'])

        # Validate required fields
        required = ['hypothesis', 'assumptions', 'expected_outcomes', 'falsiication_criteria', 'confidence_score']

        if not self._validate_response(parsed, required):
            parsed['error']: 'Missing required fields'

        return parsed
        