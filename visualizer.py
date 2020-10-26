import algo
import time
import sys
import pygame

WIDTH = 1024
HEIGHT = 512

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
    def __init__(self, app, color, x, y, width, height, text=None, text_size=None):
        self.app = app
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.text_color = colors.SPRINGGREEN

    def draw_button(self, outline=None):
        if outline:
            pygame.draw.rect(self.app.win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 4)
        pygame.draw.rect(self.app.win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text:
            font = pygame.font.SysFont(FONT, self.text_size)
            text = font.render(self.text, 0, self.text_color)
            self.app.win.blit(text, (self.x + int(self.width / 2 - text.get_width() / 2),
                                        self.y + int(self.height / 2- text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False


class Visualizer:
    def __init__(self):
        # init for pygame
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.win.fill(colors.BLACK)
        self.clock = pygame.time.Clock()

        # init for visualizer
        self.running = True
        self.algorithms = ALGORITHMS
        self.state = 'main'

        # app buttons
        self.selection_button = Button(self, colors.STEELBLUE, 142, 100, 100, 70, 'Selection', 18)
        self.bubble_button = Button(self, colors.STEELBLUE, 302, 100, 100, 70, 'Bubble', 18)
        self.insertion_button = Button(self, colors.STEELBLUE, 462, 100, 100, 70, 'Insertion', 18)
        self.merge_button = Button(self, colors.STEELBLUE, 622, 100, 100, 70, 'Merge', 18)
        self.quick_button = Button(self, colors.STEELBLUE, 782, 100, 100, 70, 'Quick', 18)
        
        self.reset_button = Button(self, colors.STEELBLUE, 782, HEIGHT - 150, 130, 70, 'Restart', 26)

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
    # DRAW BUTTONS FOR THE MENU
    ###################################################
    def sketch_menu(self):
        self.win.fill(colors.BLACK)
        self.selection_button.draw_button(colors.MINT)
        self.bubble_button.draw_button(colors.MINT)
        self.insertion_button.draw_button(colors.MINT)
        self.merge_button.draw_button(colors.MINT)
        self.quick_button.draw_button(colors.MINT)
        # self.reset_button.draw_button(colors.AQUAMARINE)
    
    ###################################################
    # MAIN FUNCTION
    ###################################################
    def main_events(self):
        pygame.display.update()
        self.sketch_menu()
        self.draw_text("Made by beomus", [WIDTH - 160, HEIGHT - 30],
                        16, colors.ALICE, FONT)
        self.draw_text("Sorting Algorithms Visualizer", [270, 300] , 30,
                        colors.SPRINGGREEN, FONT)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.selection_button.isOver(pos):
                    _, time_elapsed = self.algorithms['SelectionSort'].run()
                    self.draw_text('Algorithm: Selection Sort', [130, 100], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.draw_text(f"Time elapsed: {round(time_elapsed, 2)}", [130, 140], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.state = 'aftermath'
                elif self.bubble_button.isOver(pos):
                    _, time_elapsed = self.algorithms['BubbleSort'].run()
                    self.draw_text('Algorithm: Bubble Sort', [130, 100], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.draw_text(f"Time elapsed: {round(time_elapsed, 2)}", [130, 140], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.state = 'aftermath'
                elif self.insertion_button.isOver(pos):
                    _, time_elapsed = self.algorithms['InsertionSort'].run()
                    self.draw_text('Algorithm: Insertion Sort', [130, 100], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.draw_text(f"Time elapsed: {round(time_elapsed, 2)}", [130, 140], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.state = 'aftermath'
                elif self.merge_button.isOver(pos):
                    _, time_elapsed = self.algorithms['MergeSort'].run()
                    self.draw_text('Algorithm: Merge Sort', [130, 100], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.draw_text(f"Time elapsed: {round(time_elapsed, 2)}", [130, 140], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.state = 'aftermath'
                elif self.quick_button.isOver(pos):
                    _, time_elapsed = self.algorithms['QuickSort'].run()
                    self.draw_text('Algorithm: Quick Sort', [130, 100], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.draw_text(f"Time elapsed: {round(time_elapsed, 2)}", [130, 140], 32,
                                    colors.SPRINGGREEN, FONT)
                    self.state = 'aftermath'
            
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
                    self.set_buttons_color(colors.STEELBLUE)

    ###################################################
    # SECONDARY FUNCTION
    ###################################################
    def aftermath_events(self):
        pygame.display.update()
        self.draw_text("Made by beomus", [WIDTH - 160, HEIGHT - 30],
                        16, colors.ALICE, FONT)
        self.reset_button.text_color = colors.RED
        self.reset_button.draw_button(colors.TAN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.reset_button.isOver(pos):
                    for algo in self.algorithms:
                        self.algorithms[f'{algo}'].reset()
                    self.state = 'main'

            if event.type == pygame.MOUSEMOTION:
                if self.reset_button.isOver(pos):
                    self.reset_button.color = colors.AQUAMARINE
                else:
                    self.reset_button.color = colors.MINT

    ###################################################
    # DRAW TEXT ON THE WINDOW
    ###################################################
    def draw_text(self, words, pos, size, color, font_name, center=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        if center:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        self.win.blit(text, pos)

    ###################################################
    # CHANGING ALL BUTTONS COLORS
    ###################################################
    def set_buttons_color(self, color):
        self.selection_button.color = color
        self.bubble_button.color = color
        self.insertion_button.color = color
        self.merge_button.color = color
        self.quick_button.color = color
        self.reset_button.color = color
 

if __name__ == '__main__':
    viz = Visualizer()
    viz.run()
