import pygame;
from sys import exit
pygame.init();

screen = pygame.display.set_mode((700, 400));
screen.fill("#1F2026")
clock = pygame.time.Clock();
FPS = 60;
turn = "x";
gameWon = False;
whoWon = "";
draw = False;
pieces = 0;
wonLinePos = [(0,0),(700,400)]

game = [
    ["", "", ""], 
    ["", "", ""],
    ["" ,"", ""]
]
def DrawWireFrame():
    global screen;
    thickness = 16
    color = "#3A3A3A"
    pygame.draw.line(screen, color, (250,50), (250, 350), thickness);
    pygame.draw.line(screen, color, (150,50), (150, 350), thickness);
    pygame.draw.line(screen, color, (50,150), (350, 150), thickness);
    pygame.draw.line(screen, color, (50,250), (350, 250), thickness);

def CreateIcon(pos):
    global symbol, turn, game, pieces;  
    gameIndex = (int(pos[0]/100),int(pos[1]/100))
    print(turn);

    if(gameWon == True or draw == True): return;
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
    won = False;

    # Check Vertical
    for i in range(3):
        if((game[i][0] == game[i][1] == game[i][2]) and game[i][0]!=""):
            print(f"x = {i}")
            wonLinePos[0] = ((i+1) * 100, 1 *100);
            wonLinePos[1] = ((i+1) * 100, 3*100);
            won = True;
    
    #Check Horizontal
    for i in range(3):
        if((game[0][i] == game[1][i] == game[2][i]) and game[0][i]!=""):
            wonLinePos[0] = (1 * 100, (i+1) * 100);
            wonLinePos[1] = (3 * 100, (i+1) * 100);
            won = True;

    # Check Diagonal   
    if(game[0][0] == turn and game[1][1] == turn and game[2][2] == turn):
        won =  True
        wonLinePos[0] = (1 * 100, 1 * 100);
        wonLinePos[1] = (3 * 100, 3 * 100);
    elif(game[0][2] == turn and game[1][1] == turn and game[2][0] == turn):
        wonLinePos[0] = (3 * 100, 1 * 100);
        wonLinePos[1] = (1 * 100, 3 * 100);
        won = True;

    if(won == True):
        gameWon = True;
        whoWon = turn;
        return;

    # Check Draw
    if(pieces == 9): 
        draw = True;
        return;
    return False

class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, pos,  fontfamily = "pixel.ttf"):
        super().__init__();
        self.font = pygame.font.Font(f"Assets/{fontfamily}", size);
        self.image = self.font.render(text, False, "#757575");
        self.rect = self.image.get_rect(center = pos);
    def kill(self):
        self.kill();

class RectButton(pygame.sprite.Sprite):
    def __init__(self,pos,callbalck):
        super().__init__();
        # self.size = pygame.Rect(());;
        # self.image = pygame.draw.rect(screen, "red", self.size);
        self.image = pygame.image.load("Assets/square.png");
        self.image.fill("#1F2026")
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

        self.font = pygame.font.Font(f"Assets/pixel.ttf", 96);
        if(type == "x"):
            self.image = self.font.render("X", False, "#757575");
        else: self.image = self.font.render("O", False, "#757575");
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
                screen.fill("#1F2026")
    
    button.draw(screen);
    button.update(events);

    symbol.draw(screen);
    symbol.update();
    
    text.add(Text("Tic Tac Toe", 64, (530,100)))
    DrawWireFrame();
    if(gameWon == True or draw == True):
        if (draw == True):  
            wonText = text.add(Text(f"Draw", 64, (530,200)));
        elif(gameWon == True):
            pygame.draw.line(screen, "#eeeeee", wonLinePos[0], wonLinePos[1], 20)
            text.add(Text(f"{whoWon} won", 64, (530,200)));
    text.draw(screen);
    

    pygame.display.update();