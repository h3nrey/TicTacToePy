import pygame;
from sys import exit
pygame.init();

screen = pygame.display.set_mode((600, 450));
clock = pygame.time.Clock();
FPS = 60;
turn = "x";
gameWon = False;
whoWon = "";
draw = False;
pieces = 0;

game = [
    ["", "", ""], 
    ["", "", ""],
    ["" ,"", ""]
]
def DrawWireFrame():
    global screen;
    thickness = 10
    color = "#eeeeee"
    pygame.draw.line(screen, color, (250,50), (250, 350), thickness);
    pygame.draw.line(screen, color, (150,50), (150, 350), thickness);
    pygame.draw.line(screen, color, (50,150), (350, 150), thickness);
    pygame.draw.line(screen, color, (50,250), (350, 250), thickness);

def CreateIcon(pos):
    global symbol, turn, game, pieces;  
    gameIndex = (int(pos[0]/100),int(pos[1]/100))
    print(turn);

    if(gameWon == True): return;
    if(game[gameIndex[0] - 1][gameIndex[1] - 1] == ""):
        pieces += 1;
        game[gameIndex[0] - 1][gameIndex[1] - 1] = turn;
        symbol.add(Symbol(pos, turn));

        CheckGame();
        if(turn == "x"): turn = "0";
        else: turn = "x";
    print(game);

def CheckGame():
    global game, turn, gameWon, whoWon, draw;
    gameWon = False;
        
    # CHECK COLUMN
    if(game[0][0] == turn and game[0][1] == turn and game[0][2] == turn):
        gameWon = True;
        whoWon = turn;
    elif(game[1][0] == turn and game[1][1] == turn and game[1][2] == turn):
        gameWon = True;
        whoWon = turn;
    elif(game[2][0] == turn and game[2][1] == turn and game[2][2] == turn):
        gameWon = True;
        whoWon = turn;

    # CHECK ROW
    if(game[0][0] == turn and game[1][0] == turn and game[2][0] == turn):
        gameWon = True;
        whoWon = turn;
    elif(game[0][1] == turn and game[1][1] == turn and game[2][1] == turn):
        gameWon = True;
        whoWon = turn;
    elif(game[0][2] == turn and game[1][2] == turn and game[2][2] == turn):
        gameWon = True;
        whoWon = turn;

    # turn DIAGONAL    
    if(game[0][0] == turn and game[1][1] == turn and game[2][2] == turn):
        gameWon = True;
        whoWon = turn;
    elif(game[0][2] == turn and game[1][1] == turn and game[2][0] == turn):
        gameWon = True;
        whoWon = turn;

    if(pieces == 9): 
        draw = True;
        return;
    return False

class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, pos,  fontfamily = "pixel.ttf"):
        super().__init__();
        self.font = pygame.font.Font(f"Assets/{fontfamily}", size);
        self.image = self.font.render(text, False, "red");
        self.rect = self.image.get_rect(center = pos);
    def kill(self):
        self.kill();

class RectButton(pygame.sprite.Sprite):
    def __init__(self,pos,callbalck):
        super().__init__();
        # self.size = pygame.Rect(());;
        # self.image = pygame.draw.rect(screen, "red", self.size);
        self.image = pygame.image.load("Assets/square.png");
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
        if(type == "x"):
            self.image.fill("green");
        else: self.image.fill("red");
        self.rect = self.image.get_rect(center = pos);

button = pygame.sprite.Group();

# DRAW BUTTONS
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


text = pygame.sprite.Group();
wonText = "";
while True:
    events = pygame.event.get();
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit();
            exit();
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_r):
                gameWon = False;
                draw = False;
                game = [
                    ["", "", ""], 
                    ["", "", ""],
                    ["" ,"", ""]
                ];
                symbol.empty();
                pieces = 0;
                whoWon = ""
                turn = "x"
                text.empty();
                screen.fill("black");
    
    button.draw(screen);
    button.update(events);

    symbol.draw(screen);
    symbol.update();
    

    if(gameWon == True or draw == True):
        if (draw == True):  
            wonText = text.add(Text(f"Draw", 48, (500,50)));
            draw = False;
        elif(gameWon == True):
            text.add(Text(f"{whoWon} wins", 48, (500,50)));
            gameWon = False;
    text.draw(screen);
    

    DrawWireFrame();
    pygame.display.update();