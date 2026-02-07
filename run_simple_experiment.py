#!/usr/bin/env python3
"""
Simple test experiment to verify MASL system works
"""

from core.orchestrator import ScienceOrchestrator
from core.memory import ExperimentMemory
from core.llm import LLMBackend
from agents import hypothesis, planner, executor, analyzer, critic

def run_simple_experiment():
    """Run a simple mathematical experiment"""
    
    print("Starting MASL Simple Experiment")
    print("=" * 50)
    
    # Initialize system
    print("Initializing LLM backend...")
    llm = LLMBackend('deepseek-r1:1.5b')
    
    print("Initializing memory system...")
    memory = ExperimentMemory()
    
    print("Initializing agents...")
    agents = {
        'hypothesis': hypothesis.HypothesisAgent("H", llm),
        'planner': planner.PlannerAgent('P', llm),
        'executor': executor.ExecutorAgent('E', llm),
        'analyzer': analyzer.AnalyzerAgent('A', llm),
        'critic': critic.CriticAgent('C', llm)
    }
    
    print("Initializing orchestrator...")
    orchestrator = ScienceOrchestrator(agents, memory)
    
    # Run a simple experiment
    problem = "Test if the sum of first n natural numbers equals n(n+1)/2"
    
    print(f"\nRunning experiment: {problem}")
    print("-" * 50)
    
    try:
        result = orchestrator.run(problem, max_iters=2)
        
        print(f"\nExperiment completed!")
        print(f"Experiment ID: {result['experiment_id']}")
        print(f"Total iterations: {result['total_iterations']}")
        print(f"Final status: {result['final_status']}")
        
        return result['experiment_id']
        
    except Exception as e:
        print(f"Experiment failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    experiment_id = run_simple_experiment()
    
    if experiment_id:
        print(f"\nTo visualize results, run:")
        print(f"python visualize_experiment.py {experiment_id}")
    else:
        print("\nExperiment failed - check the errors above")
