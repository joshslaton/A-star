import pygame
from pygame.locals import *
from settings import *
import time
import math

class App():
    def __init__(self):
        self._running = True
        self._display_surf = None

    def onInit(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(size)
        self._running = True


    def onEvent(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def onRender(self):
        self._display_surf.fill((0, 0, 0))
        pygame.display.flip()

    def onLoop(self):
        pass
        # self.player.update()

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
