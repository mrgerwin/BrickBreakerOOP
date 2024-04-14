import pygame as pygame
from Block import *

def drawScore(font):
    global score, lives
    
    text=font.render(str(score), True, white)
    window.blit(text, (200, 30))
    text=font.render(str(lives), True, white)
    window.blit(text, (600, 30))

def MoveBall():
    global lives, ballSpeedx, ballSpeedy, ballLocation, ball
    
    if ballLocation[0] > screenWidth:
        ballSpeedx = -ballSpeedx
    
    if ballLocation[0] < 0:
        ballSpeedx = -ballSpeedx
    
    if ballLocation[1] < 0:
        ballSpeedy = -ballSpeedy
    
    if ballLocation[1] > screenHeight:
        ballLocation = [500, 300]
        lives = lives -1
        if lives == 0:
            ballSpeedx = 0
            ballSpeedy = 0
            lives = "Game Over"
        
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, white, ballLocation, radius, 0) 
    
def MovePaddle():
    global PadASpeed, PadA
    """
    Moves the paddle side to side
    """
    
    if PadA.left <= 0:
        print("Left Side of Screen")
        PadA = PadA.move(2,0)
        PadASpeed = 0
    
    if PadA.right >= screenWidth:
        print("Right Side of Screen")
        PadA = PadA.move(-2,0)
        PadASpeed = 0
    #Add right of Paddle Code here
        
    PadA = PadA.move(PadASpeed, 0)
    pygame.draw.rect(window, white, PadA)

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600

window = pygame.display.set_mode([screenWidth, screenHeight])

ballSpeedx = -1
ballSpeedy = 3
black = (0,0,0)
white = (255, 255, 255)
radius = 20
ballLocation=[500, 300]
ball = pygame.Rect(ballLocation, (radius, radius))

PadA = pygame.Rect((500,570), (100,20))
PadASpeed = 0

score = 0
lives = 3
alreadyHit = False

block0 = RedBlock(window, 0, 0)
block1 = RedBlock(window, 100, 0)
block2 = Block(window, 200, 0)
block3 = Block(window, 300, 0)
block4 = Block(window, 400, 0)
block5 = Block(window, 500, 0)
block6 = Block(window, 600, 0)
block7 = Block(window, 700, 0)
block8 = Block(window, 800, 0)
block9 = Block(window, 900, 0)

blocks = [block0, block1, block2, block3, block4, block5, block6, block7, block8, block9]

pygame.font.init()
#print(pygame.font.get_fonts())
font = pygame.font.SysFont(None, 72)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PadASpeed = -2
            if event.key == pygame.K_RIGHT:
                PadASpeed = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                PadASpeed = 0
            if event.key == pygame.K_RIGHT:
                PadASpeed = 0
    if PadA.colliderect(ball):
        ballSpeedy = -ballSpeedy
        ballSpeedx = ballSpeedx + PadASpeed
    timer.tick(60)
    window.fill(black)
    for block in blocks:
        block.draw()
        if ball.colliderect(block.rect):
            if alreadyHit == False:
                ballSpeedy = -ballSpeedy
                alreadyHit = True
            print("Hit Block" + str(block.rect))
            if block.color == (255, 255, 255):
                blocks.remove(block)
                points = block.destroy()
                score = score + points
            else:
                block.hit()
    alreadyHit = False        
            
    MoveBall()
    MovePaddle()
    drawScore(font)
    pygame.display.flip()