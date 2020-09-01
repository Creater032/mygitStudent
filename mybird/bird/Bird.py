#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Creaty.yi
# time: 2020.9.1

import pygame,sys
from pygame.locals import *

class Bird(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y):
        super().__init__()
        self.loadBird = pygame.image.load('./image/Mosquito.png').convert_alpha()
        #self.loadBird=pygame.image.load('./image{}'.formate(image)).convert_alpha()
        self.birdImage=pygame.transform.scale(self.loadBird,(width,height))

        self.rect=self.birdImage.get_rect()
        # 中心点数据
        self.rect.center=(x,y)

        self.width = width
        self.height = height



