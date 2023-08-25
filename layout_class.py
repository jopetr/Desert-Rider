import pygame
import math
from random import random as random

class Layout:
    
    
    def populate(self):
        start = 10**4*0.2
        end = 7.2*10**4

        #8*10^2 x 7.2*10^4
        # Diagram: 800X1440, factors: 1x50
        # Green, 300x300
        obstacles = []
        # Blue, 100x100, y = 560 - 800
        mines = []
        # Yellow, 100x180, y = 0 - 300
        bombs = []
        # Red, 12500x400, y = 50 - 450
        vessels = []

        #obstacles.append(start+1000)
        
        #bombs.append([start+1000,200])

        mines.append([1500, 750])
        bombs.append([1600, 100])
        mines.append([1700, 750])
        bombs.append([1800, 100])
        mines.append([1900, 750])
        obstacles.append(2400)
        mines.append([2400, 750])
        bombs.append([2400, 120])

        vessel_start = start + 2000

        vessels.append(vessel_start)
        for i in range(30):
            #bombs.append([vessel_start+i*400+100, 150])
            #obstacles.append(vessel_start+i*400+300)
            mines.append([vessel_start+i*400, 560])
            mines.append([vessel_start+i*400, 680])
            mines.append([vessel_start+i*400, 800])
            mines.append([vessel_start+i*400+200, 620])
            mines.append([vessel_start+i*400+200, 730])

        obstacles.append(16500)
        obstacles.append(17000)
        bombs.append([16500, 50])
        bombs.append([17000, 100])
        bombs.append([17400, 200])
        for i in range(20):
            mines.append([16500+i*300, 750-i*8])
            bombs.append([18000+i*300, 350-i*12])
        
        for i in range(20):
            mines.append([23000+i*300, 560+i*8])
            if i%4==3:
                obstacles.append(23000+i*300)
            else:
                bombs.append([24000+i*300, 100])
        vessel_start = start + 28000
        vessels.append(vessel_start)
        
        for i in range(30):
            if i%4==0:
                bombs.append([vessel_start+i*400+100, 50])
            elif i%2==0:
                obstacles.append(vessel_start+i*400+300)
            mines.append([vessel_start+i*400, 560])
            mines.append([vessel_start+i*400, 680])
            mines.append([vessel_start+i*400, 800])
            mines.append([vessel_start+i*400+200, 620])
            mines.append([vessel_start+i*400+200, 730])

        obs_start = 43000
        for i in range(30):
            if i%2==0:
                mines.append([obs_start+i*400, 600])
                mines.append([obs_start+i*400, 750])
                if i%8==0:
                    obstacles.append(obs_start+i*400+200)
                
            else:
                mines.append([obs_start+i*400, 675])
                bombs.append([obs_start+i*400, 50])
                bombs.append([obs_start+i*400, 340])
            

        vessel_start = start + 54000
        vessels.append(vessel_start)
        vessels.append(vessel_start+2000)
        for i in range(39):
            if i%4==0:
                bombs.append([vessel_start+i*400+100, 50])
            elif i%2==0:
                obstacles.append(vessel_start+i*400+300)
            mines.append([vessel_start+i*400, 560])
            mines.append([vessel_start+i*400, 680])
            mines.append([vessel_start+i*400, 800])
            mines.append([vessel_start+i*400+200, 620])
            mines.append([vessel_start+i*400+200, 730])

        self.layout['Obstacles'] = obstacles
        self.layout['Mines'] = mines
        self.layout['Bombs'] = bombs
        self.layout['Vessels'] = vessels
        return self.layout
        
    '''
    Updates rects and ims of obstacle to correspond to collision animation
    '''
    def diagram(self):
        obstacle = self.raw_ims[0]
        mine = self.raw_ims[1]
        bomb = self.raw_ims[2]
        vessel = self.raw_ims[3]
        
        
        rects = []
        ims = []

        for v in self.layout['Vessels']:
            im = pygame.transform.scale(vessel, (250, 400))
            rect = im.get_rect()
            rect.center = (v/50 + 125, 250)
            ims.append(im)
            rects.append(rect)

        for o in self.layout['Obstacles']:
            im = pygame.transform.scale(obstacle, (6, 200))
            rect = im.get_rect()
            rect.center = (o/50, 400)
            ims.append(im)
            rects.append(rect)

        for m in self.layout['Mines']:
            im = pygame.transform.scale(mine, (2, 90))
            rect = im.get_rect()
            rect.center = (m[0]/50, m[1])
            ims.append(im)
            rects.append(rect)

        for b in self.layout['Bombs']:
            im = pygame.transform.scale(bomb, (2, 180))
            rect = im.get_rect()
            rect.center = (b[0]/50, b[1])
            ims.append(im)
            rects.append(rect)

        

        self.rects = rects
        self.ims = ims

    

    '''
    Blits character to display surface using rects and ims
    '''
    def blit(self, display_surface: pygame.Surface):
        for i in range(len(self.rects)):
            display_surface.blit(self.ims[i], self.rects[i])

    '''
    Initializes character by loading character images from given path
    '''
    def __init__(self):
        self.layout = {}
        self.layout['Obstacles'] = []
        self.layout['Mines'] = []
        self.layout['Bombs'] = []
        self.layout['Vessels'] = []
        self.raw_ims = [pygame.image.load("Layout/green.png").convert(), pygame.image.load("Layout/blue.png").convert(), pygame.image.load("Layout/yellow.png").convert(), pygame.image.load("Layout/red.png").convert()]
