"""
Test script for the project
"""

import sys
import os

def test_llm_backend():
    """Test LLM Backend connection"""
    print("Testing LLM Backend Connection...")
    try:
        from core.llm import LLMBackend
        llm = LLMBackend('deepseek-r1:1.5b')

        # Test connection
        if hasattr(llm, 'test_connection'):
            connected = llm.test_connection()
            print(f"Connection Test: {'PASS' if connected else 'FAIL'}")

        # Test generation
        result = llm.generate('What is 2+2?', temperature = 0.1)
        print("Generation test pass!")
        print(f"Sample Response: {result['text'][:100]}...")

        return True

    except Exception as e:
        print(f"LLM Backend connection failed: {e}")
        return False

def test_memory_system():
    """Test Memory System"""
    print("Testing Memory System...")
    
    try:
        from core.memory import ExperimentMemory
        memory = ExperimentMemory("test_experiments")

        # Test experiment lifecycle
        exp_id = memory.start_experiment("Test problem")
        print(f"Experiment started: {exp_id}")

        memory.log_iteration({
            'hypothesis': {'text': 'test_hypothesis'},
            'planner': {'text': 'test_plan'},
            'excutor': {'text': 'test_execution'},
            'analyzer': {'text': 'test_analyzer'},
            'critic': {'continue': True},
        })
        print('Iteration logged')

        memory.end_experiment("Completed")
        print("Experiment ended")

        # Test Retrieval
        experiment = memory.get_experiment(exp_id)
        print(f"Experiment Retrieved: {experiment is not None}")

        return True

    except Exception as e:
        print(f"Memory Test System failed: {e}")
        return False

def test_tools():
    """Test tool systems"""
    print("Testing Tools...")
    try:
        from tools.symbolic_math import execute_symbolic_math
        from tools.physics_simulator import execute_physics_simulations

        # Test symbolic math
        result = execute_symoblic_math('simplify', expression = 'x**2 + 2*x + 1')
        print(f"Symbolic Math result: {'PASS' if result['success'] else 'FAIL'}")
        
        # Test physics simulator
        result = execute_physics_simulations('free_fall', initial_height = 10)
        print(f"Physics Simulation result: {'PASS' if result['success'] else 'FAIL'}")

        return True
    
    except Exception as e:
        print(f'Testing tool systems failed: {e}')
        return False

def test_agents():
    """Test agent initialization"""
    print('Testing agents...')

    try:
        from core.llm import LLMBackend
        from core.agenst import hypothesis, planner, analyzer, critic, executor

        llm = LLMBackend('deepseek-r1:1.5b')

        # Test agent creation
        agents = {
            'hypothesis': hypothesis.HypothesisAgent("H", "llm"),
            'planner': planner.PlannerAgent('P', 'llm'),
            'executor': executor.ExecutorAgent('E', 'llm'),
            'analyzer': analyzer.AnalyzerAgent('A', 'llm'),
            'critic': critic.CriticAgent('C', 'llm')
        }
        print("All agents created successfully!")

        # Test hypothesis agent with simple input
        result = agents['hypothesis'].run({'problem': 'Test problem'})
        print(f"Hypothesis Agent Test: {'PASS' if 'hypothesis' in result else 'FAIL'}")

        return True

    except Exception as e:
        print("Agent test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("AgenticLab Test Suite")
    
    tests = [
        test_llm_backend,
        test_memory_system,
        test_tools,
        test_agents
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    print(f"Test Results: {sum(results)}/{len(results)} passed")
    
    if all(results):
        print("All tests passed! System is ready.")
        return 0
    else:
        print("Some tests failed. Check the errors above.")
        return 1
 
if __name__ == "__main__":
    sys.exit(main())