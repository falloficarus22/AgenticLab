class ExecutorAgent(Agent):

    def __init__(self, tools):
        self.tools = {t.name: t for t in tools}
    
    def run(self, plan):
        results = []

        for step in plan['execution_steps']:
            tool_call = step.get('tool_call')

            if not tool_call:
                continue
            
            tool = self.tools.get(tool_call['name'])

            if tools is None:
                raise ValueError(f"Unknown tool: {tool_call['name']}")

            output = tool.run(tool_call['inputs'])
            results.append({
                'tool': tool_call['name'],
                'inputs': tool_call['inputs'],
                'output': output
            })

        return results
