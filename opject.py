import pygame
from pixel import pixell
import pixel
width=200
height=200
class opject:
    def __init__(self,pic,xx,yy,w,h):
        self.picopic = []
        # Replace with the actual path to your image file
        image =  pygame.image.load(pic)
        # Get the dimensions of the image
        resized_image = pygame.transform.scale(image,(w,h))
        # w,h=image.get_size()
        # print(w,h)
        # Loop through each pixel and change its color
        for x in range(w):
            for y in range(h):
                # Get the RGB values of the current pixel
                pixel_color = resized_image.get_at((x, y))
                a=pixell(x+xx,y+yy,pixel_color.r,pixel_color.g,pixel_color.b)
                self.picopic.append(a)

    def updateee(self,dx,dy):
        for i in self.picopic:
            i.place[0]=i.place[0]+dx
            i.place[1]=i.place[1]+dy