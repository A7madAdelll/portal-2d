import pygame
from opject import opject
from screen import screen
FPS = 45

WIN = pygame.display.set_mode((1000, 1000))





pygame.display.set_caption('Chess')
# img.show()

# runing the game in event loop every n of seconds to check if there is any change to render
def main():

    scree=screen(WIN,"./pics/bg.png")
    scree.add_opj(WIN,"./pics/me.jpg",0,0,"opj")
    scree.add_opj(WIN, "./pics/red.png", 300, 300, "inport")
    scree.add_opj(WIN, "./pics/blue.png", 600, 300, "outport")

    WIN.blit(scree.surface, (0, 0))
    lastmousenow=()
    newmousenow=()
    chosen=-1
    given_slope=0
    gameRuning = True

    clock = pygame.time.Clock()  # for the FPS

    holding=0

    while gameRuning:
        clock.tick(FPS)  # tick FPS Defined Above

        for event in pygame.event.get():  # check event if happened any time
            if holding==0:
                mous = pygame.mouse.get_pos()
                chosen = scree.every_pixel[mous[0]][mous[1]]

            if event.type == pygame.QUIT:  # if i needed to quit and pressed it turn off the game
                gameRuning = False  # and exit the loop

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and holding==0 and chosen!=0:
                lastmousenow=pygame.mouse.get_pos()
                chosen=scree.every_pixel[lastmousenow[0]][lastmousenow[1]]
                print(chosen)

                for p in scree.opjects[chosen - 1].picopic:
                    if (lastmousenow[0] == p.place[0] and lastmousenow[1] == p.place[1]):
                        given_slope = p.slope
                        break


                holding=1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and holding==1:
                print("hehe")
                holding=0
            if holding == 1:
                newmousenow=pygame.mouse.get_pos()
                dx=newmousenow[0]-lastmousenow[0]
                dy=newmousenow[1]-lastmousenow[1]
                scree.update(WIN,chosen,dx,dy,given_slope)
                lastmousenow=newmousenow
                print(lastmousenow,chosen)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 :
            scree.add_opj(WIN, "./pics/me.jpg", 0, 0, "opj")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2 :
            scree.add_opj(WIN, "./pics/blue.png", 600, 300, "outport")

        pygame.display.update()

    # pygame.quit() #window    of game is closed fffrrrrrr mnwwww


main()
