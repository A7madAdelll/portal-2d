from opject import opject
from port import port
import pygame
columns=1000
rows=1000
opjwidth=200
opjheight=200
class screen:
    def __init__(self,win,bgpic):
        self.bg = pygame.image.load(bgpic)
        self.newbg = pygame.transform.scale(self.bg, (1000, 1000))
        self.surface = pygame.Surface(self.newbg.get_size())
        self.surface.blit(self.newbg, (0, 0))
        self.every_pixel=[[0] * (columns+1001) for _ in range((rows+1001))]
        self.opjects=[]
    def add_opj(self,win,pic,x,y,kind):
        # opj => normal
        # inport => inport
        ind = len(self.opjects) + 1

        if(kind=="opj"):
            me = opject(pic,x,y,200,200)
            self.opjects.append(me)
            self.show(win,ind)
        if(kind=="inport"):
            me = port(pic,x,y,60,500)
            self.opjects.append(me)
            self.show(win,ind)
        if(kind=="outport"):
            me = port(pic,x,y,500,60)
            self.opjects.append(me)
            self.show(win,ind)

    def update(self,win,ind,dx,dy,s):
        self.delete_last(win,ind)
        # mouse[0]-=self.opjects[ind-1].picopic[0].place[0]
        # mouse[1]-=self.opjects[ind-1].picopic[0].place[1]



        self.opjects[ind-1].updateee(dx,dy,self.opjects[1],self.opjects[2],s)


        self.show(win,ind)


    def delete_last(self,win,ind):

        for i in self.opjects[ind - 1].picopic:
            col = (255, 255, 255)
            self.surface.set_at((i.place[0], i.place[1]), col)
            self.every_pixel[i.place[0]][i.place[1]] = 0

    def show(self,win,ind):

        for i in self.opjects[ind-1].picopic:
            col = (i.color[0], i.color[1], i.color[2])
            self.surface.set_at((i.place[0], i.place[1]), col)
            self.every_pixel[i.place[0]][i.place[1]] = ind
        win.blit(self.surface, (0, 0))
