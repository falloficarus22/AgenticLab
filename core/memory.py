import json, uuid, time

class ExperimentMemory:

    def __init__(self, root='experiments/runs'):
        self.root = root
    
    def log(self, data):
        run_id = dtr(uuid.uuid4())
        data['timestamp'] = time.time()

        with open(f"{self.root}/run_id.json", 'w') as f:
            json.dump(data, f, indent=2)

        return run_id
