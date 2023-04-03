import pygame;
from sys import exit
pygame.init();

screen = pygame.display.set_mode((600, 450));
clock = pygame.time.Clock();
FPS = 60;
turn = "cross";

def DrawWireFrame():
    global screen;
    thickness = 10
    color = "#eeeeee"
    pygame.draw.line(screen, color, (250,50), (250, 350), thickness);
    pygame.draw.line(screen, color, (150,50), (150, 350), thickness);
    pygame.draw.line(screen, color, (50,150), (350, 150), thickness);
    pygame.draw.line(screen, color, (50,250), (350, 250), thickness);

def CreateIcon(pos):
    global symbol, turn;  
    symbol.add(Symbol(pos, turn));

    if(turn == "cross"): turn = "circle";
    else: turn = "cross";
class RectButton(pygame.sprite.Sprite):
    def __init__(self,pos,callbalck):
        super().__init__();
        # self.size = pygame.Rect(());;
        # self.image = pygame.draw.rect(screen, "red", self.size);
        self.image = pygame.image.load("square.png");
        self.image.fill("#222222")
        self.pos = pos;
        self.rect = self.image.get_rect(center = self.pos);
        self.callback = callbalck

    def update(self, events):
        for event in events:
            if(event.type == pygame.MOUSEBUTTONUP):
                if(self.rect.collidepoint(event.pos)):
                    self.callback(self.pos);

class Symbol(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__();

        self.image = pygame.Surface((90,90));
        if(type == "cross"):
            self.image.fill("green");
        else: self.image.fill("red");
        self.rect = self.image.get_rect(center = pos);

button = pygame.sprite.Group();
button.add(RectButton((100,100), CreateIcon));
button.add(RectButton((100,200), CreateIcon));
button.add(RectButton((100,300), CreateIcon));

button.add(RectButton((200,100), CreateIcon));
button.add(RectButton((200,300), CreateIcon));
button.add(RectButton((200,200), CreateIcon));

button.add(RectButton((300,100), CreateIcon));
button.add(RectButton((300,300), CreateIcon));
button.add(RectButton((300,200), CreateIcon));

symbol = pygame.sprite.Group();

while True:
    events = pygame.event.get();
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit();
            exit();
    
    button.draw(screen);
    button.update(events);

    symbol.draw(screen);
    symbol.update();

    DrawWireFrame();
    pygame.display.update();