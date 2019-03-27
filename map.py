import pygame
from pygame.locals import *
from settings import *
import time
import math
import random

class Spot():
    def __init__(self, x, y):
        self.isWall = False
        self.f = 0
        self.g = 0
        self.gT = 0
        self.h = 0

        self.x = x
        self.y = y
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.neighbors = []

    def makeWall(self):
        # Randomly pick a cell based on percentage
        # print([len(array) for array in grid])
        print([len(array) for array in grid])

    def show(self, color):
        self.x1 = self.x * cellWidth
        self.y1 = self.y * cellHeight
        self.x2 = cellWidth
        self.y2 = cellHeight
        pygame.draw.rect(display_surf, color, (self.x1+1, self.y1+1, self.x2-2, self.y2-2))
        # pygame.display.flip()

    def getNeighbors(self):
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])

        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])

        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])

        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])

class App():
    def __init__(self):
        self._running = True
        display_surf = None
        self.drawOnce = True

    def onInit(self):
        pygame.init()
        self._running = True
        self.make2DList()

        self.start = grid[0][0]
        self.end = grid[cols-1][rows-1]
        self.openSet = [self.start]
        self.closedSet = []
        self.cameFrom = []

        # f(n) = g(n) + h(n)
        # g(n) =  cost of the path from START to NODE (n)
        # h(n) = cheapeast path from (n) to END

        # INITIALIZE SCORE FOR START
        self.start.f = 0 # heuristic cost from START TO END
        self.start.g = 0

    def make2DList(self):
        for i in range(0, cols):
            tempList1 = []
            for j in range (0, rows):
                tempList1.append(0)
            grid.append(tempList1)


        for i in range(0, cols):
            for j in range(0, rows):
                grid[i][j] = Spot(i, j)

    # Show all objects inside every grid
    def showGridInfo(self):
        for x in grid:
            for y in x:
                for attr, val in vars(y).items():
                    print(attr, val)
                print()

    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def onRender(self):
        display_surf.fill(BLACK)
        for i in range(0, cols):
            for j in range(0, rows):
                grid[i][j].show(WHITE)

        # START = GREEN
        for i in range(0, len(self.openSet)):
            self.openSet[i].show(GREEN)
        # END = BLUE
        self.end.show(BLUE)
        # CLOSED SET = BLUE
        for i in range(0, len(self.closedSet)):
            self.closedSet[i].show(RED)


        # IF OPENSET IS NOT EMPTY
        if len(self.openSet) > 0:
            winner = 0
            print("Before:")
            print(self.openSet[0].x, self.openSet[0].y)
            print(self.closedSet)



            for i in range(0, len(self.openSet)):
                if self.openSet[i].f > self.openSet[winner].f:
                    winner = i
            current = self.openSet[winner]
            if current == self.end:
                print("DONE")


            self.openSet.pop(0)
            self.closedSet.append(current)
            current.getNeighbors()
            for neighbor in current.neighbors:
                if neighbor in self.closedSet:
                    continue

            print()
            print("After:")
            print(self.openSet)
            print(self.closedSet[0].x, self.closedSet[0].y)
            print([len(array) for array in grid])
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
