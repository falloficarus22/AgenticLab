from core.llm import LLMBackend
from core.memory import ExperimentMemory
from core.orchestrator import ScienceOrchestrator

from agents import hypothesis, planner, executor, analyzer, critic
from domains.math.tools import SymbolicSolver

llm_backend = LLMBackend('local-llm')
memory = ExperimentMemory

agents = {
    'hypothesis': hypothesis.HypothesisAgent("H", llm),
    'planner': planner.PlannerAgent('P', llm),
    'executor': executor.ExecutorAgent('E', llm),
    'analyzer': analyzer.AnayzerAgent('A', llm),
    'critic': crictic.CriticAgent('C', llm)
}

lab = ScienceOrchestrator(agents, memory)

lab.run('Find a conjecture about prime gaps')
