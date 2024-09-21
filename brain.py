import random


class Brain:
    """
    The brain of a single dot.
    """
    def __init__(self, size: int, moves: list = []):
        self.step = 0
        self.size = size
        self.moves = moves.copy()
        if not self.moves:
            self.randomize()

    @staticmethod
    def random_move():
        """
        Generate one single random move.
        """
        return [random.randint(-5, 5), random.randint(-5, 5)]

    def randomize(self):
        """
        Generate random moves.
        """
        for _ in range(0, self.size):
            self.moves.append(self.random_move())

    def mutate(self):
        """
        Mutate the brain, so that the child's brain will be
        slightly different than the one of the parent.

        >> mutation_rate = 0.01 --> 1% of brain will be mutated randomly
        """
        mutation_rate = 0.01
        for i in range(0, self.size):
            if random.uniform(0, 1) < mutation_rate:
                self.moves[i] = self.random_move()

    def clone(self):
        """
        Clone this brain for a child.
        """
        return Brain(size=self.size, moves=self.moves)

