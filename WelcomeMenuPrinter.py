from __future__ import print_function # needs to be first statement in file
from terminalSize import get_terminal_size
import sys

welcomeMessage = '* Welcome to Oracle Logical Domain Manager *'
menuText = '***MENU***'
menuItem1 = ('Print active VMs list', '0')
menuItem2 = ('Create New VM', '1')
menuItem3 = ('Delete VM', '2')
menuItem4 = ('Start VM', '3')
menuItem5 = ('Show CPU/RAM Capacity', '4')


def printBorder(width):
	for i in range(width):
		print('=', end='')

def printInMid(textToPrint,width):
	spacesToprint = (width - len(textToPrint)) / 2
	printSpaces(spacesToprint)
	print(textToPrint)
	printSpaces(spacesToprint)

def printSpaces(numberOfSpacesToPrint):
	for i in range(numberOfSpacesToPrint):
		print(' ', end='')

def printMenuItem(menuItem, screenWidth):
	firstText = menuItem[0]
	secondText = menuItem[1]
	secondText = 'Press \"' + secondText + '\"'
	print(firstText, end='')
	spacesToprint = screenWidth - len(firstText) - len(secondText)
	printSpaces(spacesToprint)
	print(secondText, end='')

def printWelcomeMenu():
	size =  get_terminal_size()
	screenWidth = size[0]
	print()
	#Welcome Message
	printInMid(welcomeMessage, screenWidth)
	print()
	#print the top border
	printBorder(screenWidth)
	#print ***MENU***"
	printInMid(menuText, screenWidth)
	print('', end='\n')
	#print the bottom border
	printBorder(screenWidth)
	#Print Menu Items
	#Can use it in a dictiornary and iterate throught it too.
	printMenuItem(menuItem1, screenWidth)
	printMenuItem(menuItem2, screenWidth)
	printMenuItem(menuItem3, screenWidth)
	printMenuItem(menuItem4, screenWidth)
	printMenuItem(menuItem5, screenWidth)