#!/usr/bin/env python3
"""
Quick test to verify basic functionality
"""

def test_basic_functionality():
    """Test each component individually"""
    
    print("Quick MASL System Test")
    print("=" * 30)
    
    # Test 1: LLM Backend
    print("\n1. Testing LLM Backend...")
    try:
        from core.llm import LLMBackend
        llm = LLMBackend('deepseek-r1:1.5b')
        result = llm.generate("What is 2+2?", temperature=0.1)
        print(f"   LLM Backend: {result['text'][:50]}...")
    except Exception as e:
        print(f"   LLM Backend failed: {e}")
        return False
    
    # Test 2: Memory System
    print("\n2. Testing Memory System...")
    try:
        from core.memory import ExperimentMemory
        memory = ExperimentMemory("test_experiments")
        exp_id = memory.start_experiment("Test problem")
        memory.log_iteration({'test': 'data'})
        memory.end_experiment("completed")
        print(f"   Memory System: Experiment {exp_id} created")
    except Exception as e:
        print(f"   Memory System failed: {e}")
        return False
    
    # Test 3: Agent Creation
    print("\n3. Testing Agent Creation...")
    try:
        from agents import hypothesis, planner, executor, analyzer, critic
        
        agents = {
            'hypothesis': hypothesis.HypothesisAgent("H", llm),
            'planner': planner.PlannerAgent('P', llm),
            'executor': executor.ExecutorAgent('E', llm),
            'analyzer': analyzer.AnalyzerAgent('A', llm),
            'critic': critic.CriticAgent('C', llm)
        }
        print(f"   Agents: All 5 agents created successfully")
    except Exception as e:
        print(f"   Agent creation failed: {e}")
        return False
    
    # Test 4: Hypothesis Generation
    print("\n4. Testing Hypothesis Generation...")
    try:
        context = {'problem': 'Test if 1+1=2'}
        result = agents['hypothesis'].run(context)
        print(f"   Hypothesis: {result.get('hypothesis', 'No hypothesis')[:50]}...")
    except Exception as e:
        print(f"   Hypothesis generation failed: {e}")
        return False
    
    print(f"\nAll tests passed! System is ready.")
    return True

if __name__ == "__main__":
    success = test_basic_functionality()
    
    if success:
        print(f"\nNow run: python run_simple_experiment.py")
    else:
        print(f"\nFix the errors above before proceeding")
