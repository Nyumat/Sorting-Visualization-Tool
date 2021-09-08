import sorting_algorithms as algorithms
import time
import sys
import pygame
import os

# Len X Size of Array
size = (1024,512)
algorithms = {"SelectionSort": algorithms.SelectionSort(), "BubbleSort": algorithms.BubbleSort()}

display = pygame.display.set_mode(size)
display.fill(pygame.Color("#a48be0"))

# Check for window quit
def check_quit():
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
# Draw the sorted array on each iteration                  
def update(algorithm, swap=None, swap2=None, display=display):
      display.fill(pygame.Color("#a48be0"))
      pygame.display.set_caption("Sorting Visualization Tool   Algorithm {}   Time: {:.3f}   Status: Sorting....".format(algorithm.name, time.time() -  algorithm.start_time))
      k = int(size[0] / len(algorithm.array))

      for i in range(len(algorithm.array)):
            color = (80,0,255)
            if swap == algorithm.array[i]:
                  color = (0,255,0)
            elif swap2 == algorithm.array[i]:
                  color = (255,0,0)
            # Render the rectangles that are getting sorted to the screen
            pygame.draw.rect(display, color, (i*k, size[1], k, -algorithm.array[i]))
      check_quit()
      pygame.display.update()

def keep_window_open(algorithm, display, time):
      pygame.display.set_caption("Sorting Visualization Tool     Algorithm: {}      Time: {:.3f}      Status: Sorting Complete.".format(algorithm.name, time))     
      while True:
            check_quit()
            

def main(args):
      if len(sys.argv) < 2:
            print("Select an algorithm")
      elif args[1] == "list": # show list of algorithms available
            print("Algorithms list:\n\t" + "\n\t".join(algorithms.keys()))
            sys.exit(0)
      else: # Picked an algo
            try:
                  algorithm = algorithms[args[1]]
                  _, time_elapsed = algorithm.start()
                  keep_window_open(algorithm, display, time_elapsed)
            except:
                  print("Error")

if __name__ == "__main__":
      sys.argv.append("BubbleSort")
      main(sys.argv)