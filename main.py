# Rock-Paper-Scissors Game
# Import all required modules.
import random
import sys
import os

# This import blocks pygame from printing it's startup text.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *

# Custom modules
from GUI import GUI

# Initializing Game
pygame.init()
Clock = pygame.time.Clock()

Userwin = 0
Opponent = [-1, 0]
def Shuffle(Userchoice): return [random.randint(1, 3), Userchoice]

# Setup up window
Display = pygame.display.set_mode((1000, 675))
pygame.display.set_caption("Rock-Paper-Scissors")
Logo = pygame.image.load("./res/Logo.png")

# Setup Game elements.
# Setup Title.
Title = GUI.Text(Display, "Rock - Paper - Scissors", (44, 44, 44), (345, 10), 35)
Title_Underline = GUI.Label(Display, (44, 44, 44), (325, 50), (345, 3))
pygame.display.set_icon(Logo)

# Main menu elements
PressSpace = GUI.Text(Display, "Press Spacebar to Play", (44, 44, 44), (200, 250), 72)
PressEsc = GUI.Text(Display, "Press Escape to Quit", (44, 44, 44), (390, 355), 27)

# Main game loop elements
# Setup Game buttons.
Rock_Button = GUI.Button(Display, (255, 255, 255), (197, 161, 255), (197, 161, 255), (100, 150), (125, 50))
Rock_Text = GUI.Text(Display, "Rock", (44, 44, 44), (127, 159), 35)

Paper_Button = GUI.Button(Display, (255, 255, 255), (197, 161, 255), (197, 161, 255), (425, 150), (125, 50))
Paper_Text = GUI.Text(Display, "Paper", (44, 44, 44), (447, 159), 35)

Scissor_Button = GUI.Button(Display, (255, 255, 255), (197, 161, 255), (197, 161, 255), (750, 150), (125, 50))
Scissor_Text = GUI.Text(Display, "Scissors", (44, 44, 44), (758.5, 159), 35)

# Setup Separator and Status bar.
Separator = GUI.Label(Display, (44, 44, 44), (150, 250), (700, 3))
Statusbar = GUI.Label(Display, (44, 44, 44), (0, 650), (1000, 25))

# Computer
Computer_Text = GUI.Text(Display, "Computer", (44, 44, 44), (425, 270), 35)
Computer_Play = GUI.Text(Display, "Let's Play!", (44, 44, 44), (357, 400), 72)
Computer_Rock = GUI.Text(Display, "Rock", (44, 44, 44), (425, 400), 72)
Computer_Paper = GUI.Text(Display, "Paper", (44, 44, 44), (415, 400), 72)
Computer_Scissors = GUI.Text(Display, "Scissors", (44, 44, 44), (390, 400), 72)

# Winning status
Tie = GUI.Text(Display, "Tie!", (255, 255, 255), (475, 655), 20)
User_Win = GUI.Text(Display, "You Win!", (255, 255, 255), (450, 655), 20)
User_Lose = GUI.Text(Display, "You Lose!", (255, 255, 255), (450, 655), 20)

# Main menu
def MainMenu():
	while 1:
		Clock.tick(72)
		Display.fill((255, 255, 255))
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE: main()
				if event.key == pygame.K_ESCAPE: sys.exit()

		# Draw Title
		Title.draw()
		Title_Underline.draw()

		PressSpace.draw() # Draw Press spacebar to play text.
		PressEsc.draw() # Draw Press escape to quit text.

		pygame.display.update()
	pygame.quit()

# Game loop
def main():
	global Opponent
	while 1:
		Clock.tick(72)
		Display.fill((255, 255, 255))
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE: MainMenu()

		# Draw Title
		Title.draw()
		Title_Underline.draw()

		# Draw Game buttons.
		if Rock_Button.draw(): Opponent = Shuffle(1)
		Rock_Text.draw()

		if Paper_Button.draw(): Opponent = Shuffle(2)
		Paper_Text.draw()

		if Scissor_Button.draw(): Opponent = Shuffle(3)
		Scissor_Text.draw()

		# Main Gameplay
		Separator.draw()
		Statusbar.draw()
		Computer_Text.draw()
		if Opponent[0] != -1:
			if Opponent[1] != 0:
				if Opponent[0] == 1: Computer_Rock.draw()
				elif Opponent[0] == 2: Computer_Paper.draw()
				elif Opponent[0] == 3: Computer_Scissors.draw()

				if (Opponent[1] == 1 and Opponent[0] == 3) or (Opponent[1] == 3 and Opponent[0] == 1): Userwin = 1
				elif (Opponent[1] == 1 and Opponent[0] == 2) or (Opponent[1] == 2 and Opponent[0] == 1): Userwin = 2
				else: Userwin = 3

				if Opponent[1] == Opponent[0]: Tie.draw()
				elif Userwin == Opponent[1]: User_Win.draw()
				elif Userwin != Opponent[1]: User_Lose.draw()

		else:
			Computer_Play.draw()
			GUI.Text(Display, "Let's Play!", (255, 255, 255), (450, 655), 20).draw()

		pygame.display.update()
	pygame.quit()

if __name__ == '__main__':
	MainMenu()
	main()
