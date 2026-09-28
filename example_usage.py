from client import ParticleSwarmOptimizer

def main():
    pso = ParticleSwarmOptimizer(dimensions=2, num_particles=25)
    # Sphere function f(x, y) = x^2 + y^2
    res = pso.optimize(lambda p: p[0]**2 + p[1]**2, bounds=(-5.0, 5.0), max_iter=40)
    print("Particle Swarm Optimization Verification:")
    print(f"Optimal Cost: {res['best_cost']}")
    print(f"Optimal Position: {res['best_position']}")

if __name__ == "__main__":
    main()
