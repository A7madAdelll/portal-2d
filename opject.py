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
                a=pixell(x+xx,y+yy,pixel_color.r,pixel_color.g,pixel_color.b,0)
                self.picopic.append(a)

    def updateee(self,dx,dy,opject1,opject2,s):

        for i in self.picopic:
            if(i.slope==s):
                i.place[0] = i.place[0] + dx
                i.place[1] = i.place[1] + dy
            elif(i.slope==s+1 or (i.slope==0 and s==3)):
                i.place[0] = i.place[0] + dy
                i.place[1] = i.place[1] - dx
            elif(i.slope==s-1 or (i.slope==3 and s==0)):
                i.place[0] = i.place[0] - dy
                i.place[1] = i.place[1] + dx




        xs=opject1.picopic[0].place[0]
        xe=opject1.picopic[len(opject1.picopic)-1].place[0]

        ys=opject1.picopic[0].place[1]
        ye=opject1.picopic[len(opject1.picopic)-1].place[1]
        print(xs,xe,ys,ye)
        for i in self.picopic:
            if(i.place[0]>=xs and i.place[0]<=xe and i.place[1]>=ys and i.place[1]<=ye and self!=opject1 ):
                rel_y=i.place[1]-ys
                rel_x=xe-i.place[0]

                if(opject2.HorV!=opject1.HorV):

                    # i.place[0]=opject2.front
                    i.place[0]=opject2.picopic[0].place[0]+rel_y
                    i.place[1]=opject2.picopic[len(opject1.picopic)-1].place[1]+rel_x

                    i.slope= i.slope+1
                    if(i.slope==4):
                        i.slope=0

                else:
                    i.place[0] = opject2.picopic[0].place[0] - rel_x
                    i.place[1] = opject2.picopic[0].place[1] + rel_y


        xs=opject2.picopic[0].place[0]
        xe=opject2.picopic[len(opject2.picopic)-1].place[0]

        ys=opject2.picopic[0].place[1]
        ye=opject2.picopic[len(opject2.picopic)-1].place[1]
        print(xs,xe,ys,ye)
        for i in self.picopic:
            if(i.place[0]>=xs and i.place[0]<=xe and i.place[1]>=ys and i.place[1]<=ye and self!=opject2 ):
                rel_y=ye-i.place[1]
                rel_x=i.place[0]-xs

                if(opject2.HorV!=opject1.HorV):
                    i.place[0]=opject1.picopic[len(opject1.picopic)-1].place[0]+rel_y
                    i.place[1]=opject1.picopic[0].place[1]+rel_x

                    i.slope= i.slope-1
                    if(i.slope==-1):
                        i.slope=3

                else:
                    i.place[0] = opject1.picopic[0].place[0] - rel_x
                    i.place[1] = opject1.picopic[0].place[1] + rel_y