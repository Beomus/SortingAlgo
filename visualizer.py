import algo
import time
import sys
import pygame

WIDTH = 1024
HEIGHT = 512 + 100

FONT = 'Arial Black'

pygame.init()

ALGORITHMS = {
    'SelectionSort': algo.SelectionSort(),
    'BubbleSort': algo.BubbleSort(),
    'InsertionSort': algo.InsertionSort(),
    'MergeSort': algo.MergeSort(),
    'QuickSort': algo.QuickSort()
}


class Colors:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.AQUAMARINE = (127, 255, 212)
        self.BLACK = (0, 0, 0)
        self.ALICE = (240, 248, 255)
        self.STEELBLUE = (110, 123, 139)
        self.MINT = (189, 252, 201)
        self.SPRINGGREEN = (0, 255, 127)
        self.TOMATO = (255, 99, 71)
        self.ROYALBLUE = (72, 118, 255)
        self.TAN = (255, 165, 79)
        self.RED = (255, 0, 0)

colors = Colors()


class Button:
    def __init__(self, app, color, x, y, width, height, text=None):
        self.app = app
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self, outline=None):
        if outline:
            pygame.draw.rect(self.app.win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(self.app.win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text:
            font = pygame.font.SysFont(FONT, 12)
            text = font.render(self.text, 1, (0, 0, 0))
            self.app.win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                                        self.y + (self.height / 2- text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False


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

        # app buttons
        self.selection_button = Button(self, colors.WHITE, 142, 100, 100, 70, 'Selection')
        self.bubble_button = Button(self, colors.WHITE, 302, 100, 100, 70, 'Bubble')
        self.insertion_button = Button(self, colors.WHITE, 462, 100, 100, 70, 'Insertion')
        self.merge_button = Button(self, colors.WHITE, 622, 100, 100, 70, 'Merge')
        self.quick_button = Button(self, colors.WHITE, 782, 100, 100, 70, 'Quick')
        
        # TODO: add reset button here
        self.reset_button = Button(self, colors.WHITE, 142, 200, 100, 70, 'RESET')

    ###################################################
    # MAIN LOOP
    ###################################################
    def run(self):
        while self.running:
            if self.state == 'main':
                self.main_events()
            elif self.state == 'aftermath':
                self.aftermath_events()
        pygame.quit()
        sys.exit()

    ###################################################
    # MENU EVENT
    ###################################################
    def sketch_menu(self):
        self.selection_button.draw_button(colors.AQUAMARINE)
        self.bubble_button.draw_button(colors.AQUAMARINE)
        self.insertion_button.draw_button(colors.AQUAMARINE)
        self.merge_button.draw_button(colors.AQUAMARINE)
        self.quick_button.draw_button(colors.AQUAMARINE)
        self.reset_button.draw_button(colors.AQUAMARINE)

    def main_events(self):
        # self.win.update()
        pygame.display.update()
        self.sketch_menu()
        # self.draw_text()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.selection_button.isOver(pos):
                    self.algorithms['SelectionSort'].run()
                    self.state = 'aftermath'
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
                    self.selection_button.color = colors.AQUAMARINE
                elif self.bubble_button.isOver(pos):
                    self.bubble_button.color = colors.AQUAMARINE
                elif self.insertion_button.isOver(pos):
                    self.insertion_button.color = colors.AQUAMARINE
                elif self.merge_button.isOver(pos):
                    self.merge_button.color = colors.AQUAMARINE
                elif self.quick_button.isOver(pos):
                    self.quick_button.color = colors.AQUAMARINE
                else:
                    self.set_buttons_color(colors.WHITE)

    # TODO: check if really necessary
    def draw_text(self, words, pos, size, color, font_name, center=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        if center:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        self.win.blit(text, pos)

    # TODO: write set_buttons_color method
    def set_buttons_color(self, color):
        self.selection_button.color = color
        self.bubble_button.color = color
        self.insertion_button.color = color
        self.merge_button.color = color
        self.quick_button.color = color


    ###################################################
    # VISUALISATION
    ###################################################
    def visualize(self, algorithm, swap1=None, swap2=None):
        self.win.fill(pygame.Color("#a48be0"))
        # self.draw_text(f'SAV: {algorithm.name} | {time.time() - algorithm.start_time} | Sorting...', 200, 28, colors.WHITE, FONT, center=True)
        k = int(WIDTH / len(algorithm.array))
        for i in range(len(algorithm.array)):
            color = (80, 0, 255)
            if swap1 == algorithm.array[i]:
                color = (0, 255, 0)
            elif swap2 == algorithm.array[i]:
                color = (255, 0, 0)

            pygame.draw.rect(self.win, color, (i * k, HEIGHT, k, -algorithm.array[i]))
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
    # sys.argv.append('MergeSort')
    # main(sys.argv)
    viz = Visualizer()
    viz.run()
