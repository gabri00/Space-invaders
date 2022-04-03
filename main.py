import sys
import os
import pygame
import neat

from config import *
from game import Game

def run_neural_network(config_path):
	config = neat.config.Config(
		neat.DefaultGenome,
		neat.DefaultReproduction,
		neat.DefaultSpeciesSet,
		neat.DefaultStagnation,
		config_path)

	population = neat.Population(config)
	population.add_reporter(neat.StdOutReporter(True))	# Prints the best score of the population
	population.add_reporter(neat.StatisticsReporter())	# Prints the statistics of the population

	# winner = population.run(eval_genomes, 10)	# Runs the population for 10 generations with the specified fitness function

if __name__ == '__main__':
	neat_config_path = os.path.join(os.path.dirname(__file__), 'neat_config.txt')
	run_neural_network(neat_config_path)

	pygame.init()
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	ALIENLASER = pygame.USEREVENT + 1
	pygame.time.set_timer(ALIENLASER, ALIEN_LASER_RESET_TIME)

	game = Game(window)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == ALIENLASER:
				game.alien_shoot()

		window.fill(BG_COLOR)

		game.run()

		pygame.display.flip()
		clock.tick(60)