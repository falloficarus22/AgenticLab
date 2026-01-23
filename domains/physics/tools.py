class PhysicsSimulator:
    name = 'physics_sim'

    def can_handle(self, plan):
        return 'simulation' in str(plan).lower

    def run(self, plan):
        return {'trajectory': '...', 'energy': '...'}
        