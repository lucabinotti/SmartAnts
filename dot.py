from brain import Brain


class Dot:
    def __init__(self, position: list, brain_size: int, brain: Brain = None):
        self.brain_size = brain_size
        self.brain = Brain(size=brain_size) if brain is None else brain
        self.start_position = position.copy()
        self.position = position.copy()
        self.alive = True
        self.reached_target = False
        self.is_best = False
        self.fitness = 0

    def kill(self):
        self.alive = False

    def move(self):
        self.position[0] += self.brain.moves[self.brain.step][0]
        self.position[1] += self.brain.moves[self.brain.step][1]
        self.brain.step += 1

    def calculate_fitness(self, goal_pos: list):
        if self.reached_target:
            self.fitness = 1000.0 / self.brain.step
        else:
            self.fitness = 1.0 / ((self.position[0] - goal_pos[0]) ** 2 + (self.position[1] - goal_pos[1]) ** 2)

    def get_child(self):
        child_brain = self.brain.clone()
        child_brain.mutate()
        return Dot(position=self.start_position, brain_size=self.brain_size, brain=child_brain)
