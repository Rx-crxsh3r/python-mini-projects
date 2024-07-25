#This program shows the simulation of 5 balls bouncing under gravitational acceleration.
#It is also accompanied by eleastic collission with walls of the container.
#It is fun to watch.
import pygame,time,random

pygame.init()

#setting screen size of pygame window to 800 by 600 pixels
screen=pygame.display.set_mode((800,600))
background=pygame.image.load(r'C:\Users\thebl\Desktop\‎\folder1\mini-stuff\python-mini-projects\projects\Bouncing_ball_simulator\background-img.jpg')

#Adding title
pygame.display.set_caption('Ball Bounce Simulation')

class ball:
    ball_image=pygame.image.load(r'C:\Users\thebl\Desktop\‎\folder1\mini-stuff\python-mini-projects\projects\Bouncing_ball_simulator\ball.png')
    g=1
    def __init__(self):
        self.velocityX=10
        self.velocityY=10
        self.X=random.randint(0,768)
        self.Y=random.randint(0,350)

    def render_ball(self):
        screen.blit(ball.ball_image, (self.X,self.Y))
    def move_ball(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY+=ball.g
        #changing position based on velocity
        self.X+=self.velocityX
        self.Y+=self.velocityY
        #collission with the walls lead to change in velocity
        if self.X<0 or self.X>768:
            self.velocityX*=-1
        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            self.Y=0
        if self.Y>568 and self.velocityY>0:
            self.velocityY*=-1
            self.Y=568



class ball2:
    ball_image2=pygame.image.load(r'C:\Users\thebl\Desktop\‎\folder1\mini-stuff\python-mini-projects\projects\Bouncing_ball_simulator\ball2.png')
    g=1
    def __init__(self):
        self.velocityX=13
        self.velocityY=13
        self.X=random.randint(0,768)
        self.Y=random.randint(0,350)

    def render_ball(self):
        screen.blit(ball2.ball_image2, (self.X,self.Y))
    def move_ball(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY+=ball2.g
        #changing position based on velocity
        self.X+=self.velocityX
        self.Y+=self.velocityY
        #collission with the walls lead to change in velocity
        if self.X<0 or self.X>768:
            self.velocityX*=-1
        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            self.Y=0
        if self.Y>568 and self.velocityY>0:
            self.velocityY*=-1
            self.Y=568


class ball3:
    ball_image3=pygame.image.load(r'C:\Users\thebl\Desktop\‎\folder1\mini-stuff\python-mini-projects\projects\Bouncing_ball_simulator\ball3.png')
    g=1
    def __init__(self):
        self.velocityX=9.4
        self.velocityY=12.89
        self.X=random.randint(0,768)
        self.Y=random.randint(0,350)

    def render_ball(self):
        screen.blit(ball3.ball_image3, (self.X,self.Y))
    def move_ball(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY+=ball3.g
        #changing position based on velocity
        self.X+=self.velocityX
        self.Y+=self.velocityY
        #collission with the walls lead to change in velocity
        if self.X<0 or self.X>768:
            self.velocityX*=-1
        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            self.Y=0
        if self.Y>568 and self.velocityY>0:
            self.velocityY*=-1
            self.Y=568


class ball4:
    ball_image4=pygame.image.load(r'C:\Users\thebl\Desktop\‎\folder1\mini-stuff\python-mini-projects\projects\Bouncing_ball_simulator\ball4.png')
    g=1
    def __init__(self):
        self.velocityX=8.7
        self.velocityY=12
        self.X=random.randint(0,768)
        self.Y=random.randint(0,350)

    def render_ball(self):
        screen.blit(ball4.ball_image4, (self.X,self.Y))
    def move_ball(self):
        #changing y component of velocity due to downward acceleration
        self.velocityY+=ball4.g
        #changing position based on velocity
        self.X+=self.velocityX
        self.Y+=self.velocityY
        #collission with the walls lead to change in velocity
        if self.X<0 or self.X>768:
            self.velocityX*=-1
        if self.Y<0 and self.velocityY<0:
            self.velocityY*=-1
            self.Y=0
        if self.Y>568 and self.velocityY>0:
            self.velocityY*=-1
            self.Y=568
#list of balls created as objects
Ball_List=[ball(),ball(), ball(), ball4(), ball3(), ball2(), ball4(), ball4(), ball3(), ball3(), ball2(), ball2()]

#The main program loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    time.sleep(0.02)
    screen.blit(background, (0,0))
    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()
    pygame.display.update()