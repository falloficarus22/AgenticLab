#!/usr/bin/env python3
"""
Example: Prime Gaps Analysis Experiment
"""

from core.orchestrator import ScienceOrchestrator
from core.memory import ExperimentMemory
from core.llm import LLMBackend
from agents import hypothesis, planner, executor, analyzer, critic

def run_prime_gap_experiment():
    """Run experiment on prime gaps"""
    
    # Initialize system
    llm = LLMBackend('deepseek-r1:1.5b')
    memory = ExperimentMemory()
    
    agents = {
        'hypothesis': hypothesis.HypothesisAgent("H", llm),
        'planner': planner.PlannerAgent('P', llm),
        'executor': executor.ExecutorAgent('E', llm),
        'analyzer': analyzer.AnalyzerAgent('A', llm),
        'critic': critic.CriticAgent('C', llm)
    }
    
    orchestrator = ScienceOrchestrator(agents, memory)
    
    # Run experiment
    problem = "Analyze the distribution of prime gaps and formulate a conjecture about their patterns"
    
    result = orchestrator.run(problem, max_iters=3)
    
    print(f"Experiment completed: {result['experiment_id']}")
    print(f"Total iterations: {result['total_iterations']}")
    print(f"Final status: {result['final_status']}")
    
    return result

if __name__ == "__main__":
    run_prime_gap_experiment()
    