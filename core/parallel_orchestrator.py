import asyncio
from concurrent.futures import ThreadPoolExecutor
from core.orchestrator import ScienceOrchestrator

class ParallelOrchestrator(ScienceOrchestrator):
    """Enhanced orchestrator with parallel execution capabilities"""

    def __init__(self, agents, memory, max_workers = 3):
        super().__init__(agents, memory)
        self.max_workers = max_workers
    async def run_parallel_experiments(self, problems, max_iters):
        """Run a single experiment asynchronously"""
        loop = asyncio.get_event_loop()

        with ThreadPoolExecutor(max_workers = 1) as executor:
            result = await loop.run_in_executor(
                executor, self.run, problem, max_iters
            )

        return result

    def batch_hypothesis_generation(self, problems):
        """Generate hypotheses for multiple problems in parallel"""
        with ThreadPoolExecutor(max_workers = self.max_workers) as executor:
            contexts = [{'problem': problem} for problem in problems]
            hypotheses = list(executor.map(
                self.agents['hypothesis'].run, contetxs
            ))

        return hypotheses
        