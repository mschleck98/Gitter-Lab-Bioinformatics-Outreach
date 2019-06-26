import pygame, sys
import os
import pygame.locals
import time
import matplotlib.pyplot as plt

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MN', 100)
BLACK = (255,255,255)
WIDTH = 1280
HEIGHT = 1000
screenInfo = pygame.display.Info()
screen = pygame.display.set_mode((screenInfo.current_w,screenInfo.current_h),0,32)


def updateBoard(lives, WIDTH, HEIGHT,color, filename, myfont, screenInfo, screen):
    windowSurface = pygame.Surface((WIDTH,HEIGHT))
    tempSurface = pygame.Surface((screenInfo.current_w,screenInfo.current_h))
    windowSurface.fill(color)
    tmpsurface = myfont.render('PROTEIN', False, (255,0,0))
    windowSurface.blit(tmpsurface, (50,0))
    tmp = myfont.render('I',False,(255,0,0))
    windowSurface.blit(tmp, (50,60))
    tmp = myfont.render('N',False,(255,0,0))
    windowSurface.blit(tmp, (50,120))
    tmp = myfont.render('B',False,(255,0,0))
    windowSurface.blit(tmp, (50,180))
    tmp = myfont.render('A',False,(255,0,0))
    windowSurface.blit(tmp, (50,240))
    tmp = myfont.render('L',False,(255,0,0))
    windowSurface.blit(tmp, (50,300))
    tmp = myfont.render('L',False,(255,0,0))
    windowSurface.blit(tmp, (50,360))
    image = pygame.image.load(filename)
    windowSurface.blit(image,(250,75))
    image = pygame.image.load('Alpha_Helix.png')
    windowSurface.blit(image,(900,25))
    image = pygame.image.load('download.png')
    windowSurface.blit(image,(25, 600))
    image = pygame.image.load('amino.png')
    windowSurface.blit(image,(800,600))
    tmp = myfont.render('Lives: ' + str(lives), False, (255,255,255))
    tmp_rect = tmp.get_rect()
    tmp_x = tmp_rect.width + 20
    tmp_y = tmp_rect.height + 20
    pygame.draw.rect(windowSurface, (255,0,0), [450, 580, tmp_x,tmp_y])
    windowSurface.blit(tmp,(460,590))
    pygame.transform.scale(windowSurface, (screenInfo.current_w,screenInfo.current_h), tempSurface)
    screen.blit(tempSurface,(0,0))
    pygame.display.update()
        
