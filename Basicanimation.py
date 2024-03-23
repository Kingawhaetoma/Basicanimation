# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:06:43 2024

@author: kinga
"""
import pygame
def main():
    pygame.init()

    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Soccer!")

    #Entities
    #Soccerfield background
    background = pygame.image.load("SoccerField.jpeg")
    background = background.convert_alpha()
    background = pygame.transform.scale(background, screen.get_size())

    #load an image
    SoccerBall = pygame.image.load("SoccerBall.png")
    SoccerBall = SoccerBall.convert_alpha()
    SoccerBall = pygame.transform.scale(SoccerBall, (100, 100))

    # set up some SoccerBall variables
    SoccerBall_x = 0
    SoccerBall_y = 200

    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True

        #Loop
    while keepGoing:

        #Time
        clock.tick(30)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #modify SoccerBall value
        SoccerBall_x += 5
        #check boundaries
        if SoccerBall_x > screen.get_width():
            SoccerBall_x = 0

        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(SoccerBall, (SoccerBall_x, SoccerBall_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()