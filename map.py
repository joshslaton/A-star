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

    def showCell(self):
        pygame.draw.rect(display_surf, GREEN, (self.x*cellWidth+1, self.y*cellHeight+1, cellWidth-1, cellHeight-1))
        # pygame.display.flip()



class App():
    def __init__(self):
        self._running = True
        display_surf = None

    def onInit(self):
        pygame.init()
        Spot(0, 0).initCell()
        self._running = True

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def onRender(self):
        display_surf.fill((0, 0, 0))
        for i in range(0, cols):
            for j in range(0, rows):
                grid[i][j] = Spot(i, j).showCell()
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
