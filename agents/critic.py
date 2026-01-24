class CriticAgent(Agent):

    def run(self, context):
        analysis = context['analysis']

        if 'does NOT' in str(analysis):
            return {
                'fatal_flaw': True,
                'reason': 'Hypothesis disproven symbolically.',
                'continue': False
            }
        
        return {
            'fatal_flaw': False,
            'reason': 'No immediate logical flaws',
            'continue': True
        }
        