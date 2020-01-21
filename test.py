import time, pygame
import RPi.GPIO as GPIO

left_high = 17
left_low = 27
right_high = 23
right_low = 22

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(left_high, GPIO.OUT)
    GPIO.setup(left_low, GPIO.OUT)
    GPIO.setup(right_high, GPIO.OUT)
    GPIO.setup(right_low, GPIO.OUT)

init()

def forward():
    init()
    GPIO.output(left_high, False)
    GPIO.output(left_low, True)
    GPIO.output(right_high, True)
    GPIO.output(right_low, False)
def backward():
    init()
    GPIO.output(left_high, True)
    GPIO.output(left_low, False)
    GPIO.output(right_high, False)
    GPIO.output(right_low, True)
def turnleft():
    init()
    GPIO.output(left_high, True)
    GPIO.output(left_low, False)
    GPIO.output(right_high, True)
    GPIO.output(right_low, False)
def turnright():
    GPIO.output(left_high, False)
    GPIO.output(left_low, True)
    GPIO.output(right_high, False)
    GPIO.output(right_low, True)
def halt():
    GPIO.output(left_high, False)
    GPIO.output(left_low, False)
    GPIO.output(right_high, False)
    GPIO.output(right_low, False)

pygame.init()
display = pygame.display.set_mode((200, 200))
display.fill((0, 0, 0))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_w:
                forward()
            elif event.key == pygame.K_s:
                backward()
            elif event.key == pygame.K_a:
                turnleft()
            elif event.key == pygame.K_d:
                turnright()
            else:
                halt()

GPIO.cleanup()