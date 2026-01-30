from core.agent import Agent

class PlannerAgent(Agent):

    def run(self, hypothesis_data):
        hypothesis = hypothesis_data.get('hypothesis', '')
        expected_outcomes = hypothesis_data.get('expected_outcomes', [])

        prompt = f"""
        You are an experimental planner. Design a concrete experiment to test the hypothesis.
        

        Hypothesis: {hypothesis}
        Expected Outcomes: {expected_outcomes}

        Avalaible tools:
        - symbolic_math: For mathematical proofs and calculations.
        - physics_simulator: For physics simulations.
        - data_analyzer: For statistical analysis.

        Design and experiment plan that:
        1. Specifies exact steps to take.
        2. Selects appropriate tool.
        3. Defines success/failure criteria.
        4. Includes measurable metrics.

        Output JSON format:
        {{
            'experiment_type': 'mathematical | simulation | analytical',
            'steps': ['step 1 description', 'step 2 description'],
            'tools_required': ['tool1', 'tool2'],
            'success_metrics': ['metric1', 'metric2'],
            'failure_criteria': ['what indicates failure'],
            'estimated_duration': 'short | medium | long'
        }}
        """

        response = self.llm.generate(prompt, temperature = 0.3)
        parsed = self._parse_json_response(response['text'])

        required = ['experiment_type', 'steps', 'tools_required', 'success_metrics', 'failure_criteria', 'estimated_duration']

        if not self._validate_response(response, required_fields):
            parsed['error'] = "Missing reqiured fields"

        return parsed
        