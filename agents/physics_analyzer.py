import numpy as np

class PhysicsAnalyzer:
    def run(self, sim_output):
        energies = np.array(sim_output[0]['output']['energies'])
        drift = abs(energies[-1] - energies[0])

        return {
            'energy_drift': float(drift),
            'conserved': drift < 1e-2
        }
        