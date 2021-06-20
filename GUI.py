# This import blocks pygame from printing it's startup text.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *

# Setup a GUI class to make the game developement process a bit easy.
class GUI:
	class Label:
		def __init__(self, Display, Colors, Pos, Size):
			self.Pos = Pos
			self.Size = Size
			self.Colors = Colors
			self.Display = Display

		def draw(self):
			pygame.draw.rect(self.Display, self.Colors, (self.Pos[0], self.Pos[1], self.Size[0], self.Size[1]))

	class Button:
		def __init__(self, Display, Colors, NewColor, Pressed, Pos, Size):
			self.Pos = Pos
			self.Size = Size
			self.Colors = Colors
			self.NewColor = NewColor
			self.Pressed = Pressed
			self.Display = Display

		def draw(self):
			self.Hover_On_Rect = pygame.Rect(self.Pos[0], self.Pos[1], self.Size[0], self.Size[1])
			self.Mouse_Pos = pygame.mouse.get_pos()
			self.Hover_On = self.Hover_On_Rect.collidepoint(self.Mouse_Pos)

			pygame.draw.rect(self.Display, self.Colors, self.Hover_On_Rect)
			if self.Hover_On:
				pygame.draw.rect(self.Display, self.NewColor, self.Hover_On_Rect)
				if pygame.mouse.get_pressed()[0]:
					pygame.draw.rect(self.Display, self.Pressed, self.Hover_On_Rect)
					pygame.time.delay(100)
					return 1

				else: return 0
			else: pygame.draw.rect(self.Display, self.Colors, self.Hover_On_Rect)

	class Text:
		def __init__(self, Display, Text, Colors, Font_Pos, Font_size):
			self.Colors = Colors
			self.Font_Pos = Font_Pos
			self.Font_size = Font_size
			self.Text = Text
			self.Display = Display

		def draw(self):
			self.font = pygame.font.SysFont("calibri", self.Font_size)
			self.text = self.font.render(self.Text, True, self.Colors)
			self.Display.blit(self.text, self.Font_Pos)
