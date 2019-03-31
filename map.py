import pygame
from pygame.locals import *
from settings import *
import time
import math

class Spot():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def initCell(self):
        for i in range(0, cols):
            tempGrid = []
            for j in range(0, rows):
                tempGrid.append(0)
            grid.append(tempGrid)

    def showCell(x, y):
        pygame.draw.rect(display_surf, WHITE, (0, 0, 0, 0))



class App():
    def __init__(self):
        self.spot = Spot(0, 0)
        self._running = True
        display_surf = None

    def onInit(self):
        pygame.init()
        self._running = True
        self.spot.initCell()
        for i in range(0, cols):
            for j in range(0, rows):
                grid[i][j] = Spot(i, j)

        debug(grid)

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def onRender(self):
        display_surf.fill((0, 0, 0))

        pygame.display.flip()

    def onLoop(self):
        pass

    def onCleanup(self):
        pygame.quit()

    def onExecute(self):
        if self.onInit() == False:
            self._running == False

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if(keys[K_ESCAPE]):
                self._running = False

            self.onLoop()
            self.onRender()
            time.sleep(50.0/1000.0)

        self.onCleanup()

if __name__ == "__main__":
    app = App()
    app.onExecute()
