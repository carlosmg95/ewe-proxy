#!/usr/bin/env python

"""
MiP  program to control it
To Use:
./control_mip.py --i hci0 -b B4:99:4C:48:CA:23
"""
import logging, argparse, time, sys, json,random, math
import mippy
import threading
def prueba_movement():
	
	robot.forward(0.3)
	print("POSICION FINAL")
	print("x   "+str(robot.x))
	print("y   "+str(robot.y))
	print("apha   "+str(robot.ang))

def playSound(type):
	"""
	35 = hellllooo (sexy)
	p60 = play
	m87 = Boring
	53 = Music (MiP says music not plays it)
	"""
	sounds =[]
	if type=='affirmation':
		sounds= [16,37,56,79,80,81]
	elif type=='negation':
		sounds= [22,17,51,78,85]
	elif type=='joy':
		sounds= [29,39,40,65,50,57,73,76,77,90]
	elif type=='question':
		sounds= [19,36,38,75]
	elif type=='laugh':
		sounds= [28,41,91,52,94]
	elif type=='talk':
		sounds= [20,21,45]
	elif type=='angry':
		sounds=[4,15,79,80,33,81]
	elif type=='sad':
		sounds= [55,97]
	else:
		sounds = [10,11,12,13,26,29,34,69,70,89]
	n = random.randrange(len(sounds))
	mip.playSound(sounds[n])

def dance():
	mip.setVolume(0)
	time.sleep(1)
	mip.setGameMode(0x04)

def talk_movement():
	playSound("talk")
	robot.forward(0.4)
	mip.setHeadLed(0,1,0,1)
	playSound("talk")
	time.sleep(1)
	robot.right(45)
	time.sleep(1)
	robot.forward(0.1)
	playSound("talk")
	time.sleep(1)
	mip.setHeadLed(1,0,1,0)
	robot.left(180)
	playSound("talk")
	time.sleep(1)
	robot.forward(0.1)
	time.sleep(1)
	robot.left(55)
	playSound("talk")
	mip.setHeadLed(1,1,1,1)
	time.sleep(1)
	robot.forward(0.4)
	goInitialPosition()

def affirmation_movement():
	mip.setHeadLed(2,2,2,2)
	playSound("affirmation")
	for i in range(4):
		if((i%2)==0):
			robot.forward(0.025)
		else:
			robot.reverse(0.025)
	mip.setHeadLed(1,1,1,1)

def negation_movement():
	robot = mippy.Turtle(mip)
	mip.setChestLed(255, 0, 0)
	for i in range(4):
		if((i%2)==0):
			mip.setHeadLed(0,1,0,1)
			robot.right(35)
		else:
			mip.setHeadLed(1,0,1,0)
			robot.left(35)
		playSound("negation")
		time.sleep(0.2)
	mip.setHeadLed(1,1,1,1)

def action_movement():
	robot.forward(0.035)
	mip.setHeadLed(3,3,3,3)
	time.sleep(0.2)
	playSound("")
	time.sleep(0.2)
	robot.right(360)
	time.sleep(0.2)
	robot.reverse(0.035)
	time.sleep(0.2)
	mip.setHeadLed(1,1,1,1)
	time.sleep(0.2)

def question_movement():
	for i in range(2):
		if((i%2)==0):
			mip.setHeadLed(0,1,0,1)
			robot.right(15)
		else:
			mip.setHeadLed(1,0,1,0)
			robot.left(15)
		playSound("")
		time.sleep(1)
	mip.setHeadLed(1,1,1,1)

def start_movement():
	mip.setChestLed(0, 0, 255)
	mip.setHeadLed(3,3,3,3)
	mip.playSound(43)
	time.sleep(2)
	robot.forward(2.4)

def go_back_movement():
	playSound("affirmation")
	time.sleep(0.2)
	robot.right(180)
	time.sleep(0.5)
	robot.forward(2.4)
	time.sleep(0.5)
	robot.right(90)
	time.sleep(0.5)
	robot.forward(1.1)
	time.sleep(0.5)
	robot.left(90)
	time.sleep(0.5)
	robot.forward(2.2)
	time.sleep(0.5)
	robot.left(90)
	time.sleep(0.5)
	robot.forward(1.2)
	time.sleep(0.5)
	robot.left(450)
	time.sleep(0.5)
	playSound("affirmation")

def show_coffee_movement():
	mip.setHeadLed(3,3,3,3)
	time.sleep(0.5)
	playSound("affirmation")

def show_work_room_movement():
	mip.setHeadLed(3,3,3,3)
	time.sleep(0.5)
	playSound("affirmation")

