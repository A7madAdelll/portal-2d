from opject import opject
class port(opject):
    def __init__(self,pic,xx,yy,w,h):
        super().__init__(pic,xx,yy,w,h)
        self.HorV=""
        self.front=[]
        self.back=[]
        if(w>h):
            self.HorV = "H"
            for i in range(xx,xx+w+1):
                self.front.append([i,yy+h])
            for i in range(xx,xx+w+1):
                self.front.append([i,yy])
        else:
            self.HorV = "V"
            for i in range(yy,yy+h+1):
                self.front.append([xx+w,i])
            for i in range(yy,yy+h+1):
                self.front.append([xx,i])


