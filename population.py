import random
from dot import Dot


class Population:
    def __init__(self, size: int, target: list, spawn_pos: list, max_step: int, borders: tuple, border_size: int, walls: list, random_population: bool = True):
        self.step = 0
        self.size = size
        self.target = target
        self.spawn_pos = spawn_pos.copy()
        self.max_step = max_step
        self.borders = borders
        self.population = []
        self.reached = False
        self.all_dead = False
        self.border_size = border_size
        self.walls = walls
        if random_population:
            self.populate()

    def populate(self):
        for _ in range(0, self.size):
            self.population.append(Dot(position=self.spawn_pos, brain_size=self.max_step))

    @staticmethod
    def collide(position: list, rect: list) -> bool:
        return rect[0] <= position[0] <= rect[0] + rect[2] and rect[1] <= position[1] <= rect[1] + rect[3]

    def next_step(self):
        all_dead = True
        for i, dot in enumerate(self.population):
            if dot.alive and not dot.reached_target:
                dot.move()

                # Reached the target
                if (dot.position[0] - self.target[0]) ** 2 + (dot.position[1] - self.target[1]) ** 2 <= 49:
                    dot.reached_target = True
                    if not self.reached:
                        dot.is_best = True
                        self.reached = True

                # Die touching borders
                elif dot.position[0] < self.borders[0] + self.border_size or dot.position[1] < self.borders[1] + self.border_size or dot.position[0] > self.borders[2] - self.border_size or dot.position[1] > self.borders[3] - self.border_size:
                    dot.kill()

                # Die touching walls
                elif True in [self.collide(position=dot.position, rect=rect) for rect in self.walls]:
                    dot.kill()

                else:
                    all_dead = False
        self.all_dead = all_dead
        self.step += 1

    def get_next_generation(self):

        best_fitness = 0
        best_dot = -1
        for d, dot in enumerate(self.population):
            dot.calculate_fitness(self.target)
            dot.is_best = False
            if dot.fitness > best_fitness:
                best_fitness = dot.fitness
                best_dot = d
        self.population[best_dot].is_best = True

        next_population = Population(size=self.size, spawn_pos=self.spawn_pos, target=self.target, max_step=self.max_step, borders=self.borders, border_size=self.border_size, walls=self.walls, random_population=False)

        clone_best = self.population[best_dot]
        clone_best.alive = True
        clone_best.reached_target = False
        clone_best.is_best = True
        clone_best.position = self.spawn_pos
        clone_best.brain.step = 0

        next_population.population.append(self.population[best_dot])

        total_fitness = 0
        for dot in self.population:
            total_fitness += dot.fitness

        probabilities = []
        for d, dot in enumerate(self.population):
            if d == 0:
                probabilities.append(dot.fitness / total_fitness)
            elif d == len(self.population) - 1:
                probabilities.append(1)
            else:
                probabilities.append(probabilities[d - 1] + dot.fitness / total_fitness)

        for _ in range(0, self.size - 1):

            choice = random.uniform(0, 1)
            choiced_dot = None
            for i, p in enumerate(probabilities):
                if i == 0:
                    if choice < probabilities[0]:
                        choiced_dot = self.population[i]
                        break
                else:
                    if probabilities[i - 1] <= choice < probabilities[i]:
                        choiced_dot = self.population[i]
                        break

            next_population.population.append(choiced_dot.get_child())

        return next_population
