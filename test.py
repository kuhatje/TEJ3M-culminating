import time, pygame
import RPi.GPIO as GPIO

left_high = 17
left_low = 27
right_high = 23
right_low = 22

l1 = l2 = r1 = r2 = False

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(left_high, GPIO.OUT)
	GPIO.setup(left_low, GPIO.OUT)
	GPIO.setup(right_high, GPIO.OUT)
	GPIO.setup(right_low, GPIO.OUT)

init()

def run():
	init()
	print('set')
	GPIO.output(left_high, l1)
	GPIO.output(left_low, l2)
	GPIO.output(right_high, r1)
	GPIO.output(right_low, r2)

def forward():
	l1 = r2 = False
	l2 = r1 = True
	run()
	#GPIO.output(left_high, False)
	#GPIO.output(left_low, True)
	#GPIO.output(right_high, True)
	#GPIO.output(right_low, False)
def backward():
	l1 = r2 = True
	l2 = r1 = False
	run()
def turnleft():
	l2 = r2 = False
	l1 = r1 = True
	run()
def turnright():
	l2 = r2 = True
	l1 = r1 = False
	run()
def halt():
	l1 = l2 = r1 = r2 = False
	run()

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
	#add some sort of delay to slow down

print('start')
print('end')

GPIO.cleanup()