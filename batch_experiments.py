#!/usr/bin/env python3
"""
Run multiple experiments using templates
"""

from core.parallel_orchestrator import ParallelOrchestrator
from core.memory import ExperimentMemory
from core.llm import LLMBackend
from agents import hypothesis, planner, executor, analyzer, critic
from templates.experiment_templates import ExperimentTemplates

async def run_batch_experiments():
    """Run experiments using templates"""
    
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
    
    orchestrator = ParallelOrchestrator(agents, memory)
    
    # Get prime research template
    template = ExperimentTemplates.get_template('prime_research')
    problems = template['default_problems'][:2]  # Run first 2 problems
    
    print(f"🚀 Running {len(problems)} experiments in parallel...")
    
    # Run experiments in parallel
    results = await orchestrator.run_parallel_experiments(problems, template['max_iterations'])
    
    print(f"✅ Completed {len(results)} experiments")
    
    # Analyze results
    from core.meta_analyzer import MetaAnalyzer
    analyzer = MetaAnalyzer(memory)
    
    experiment_ids = [r.get('experiment_id') for r in results if 'experiment_id' in r]
    comparison = analyzer.compare_experiments(experiment_ids)
    
    print(f"📊 Meta-analysis completed")
    print(f"   Average success rate: {comparison['metrics']['success_rates']}")
    
    return results

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_batch_experiments())
    