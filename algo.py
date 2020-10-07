import time
import random
from abc import ABCMeta, abstractmethod


class Algorithm(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
        self.array = random.sample(range(512), 512)

    def update_display(self, swap1=None, swap2=None):
        import visualizer
        visualizer.update(self, swap1, swap2)

    def run(self):
        start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - start_time
        return self.array, time_elapsed

    @abstractmethod
    def algorithm(self):
        raise TypeError(f'Algorithm.algorithm() has not been overwritten.')


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
            
