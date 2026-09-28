# genpark-particle-swarm-optimization-pso-skill

> Continuous domain Particle Swarm Optimization (PSO) with inertia weight decay and cognitive/social acceleration.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[Initial Candidate Population] --> B[Evolutionary Selection & Variation]
    B --> C[Metaheuristic Swarm Optimization]
    C --> D[Optimal Global Solution]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`math`, `random`).
- **Robust Metaheuristics**: Genetic crossover/mutation, PSO swarm velocity, simulated annealing Metropolis criterion, and ACO stigmergy.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-particle-swarm-optimization-pso-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-particle-swarm-optimization-pso-skill.git
cd genpark-particle-swarm-optimization-pso-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-particle-swarm-optimization-pso-skill": {
      "command": "python",
      "args": ["-m", "genpark-particle-swarm-optimization-pso-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