def show_workspace_movement():
	mip.setHeadLed(3,3,3,3)
	time.sleep(0.5)
	playSound("affirmation")
	time.sleep(0.5)
	robot.left(90)
	time.sleep(0.5)
	robot.forward(1.2)
	time.sleep(0.5)
	robot.left(90)
	time.sleep(0.5)
	robot.forward(0.9)
	time.sleep(0.5)
	robot.left(90)
	time.sleep(0.5)
	playSound("talk")
	time.sleep(0.5)
	robot.left(90)
	time.sleep(0.5)
	robot.forward(0.5)
	time.sleep(0.5)
	robot.right(90)
	time.sleep(0.5)
	playSound("joy")

def main(action):
	if action=='affirmation':
		affirmation_movement()
	elif action=='stressed':
		dance()
	elif action=='talk':
		talk_movement()
	elif action=='action':
		action_movement()
	elif action=='negation':
		negation_movement()
	elif action=='question':
		question_movement()
	elif action=='start':
		start_movement()
	elif action=='action':
		action_movement()
	elif action=='show_coffee':
		show_coffee_movement()
	elif action=='show_workspace':
		show_workspace_movement()
	elif action=='show_work_room':
		show_work_room_movement()
	elif action=='go_back':
		go_back_movement()
	else:
		prueba_movement()
		print("ninguno")
	mip.setGameMode(0x05)

def goInitialPosition():
	print("go to initial")
	print("x   "+str(robot.x))
	print("y   "+str(robot.y))
	print("angulo   "+str(robot.ang))
	robot.right(robot.ang)
	print("angulo final   "+str(robot.ang))
	time.sleep(1)
	robot.left(90)
	print("angulo inicial   "+str(robot.ang))
	time.sleep(1)
	robot.reverse(robot.y)
	print("x   "+str(robot.x))
	print("y   "+str(robot.y))
	time.sleep(1)
	if(robot.x<0):
		robot.right(90)
		time.sleep(1)
		robot.forward(-robot.x)
		time.sleep(1)
		robot.left(90)
	if(robot.x>0):
		robot.left(90)
		time.sleep(1)
		robot.forward(robot.x)
		time.sleep(1)
		robot.right(90)

class Control:
	def __init__(self, mip):
		self.mip = mip
		self.x =0
		self.y=0
		self.ang=90
		self.const=float(440)/(360)

	def left(self, angle):
		self.mip.turnByAngle(-angle*self.const)
		self.ang+=angle
		print("left")
		print("x   "+str(robot.x))
		print("y   "+str(robot.y))

	def right(self, angle):
		self.mip.turnByAngle(angle*self.const)
		self.ang-=angle
		print("right")
		print("x   "+str(robot.x))
		print("y   "+str(robot.y))

	def forward(self, distance):
		print("forward  "+str(distance))
		print("x   "+str(robot.x))
		print("y   "+str(robot.y))
		alpha=self.ang%360
		print("apha   "+str(alpha))
		if(alpha<0):
			alpha+=360
		self.mip.distanceDrive(distance)
		if(alpha<90)&(alpha>=0):
			self.x+=distance*math.cos((alpha*math.pi)/180)
			self.y+=distance*math.sin((alpha*math.pi)/180)
		if(alpha>=90)&(alpha<180):
			self.x-=distance*math.cos(((180-alpha)*math.pi)/180)
			self.y+=distance*math.sin(((180-alpha)*math.pi)/180)
		if(alpha<270)&(alpha>=180):
			self.x-=distance*math.cos(((alpha-180)*math.pi)/180)
			self.y-=distance*math.sin(((alpha-180)*math.pi)/180)
		if(alpha>=270):
			self.x+=distance*math.cos(((360-alpha)*math.pi)/180)
			self.y-=distance*math.sin(((360-alpha)*math.pi)/180)

	def reverse(self, distance):
		print("reverse  "+str(distance))
		print("x   "+str(robot.x))
		print("y   "+str(robot.y))
		alpha=self.ang%360
		print("apha   "+str(alpha))
		if(alpha<0):
			alpha+=360
		self.mip.distanceDrive(-distance)
		if(alpha<90)&(alpha>=0):
			self.x-=distance*math.cos((alpha*math.pi)/180)
			self.y-=distance*math.sin((alpha*math.pi)/180)
		if(alpha>=90)&(alpha<180):
			self.x+=distance*math.cos(((180-alpha)*math.pi)/180)
			self.y-=distance*math.sin(((180-alpha)*math.pi)/180)
		if(alpha<270)&(alpha>=180):
			self.x+=distance*math.cos(((alpha-180)*math.pi)/180)
			self.y+=distance*math.sin(((alpha-180)*math.pi)/180)
		if(alpha>=270):
			self.x-=distance*math.cos(((360-alpha)*math.pi)/180)
			self.y+=distance*math.sin(((360-alpha)*math.pi)/180)


logging.basicConfig(level=logging.DEBUG)
gt = mippy.GattTool('hci0', "B4:99:4C:48:CA:23")
mip = mippy.Mip(gt)
robot=Control(mip)
main(sys.argv[1])

