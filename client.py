"""Particle Swarm Optimization (PSO) Engine
100% Python Standard Library (random).
"""

import random

class ParticleSwarmOptimizer:
    """Continuous space swarm intelligence optimizer."""
    def __init__(self, dimensions=2, num_particles=20, w=0.7, c1=1.5, c2=1.5):
        self.dims = dimensions
        self.num_particles = num_particles
        self.w = w
        self.c1 = c1
        self.c2 = c2

    def optimize(self, cost_fn, bounds=(-5.0, 5.0), max_iter=50):
        lb, ub = bounds
        particles = [[random.uniform(lb, ub) for _ in range(self.dims)] for _ in range(self.num_particles)]
        velocities = [[random.uniform(-1.0, 1.0) for _ in range(self.dims)] for _ in range(self.num_particles)]
        pbest = [list(p) for p in particles]
        pbest_cost = [cost_fn(p) for p in particles]

        gbest_idx = min(range(self.num_particles), key=lambda i: pbest_cost[i])
        gbest = list(pbest[gbest_idx])
        gbest_cost = pbest_cost[gbest_idx]

        for _ in range(max_iter):
            for i in range(self.num_particles):
                for d in range(self.dims):
                    r1 = random.random()
                    r2 = random.random()
                    velocities[i][d] = (self.w * velocities[i][d] +
                                        self.c1 * r1 * (pbest[i][d] - particles[i][d]) +
                                        self.c2 * r2 * (gbest[d] - particles[i][d]))
                    particles[i][d] += velocities[i][d]
                    particles[i][d] = min(ub, max(lb, particles[i][d]))

                cost = cost_fn(particles[i])
                if cost < pbest_cost[i]:
                    pbest_cost[i] = cost
                    pbest[i] = list(particles[i])
                    if cost < gbest_cost:
                        gbest_cost = cost
                        gbest = list(particles[i])

        return {
            "best_cost": round(gbest_cost, 6),
            "best_position": [round(x, 4) for x in gbest]
        }
