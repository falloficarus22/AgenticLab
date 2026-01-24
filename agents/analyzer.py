class AnalyzerAgent(Agent):

    def run(self, tool_results):
        conclusions = []

        for r in tool_results:
            if r['output']['simplified'] == '0':
                conclusions.append('Identity holds symbolically.')
            else:
                conclusions.append('Identity does NOT simplify to zero.')
        
        return {
            'conclusions': conclusions,
            'confidence': 0.9
        }