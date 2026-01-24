class ScienceOrchestrator:

    def __init__(self, agents, memory):
        self.agents = agents
        self.memory = memory

    def run(self, problem, max_iters=5):
        context = {'problem': problem}
        
        for i in range(max_iters):
            h = self.agents['hypothesis'].run(context)
            p = self.agents['planner'].run(h)
            e = self.agents['executor'].run(p)
            a = self.agents['analyzer'].run(e)
            c = self.agents['critic'].run({
                'hypothesis': h,
                'analysis': a
                })

            self.memory_log({
                'iteration': i,
                'hypothesis': h,
                'plan': p,
                'execution': e,
                'analysis': a,
                'critic': c
                })

            if not c['continue']:
                break

