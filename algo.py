import time
import random
import pygame

WIDTH = 1024
HEIGHT = 512

class Algorithm:
    def __init__(self, name):
        self.name = name
        self.array = random.sample(range(512), 512)
        self.start_time = None
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))

    def update_display(self, swap1=None, swap2=None):
        self.win.fill((0, 0, 0))
        k = int(WIDTH / len(self.array))
        for i in range(len(self.array)):
            color = (0, 255, 127)
            if swap1 == self.array[i]:
                color = (0, 0, 255)
            elif swap2 == self.array[i]:
                color = (255, 0, 0)

            pygame.draw.rect(self.win, color, (i * k, HEIGHT, k, - self.array[i]))
        pygame.display.update()

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

    def reset(self):
        self.array = random.sample(range(512), 512)
        self.start_time = None


class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__('SelectionSort')

    def algorithm(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.update_display(self.array[i], self.array[min_idx])


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__('BubbleSort')

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array) - 1 - i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_display(self.array[j], self.array[j+1])


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__('InsertionSort')

    def algorithm(self):
        for i in range(len(self.array)):
            pointer = self.array[i]
            idx = i
            while idx > 0 and self.array[idx-1] > pointer:
                self.array[idx] = self.array[idx - 1]
                idx -= 1
            self.array[idx] = pointer
            self.update_display(self.array[idx], self.array[i])


class QuickSort(Algorithm):
    def __init__(self):
        super().__init__('QuickSort')

    def algorithm(self, array=[], start=0, end=0):
        if not array:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array, start, end)
            self.algorithm(array, start, pivot - 1)
            self.algorithm(array, pivot + 1, end)

    def partition(self, array, start, end):
        x = array[end]
        i = start - 1
        for j in range(start, end + 1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i], array[j])
        return i


# TODO: fix merge sort, doesn't work well with visualizer
class MergeSort(Algorithm):
    def __init__(self):
        super().__init__('MergeSort')

    def algorithm(self, array=[]):
        if not array:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update_display()
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result
