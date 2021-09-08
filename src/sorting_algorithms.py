import time
import random
from abc import ABCMeta, abstractmethod

class Algorithm(metaclass=ABCMeta):
      def __init__(self, name):
            self.array = random.sample(range(512), 512)
            self.name = name
      def render_display(self, swap=None, swap2=None):
            # import other file
            import visualization
            visualization.update(self, swap, swap2) # Passing the index
      def start(self): # Run the algorithm
            self.start_time = time.time()
            self.algorithm()
            # Time elapsed since start
            time_elapsed = time.time() - self.start_time
            return self.array, time_elapsed # Return the sorted array too
      @abstractmethod
      def algorithm(self):
            raise TypeError(f"Algorithm.algorithm() has not been overwritten.")

class SelectionSort(Algorithm):
      def __init__(self):
            super().__init__("SelectionSort")
      def algorithm(self):
            for x in range(len(self.array)):
                  minimum_index = x
                  for k in range(x + 1, len(self.array)):
                        if self.array[k] < self.array[minimum_index]:
                              minimum_index = k
                  self.array[x], self.array[minimum_index] = self.array[minimum_index], self.array[x]
                  # Everytime we swap, call update_display to perform it in realtime
                  self.update_display(self.array[x], self.array[minimum_index])
class BubbleSort(Algorithm):
      def __init__(self):
            super().__init__("BubbleSort")
      def algorithm(self):
            for x in range(len(self.array)):
                  for y in range(len(self.array) - 1 - x):
                        if self.array[y] > self.array[y + 1]:
                              self.array[y],self.array[y + 1] = self.arrray[y  + 1], self.array[y]
                  self.update_display(self.array[y], self.arrray[y + 1]) 
