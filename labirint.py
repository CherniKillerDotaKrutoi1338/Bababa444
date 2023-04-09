# Разработай свою игру в этом файле!
from  pygame import *
#Основое окно

display.set_caption('Моя первая игра')

window = display.set_mode((700, 500))

background = transform.scale(image.load('sky.png'), (700,500) )

class Card(sprite.Sprite):
    def __init__(self,wigth,height,x,y,color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
            draw.rect(window, self.fill_color, self.rect)


class Pic(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
#СТЕНЫ
class GameSprite(sprite.Sprite):
    def __init__(self, picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture), (w,h))
        self.rect = self.image.get_rect()    
        self.rect.x = x
        self.rect.y = y       
def reset(self):
    window.blit(self.image,(self.rect.x, self.rect.y))
wall_1 = GameSprite('wall.jpg', 80,180,200,250)



player2 = Pic('mzlf.png',80,80,200,250)
   

run = True
while run:
    time.delay(50)
    

    for e in event.get():
        if e.type == QUIT:
            run = False
                
    window.blit(background, (0,0))
    
    #player1.draw()
    player2.reset()
    display.update()


        