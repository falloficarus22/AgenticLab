class ExecutorAgent(Agent):
    
    def run(self, plan):
        results = {}
        for tool in self.tools:
            if tool.can_handle(plan):
                results[tool.name] = tool.run(plan)

        return results
