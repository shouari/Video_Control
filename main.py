from moviepy.editor import *

import pygame

pygame.init()

pygame.display.set_caption('Show Video on screen')

video = VideoFileClip('name_of_your video.mp4')
video.preview()

pygame.quit()
