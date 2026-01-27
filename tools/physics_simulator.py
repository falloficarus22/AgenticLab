import numpy as np
from core.tools import Tool

class HarmonicOscillatorSim(Tool):
    name = 'harmmonic_oscillator'
    description = "Simulates x'' + kx = 0 using Euler Integration"

    input_schema = {
            'k': 'float',
            'x0': 'float',
            'v0': 'float',
            'dt': 'float',
            'steps': 'int'
            }

    def run(self, inputs):
        k = inputs['k']
        x = inputs['x0']
        v = inputs['v0']
        dt = inputs['dt']
        steps = inputs['steps']

        xs, vs, energies = [], [], []

        for _ in range(steps):
            a = -k * x
            v = v + a * dt
            x = x + v * dt

            energy = 0.5 * v**2 + 0.5 * k * x**2
            xs.append(x)
            vs.append(v)

            energies.append(energy)

        return {
                'positions': xs,
                'velocities': vs,
                'energies': energies
                }
