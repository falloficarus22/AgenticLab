class ScienceOrchestrator:

    def __init__(self, agents, memory):
        self.agents = agents
        self.memory = memory

    def run(self, problem, max_iters=5):
        # Start experiment tracking
        experiment_id = self.memory.start_experiment(problem)
        print(f'Started experiment: {experiment_id}')
        print(f"Problem: {problem}")

        context = {'problem': problem}
        
        for i in range(max_iters):
            print(f"\n---Iteration {i + 1}/{max_iters} ---")

            try:
                # Execute the scientific method cycle
                h = self.agents['hypothesis'].run(context)
                print('Hypothesis generated.')

                p = self.agents['planner'].run(h)
                print('Plan created.')

                e = self.agents['executor'].run(p)
                print('Execution completed.')

                a = self.agents['analyzer'].run(e)
                print('Analysis finished.')

                c = self.agents['critic'].run({
                    'hypothesis': h,
                    'analysis': a
                    })
                print('Critique completed.')

                # Log the complete iteration
                iteration_data = {
                    'hypothesis': h,
                    'planner': p,
                    'executor': e,
                    'analyzer': a,
                    'critic': c
                }

                self.memory.log_iteration(iteration_data)

                # Check if critic recommends stopping
                if not c.get('continue', True):
                    print('Critic recommends stopping the experiment.')
                    self.memory.end_experiment('stopped_by_critic')
                    break
                
                # Update context for the next iteration
                context.update({
                    'previous_hypothesis': h,
                    'previous_analysis': a,
                    'previous_critic': c
                })

            except Exception as e:
                print(f"Error in iteration {i + 1}: {str(ex)}")
                self.memory.end_experiment(f"error in iteration {i + 1}")
                raise

        else:
            # Comepleted all iterations
            print(f"Completed {max_iters} iterations")
            self.memory.end_experiment("completed_all_iterations")
        
        # Return final results
        final_experiment = self.memory.get_experiment(experiment_id)
        return {
            'experiment_id': experiment_id,
            'total_iterations': len(final_experiment.get('iterations', [])),
            'final_status': final_experiment.get('status'),
            'summary': final_experiment
        }
        