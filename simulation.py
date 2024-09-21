import sys
import time
import pygame
import pickle
from pygame.locals import *
from population import Population

pygame.init()


class Simulation:
    def __init__(self, simulation_display: list, walls: list, target: list, dot_life: int, spawn: list, population_size: int):
        self.simulation_display = simulation_display
        self.walls = walls
        self.info_display = 100
        self.target: list = target
        self.dot_life: int = dot_life
        self.spawn: list = spawn
        self.population_size = population_size
        self.enable_display: bool = True
        self.pause: bool = False
        self.fps: int = 120
        self.font = pygame.font.Font(size=50)
        self.generation: int = 0
        self.current_population: Population = Population(size=self.population_size, target=self.target, max_step=self.dot_life, spawn_pos=self.spawn, borders=(0, 0, 800, 800), border_size=3, walls=self.walls)
        self.screen = None
        self.clock = None
        self.step_for_target = self.dot_life

        self.init_display()
        self.loop()

    def init_display(self):
        pygame.display.set_caption("Smart Ants Simulation")
        self.screen = pygame.display.set_mode(size=(self.simulation_display[2], self.simulation_display[3] + self.info_display))
        self.clock = pygame.time.Clock()
        self.screen.fill(color=(255, 255, 255))

        self.update_info()

    def update_info(self):
        pygame.draw.line(surface=self.screen, color=(0, 0, 0), start_pos=[self.simulation_display[0], self.simulation_display[3] + 5], end_pos=[self.simulation_display[2], self.simulation_display[3] + 5], width=5)
        gen_surface = self.font.render(f"Generation: {self.generation}", False, (0, 0, 0))
        gen_w, gen_h = gen_surface.get_size()
        self.screen.blit(gen_surface, ((self.simulation_display[2] - gen_w) / 2, self.simulation_display[3] + (self.info_display / 2 - gen_h) / 2))

        step_surface = self.font.render(f"Best dot: {self.step_for_target} steps", False, (0, 0, 0))
        step_w, step_h = step_surface.get_size()
        self.screen.blit(step_surface, ((self.simulation_display[2] - step_w) / 2, self.simulation_display[3] + self.info_display / 2 + (self.info_display / 2 - step_h) / 2))

        pygame.display.update([self.simulation_display[0], self.simulation_display[3], self.simulation_display[2], self.simulation_display[3] + self.info_display])

    def loop(self):
        while 1:

            if not self.pause:
                if self.current_population.all_dead or self.current_population.step >= self.dot_life:
                    self.current_population = self.current_population.get_next_generation()
                    self.generation += 1
                    if self.enable_display:
                        self.update_info()
                else:
                    self.current_population.next_step()

                if self.enable_display:
                    self.screen.fill(color=(255, 255, 255))
                    pygame.draw.circle(surface=self.screen, color=(255, 0, 0), center=self.target, radius=7, width=0)

                    for wall in self.walls:
                        pygame.draw.rect(surface=self.screen, color=(0, 0, 255), rect=pygame.Rect(wall))

                    for dot in self.current_population.population:
                        if dot.is_best and (not dot.alive or dot.reached_target):
                            self.step_for_target = dot.brain.step
                        if dot.is_best:
                            pygame.draw.circle(surface=self.screen, color=(0, 255, 0), center=dot.position, radius=3, width=0)
                        else:
                            pygame.draw.circle(surface=self.screen, color=(0, 0, 0), center=dot.position, radius=2, width=0)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Disable display for fast evolution
                    if event.key == K_SPACE:
                        if self.enable_display:
                            self.enable_display = False
                        else:
                            self.enable_display = True
                            self.update_info()
                    # Pause the simulation
                    elif event.key == K_p:
                        self.pause = not self.pause
                    # Save the population into a file
                    elif event.key == K_s:
                        with open(f"populations/{time.strftime('%Y%m%d%H%M')}_gen{self.generation}.pickle", "wb") as f:
                            pickle.dump(self.current_population, f)
                        print(f"{time.strftime('%Y%m%d%H%M')}_gen{self.generation}.pickle saved.")

                elif event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if self.enable_display and not self.pause:
                pygame.display.update(self.simulation_display)
                self.clock.tick(self.fps)
