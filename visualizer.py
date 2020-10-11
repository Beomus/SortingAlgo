import algo
import time
import sys
import pygame

WIDTH = 1024
HEIGHT = 512

pygame.init()

ALGORITHMS = {
    'SelectionSort': algo.SelectionSort(),
    'BubbleSort': algo.BubbleSort(),
    'InsertionSort': algo.InsertionSort(),
    'MergeSort': algo.MergeSort(),
    'QuickSort': algo.QuickSort()
}

class Visualizer:
    def __init__(self):
        # init for pygame
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.win.fill(pygame.Color("#a48be0"))
        self.clock = pygame.time.Clock()

        # init for visualizer
        self.running = True
        self.algorithms = ALGORITHMS
        self.state = 'main'

        # TODO: add all buttons here
        ##############################################
        # button for Selection
        self.selection_button = None
        # button for Bubble
        self.bubble_button = None
        # button for Insertion
        self.insertion_button = None
        # button for Merge
        self.merge_button = None
        # button for Quick
        self.quick_button = None
        ##############################################

    def run(self):
        while self.running:
            if self.state == 'main':
                self.main_events()
            elif self.state == 'visualizing':
                self.visualize()
            elif self.state == 'aftermath':
                self.reset()
        pygame.quit()
        sys.exit()

    def main_events(self):
        self.win.update()
        pygame.display.update()
        self.draw_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.selection_button.isOver(pos):
                    self.visualize()
                    self.state = 'visualizing'
                elif self.bubble_button.isOver(pos):
                    self.visualize()
                    self.state = 'visualizing'
                elif self.insertion_button.isOver(pos):
                    self.visualize()
                    self.state = 'visualizing'
                elif self.merge_button.isOver(pos):
                    self.visualize()
                    self.state = 'visualizing'
                elif self.quick_button.isOver(pos):
                    self.visualize()
                    self.state = 'visualizing'
            
            # TODO: change button colors
            if event.type == pygame.MOUSEMOTION:
                if self.selection_button.isOver(pos):
                    self.selection_button.color = None
                elif self.bubble_button.isOver(pos):
                    self.bubble_button.color = None
                elif self.insertion_button.isOver(pos):
                    self.insertion_button.color = None
                elif self.merge_button.isOver(pos):
                    self.merge_button.color = None
                elif self.quick_button.isOver(pos):
                    self.quick_button.color = None
                else:
                    self.set_buttons_color(None)

    # TODO: write draw_text method
    def draw_text(self):
        pass

    # TODO: write draw_text method
    def visualize(self):
        pass

    # TODO: write set_buttons_color method
    def set_buttons_color(self, color):
        pass

    def update(self, algorithm, swap1=None, swap2=None):
        self.win.fill(pygame.Color("#a48be0"))
        pygame.display.set_caption(f'SAV: {algorithm.name} | {time.time() - algorithm.start_time} | Sorting...')
        k = int(WIDTH / len(algorithm.array))
        for i in range(len(algorithm.array)):
            color = (80, 0, 255)
            if swap1 == algorithm.array[i]:
                color = (0, 255, 0)
            elif swap2 == algorithm.array[i]:
                color = (255, 0, 0)

            pygame.draw.rect(self.win, color, (i * k, HEIGHT, k, -algorithm.array[i]))
        check_events()
        pygame.display.update()

win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill(pygame.Color("#a48be0"))


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()





def keep_open(algorithm, t, display=win):
    pygame.display.set_caption(f'SAV: {algorithm.name} | {t} | Done!')
    while True:
        check_events()


def main(args):
    if len(args) < 2:
        print("Select a sorting algorithm")
    elif args[1] == "list":
        print("Available algorithms:\n\t" + "\n\t".join(algorithms.keys()))
        sys.exit(0)
    else:
        algorithm = algorithms[args[1]]
        _, time_elapsed = algorithm.run()
        keep_open(algorithm, time_elapsed)


if __name__ == '__main__':
    sys.argv.append('MergeSort')
    main(sys.argv)
