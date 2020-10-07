import algo
import time
import sys
import pygame

WIDTH = 1024
HEIGHT = 512

algorithms = {
    'SelectionSort': algo.SelectionSort(),
    'BubbleSort': algo.BubbleSort(),
    'InsertionSort': algo.InsertionSort(),
    'MergeSort': algo.MergeSort(),
    'QuickSort': algo.QuickSort()
}

win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill(pygame.Color("#a48be0"))


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def update(algorithm, swap1=None, swap2=None, display=win):
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption(f'SAV: {algorithm.name} | {time.time() - algorithm.start_time} | Sorting...')
    k = int(WIDTH / len(algorithm.array))
    for i in range(len(algorithm.array)):
        color = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            color = (0, 255, 0)
        elif swap2 == algorithm.array[i]:
            color = (255, 0, 0)

        pygame.draw.rect(display, color, (i * k, HEIGHT, k, -algorithm.array[i]))
    check_events()
    pygame.display.update()


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
    sys.argv.append('SelectionSort')
    main(sys.argv)
