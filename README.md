# Smart Ants

This project demonstrates a genetic algorithm applied to a pathfinding problem. In this simulation, a population of "ants" evolves over time, learning to reach a red target while avoiding obstacles. Each ant is controlled by a "brain" that stores a series of random movements. Through evolution and mutation, the ants improve their ability to find the shortest path to the goal.

## Project Overview

The project visualizes how a genetic algorithm can be used for solving pathfinding problems. The ants start at a spawn point and aim to reach a target, learning from their ancestors' movements. The genetic algorithm ensures that over successive generations, the ants become more adept at reaching the goal.

### Key Features
- **Genetic Algorithm**: The ants evolve over time through mutation and selection based on their fitness.
- **Obstacle Avoidance**: Ants must navigate a grid with walls and avoid obstacles to reach the target.
- **Fitness Function**: Ants are scored based on their proximity to the target and the number of steps taken to reach it.
- **Random Mutations**: Each generation introduces random mutations to improve the ants' pathfinding abilities.

## Genetic Algorithm

The genetic algorithm is the core of this project. Each ant is controlled by a "brain" that contains a set of moves, which are initially random. Over successive generations:
- **Selection**: Ants that perform better (get closer to the target) are selected for the next generation.
- **Mutation**: Some ants' brains are randomly mutated, leading to new paths being discovered.
- **Crossover**: The best-performing ants influence the next generation, combining their "genes" to produce offspring with similar or improved performance.

The algorithm allows for optimization, with each generation of ants getting closer to reaching the goal efficiently.

## Controls

- Press `SPACE` to hide the simulation display and speed up the evolution process.
- Press `P` to pause the simulation.
- Press `S` to save the current population to a file.
