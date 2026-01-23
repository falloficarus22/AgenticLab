class MLExperiment:
    name = 'ml_experiment'

    def can_handle(self, plan):
        return 'train' in str(plan).lower()

    def run(self, plan):
        return {'accuracy': 0.91, 'loss_curve': [...]}
        