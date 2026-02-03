import numpy as np
import math

class PhysicsSimulator:
    
    def __init__(self):
        self.constants = {
            'g': 9.81,
            'c': 299792458,
            'G': 6.6743e-11,
            'k': 8.99e9,
            'h': 6.62607015e-34
        }

    def projectile_motion(self, initial_velocity, angle, initial_height = 0, time_step = 0.01):
        """Simulate projectile motion."""
        try:
            # Convert angle to radians
            angle_rad = math.radians(angle)
            vx = initial_velocity * math.cos(angle_rad)
            vy = initial_velocity * math.sin(angle_rad)

            # Simulation arrays
            times = []
            positions_x = []
            positions_y = []
            velocities_x = []
            velocities_y = []
            
            # Initial conditions
            t = 0
            x = 0
            y = initial_height

            while y >= 0:
                times.append(t)
                postions_x.append(x)
                postions_y.append(y)
                velocities_x.append(vx)
                velocities_y.append(vy)

                # Update velocities (only y changes due to gravity)
                vy_new = vy - self.constants['g'] * time_step

                # Update position
                x_new = x + vx * time_step
                y_new = y + vy * time_step

                x, y, vy = x_new, y_new, vy_new
                t += time_step

                # Prevent infinite loops
                if t > 100:
                    break

            # Calculate key metrics
            max_height = max(positions_y)
            range_distance = max(positions_x)
            flight_time = times[-1]

            return {
                'success': True,

                'trajectory': {
                    'times': times,
                    'x_positions': x_positions,
                    'y_positions': y_positions,
                    'x_velocities': velocities_x,
                    'y_velocities': velocities_y
                },

                'metrics': {
                    'max_height': max_height,
                    'range_distance': range_distance,
                    'flight_time': flight_time,
                    'impact_velocity': math.sqrt(velocities_x[-1]**2 + veloxities_y[-1]**2)
                },

                'parameters': {
                    'initial_velocity': initial_velocity,
                    'angle': angle,
                    'initial_height': initial_height
                }
            }

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def pendulum_motion(self, length, initial_angle, mass = 1.0, damping = 0.0, time_step = 0.01, duration = 10.0):
        """Simulate pendulum motion."""
        try:
            # Initial conditions
            theta = math.radians(initial_angle)
            omega = 0.0 # angular velocity

            times = []
            angles = []
            angular_velocities = []
            energies = []

            t = 0

            while t < duration:
                times.append(t)
                angles.append(math.degrees(theta))
                angular_velocities.append(omega)

                # Calculate energy
                kinetic_energy = 0.5 * mass * (length * omega)**2
                potential_energy = mass * self.constants['g'] * length * (1 - math.cos(theta))
                total_energy = kinetic_energy + potential_energy
                energies.append(total_energy)

                # Update using Euler method
                alpha = -(self.constants['g'] / length) * math.sin(theta) - damping * omega
                omega_new = omega + alpha * time_step
                theta_new = theta + omega * time_step

                theta, omega = theta_new, omega_new
                t += time_step

            return {
                'success': True,

                'motion': {
                    'times': times,
                    'angles': angles,
                    'angular_velocities': angluar_velocities,
                    'energies': energies
                },

                'parameters': {
                    'length': length,
                    'initial_angle': initial_angle,
                    'mass': mass,
                    'damping': damping
                },

                'analysis': {
                    'period': self._estimate_period(times, angles),
                    'max_angle': max(angles),
                    'min_angle': min(angles),
                    'energy_conservation': (max(energies) - min(energies) / max(energies))
                }
            }

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def free_fall(self, intital_height, initial_velocity = 0, mass = 1.0, air_resistance = False):
        """Simulate free fall with optional air resistance."""
        try:
            times = []
            positions = []
            velocities = []
            accelerations = []

            t = 0
            y = initial_height
            v = initial_velocity

            while y > 0:
                times.append(t)
                postions.append(y)
                velocities.append(v)

                # Calculate acceleration
                if air_resistance:
                    # Simple linear air resistance model
                    drag_coeff = 0.47 # sphere
                    air_density = 1.225 # kg/m^3
                    radius = 0.1 # m
                    cross_section = math.pi * radius**2

                    drag_force = 0.5 * air_density * v**2 * drag_coeff * cross_section
                    drag_acceleration = drag_force / mass if v > 0 else -drag_force / mass
                    a = -self.constants['g'] + drag_acceleration

                else:
                    a = -self.constants['g']

                accelerations.append(a)

                # Update state
                dt = 0.01
                v_new = v + a * dt
                y_new = y + v * dt

                v, y = v_new, y_new
                t += dt

                if t > 100:
                    break
            return {
                'success': True,

                'trajectory': {
                    'times': times,
                    'positions': positions,
                    'velocities': velocities,
                    'accelerations': accelerations
                },

                'metrics': {
                    'fall_time': times[-1],
                    'impact_velocity': abs(velocities[-1]),
                    'max_velocity' : abs(max(velocities))
                }

                'parameters': {
                    'initial_height': initial_height,
                    'initial_velocity': initial_velocity,
                    'mass': mass,
                    'air_resistance': air_resistance
                }
            }

        except Exception as e:
            return {'success': False, 'error': str(e)}

    def _estimate_period(self, times, angles):
        """Estimate period from oscillation data."""
        try:
            # Find peaks (simple approach)
            peaks = []

            for i in range(1, len(angles) - 1):
                if angles[i] > angles[i - 1] and angles[i] > angles [i + 1]:
                    peaks.append(times[i])

            if len(peaks) >= 2:
                return 2 * (peaks[-1] - peaks[0]) / (len(peaks) - 1)

            else:
                return 0.0

        except:
            return 0.0

# Tool interface for agents
def execute_physics_simulations(operation, **kwargs):
    """Interface for agents to use physics simulation tools."""
    simulator = PhysicsSimulator()

    operations = {
        'projectile': simulator.projectile_motion,
        'pendulum': simulator.pendulum,
        'free_fall': simulator.free_fall
    }

    if operation not in operations:
        return {'success': False, 'error': f"Unknown operation: {operation}"}

    return operations[operation](**kwargs)
    