while True:
    #print('HERDASDSADSADSADASD')
    windowSurface = pygame.Surface((WIDTH,HEIGHT))
    tempSurface = pygame.Surface((screenInfo.current_w,screenInfo.current_h))                
    windowSurface.fill(BLACK)
    testsurface = myfont.render('WELCOME TO PROTEIN PINBALL', False, (255,0,0))
    windowSurface.blit(testsurface, (0,0))
    textsurface = myfont.render('LAUNCH BALL TO BEGIN', False, (255, 0, 0))
    windowSurface.blit(textsurface, (0,200))
    image2 = pygame.image.load('maindq.png')
    windowSurface.blit(image2,(400,400))
    pygame.transform.scale(windowSurface, (screenInfo.current_w,screenInfo.current_h), tempSurface)
    screen.blit(tempSurface,(0,0))
    pygame.display.update()
    #image = pygame.image.load('signal_graph.png')
    #protein counts
    p1 = 0
    Ap1 = [0]
    p2 = 0
    Ap2 = [0]
    p3 = 0
    Ap3 = [0]
    #initial time variable
    t0 = 0
    t1 = 0
    t2 = 0
    xaxis = [0]
    temp = -1
    #print('HEREHEHREHRHERHEHR')
    plt.plot(xaxis,Ap1, color = 'green', label = "SIGNAL 1")
    plt.plot(xaxis,Ap2, color='blue', label = "SIGNAL 2")
    plt.plot(xaxis,Ap3, color='red', label = "SIGNAL 3")
    plt.xlabel('time')
    plt.ylabel('# of Signals')
    plt.title('Protein Interactions Over Time')
    plt.legend()
    
    lives = 3
    pause = False
    game = True
    newGame = True
    while game:
        if ((t2-t1) >= 5) and pause:
                temp = temp + 1
                xaxis.append(temp)
                Ap1.append(p1)
                Ap2.append(p2)
                Ap3.append(p3)
                plt.plot(xaxis,Ap1, color = 'green', label = "Protein 1")
                plt.plot(xaxis,Ap2, color='blue', label = "Protein 2")
                plt.plot(xaxis,Ap3, color='red', label = "Protein 3")
                #plt.xlabel('time')
                #plt.ylabel('# of Signals')
                filename = "signal_graph" + str(temp) + ".png"
                plt.savefig(filename)
                updateBoard(lives, WIDTH,HEIGHT,BLACK, filename, myfont, screenInfo, screen)
                p1 = 0
                p2 = 0
                p3 = 0
                t1 = t2
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_RIGHT:
                 #   t0 = int(time.time())
                  #  t1 = t0
                   # if newGame:
                     #   windowSurface.fill(BLACK)
                      #  pygame.display.update()
                    #    newGame = False
                    #pause = True
                    #pass
                if event.key == pygame.K_UP:
                    if pause:
                        p1 = p1 + 5
                        t2 = int(time.time())
                    else:
                        t0 = int(time.time()) - 5
                        t1 = t0
                        t2 = t1 + 5
                        lives = lives - 1
                        if newGame:
                            newGame = False
                        pause = True
                    pass
                if event.key == pygame.K_DOWN and pause:
                    if pause:
                        p2 = p2 + 5
                        t2 = int(time.time())
                    else:
                        t0 = int(time.time()) - 5
                        t1 = t0
                        t2 = t1 + 5
                        lives = lives - 1
                        if newGame:
                            newGame = False
                        pause = True
                    pass
                if event.key == pygame.K_LEFT and pause:
                    if pause:    
                        p3 = p3 + 5;
                        t2 = int(time.time())
                    else:
                        t0 = int(time.time()) - 5
                        t1 = t0
                        t2 = t1 + 5
                        lives = lives - 1
                        if newGame:
                                newGame = False
                        pause = True
                    pass
                if event.key == pygame.K_SPACE and pause:
                    temp = temp + 1
                    xaxis.append(temp)
                    Ap1.append(p1)
                    Ap2.append(p2)
                    Ap3.append(p3)
                    plt.plot(xaxis,Ap1, color = 'green', label = "Protein 1")
                    plt.plot(xaxis,Ap2, color='blue', label = "Protein 2")
                    plt.plot(xaxis,Ap3, color='red', label = "Protein 3")
                    #plt.xlabel('time')
                    #plt.ylabel('# of Signals')
                    filename = "signal_graph" + str(temp) + ".png"
                    plt.savefig(filename)
                    if lives == 0:
                        game = False
                        plt.clf()
                        #sys.exit()
                        #pygame.quit()
                        continue 
                    #image = pygame.image.load(filename)
                    #windowSurface.blit(image,(0,0))
                    #pygame.display.update()
                    updateBoard(lives, WIDTH,HEIGHT,BLACK, filename, myfont, screenInfo, screen)
                    temp = temp - 1
                    pause = False
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
    while newGame == False:
        windowSurface = pygame.Surface((WIDTH,HEIGHT))
        tempSurface = pygame.Surface((screenInfo.current_w,screenInfo.current_h))
        windowSurface.fill(BLACK)
        image = pygame.image.load(filename)
        windowSurface.blit(image,(325,100))
        textsurface = myfont.render('GAME OVER', False, (255, 0, 0))
        windowSurface.blit(textsurface, (450,50))
        textsurface = myfont.render('Press Start Button to Play Again', False, (255, 0, 0))
        windowSurface.blit(textsurface, (150,600))
        pygame.transform.scale(windowSurface, (screenInfo.current_w,screenInfo.current_h), tempSurface)
        screen.blit(tempSurface,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    newGame = True
                    pass
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
                        
            
                
    