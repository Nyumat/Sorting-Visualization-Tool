import sorting_algorithms as algorithms
import time
import sys
import pygame
import os

# Len X Size of Array
size = [1024,512]
algorithms = {"Selection_Sort": algorithms.Selection_Sort()}

if len(sys.argv) > 1:
      if sys.argv[1] == "list":
            for key in algorithms.keys():
                  print(key,end=" ")
            print("")
            sys.exit(0)
pygame.init()
display = pygame.display.set_mode((size[0], size[1]))
display.fill(pygame.Color("#a48be0"))
# Check for window quit
def check_quit():
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
# Draw the sorted array on each iteration                  
def render(algorithm, swap=None, swap2=None, display=display):
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

"""
To  still  do:

 - Keep window open
 - Main function
 - Error handling
 - Finish adding other algorithms  
"""