import pygame
import sys,os,time
pygame.init()

whichT = -1
whichG = -1

moves = 0
width = 1400
height = 800
screen = pygame.display.set_mode((width, height))

text1 = "Start"
text2 = "Quit"

 # colors
PURPLE = (0, 68, 204)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GREEN = (50, 205, 50)
PINK = (179, 0, 89)
RED = (153, 0, 0)
REDL = (240, 0, 0)
LIGHT_YELLOW = (200, 200, 0)
YELLOW = (255, 255, 0)
GREEN = (173,255,47)
LIME = (0, 255, 0)
DARK_BLUE = (0,102,102)
GOLD = (218,165,32)
COLOR = (254,249,167)


input_rect = pygame.Rect(800, 600, 200, 50)


clock = pygame.time.Clock()

pygame.mixer.music.load('Tiger_goat_game/birds.mp3')
pygame.mixer.music.play(-1)


tiger_noise = pygame.mixer.Sound('Tiger_goat_game/tiger-roar.mp3')
# goat_noise = pygame.mixer.Sound('Tiger_goat_game/goatnoise.mp3')

# coin_sound = pygame.mixer.Sound('Tiger_goat_game/jump.mp3')
tiger = 1
goat = 0

icon = pygame.image.load(os.path.join('Tiger_goat_game','game_logo.png'))
pygame.display.set_icon(icon)

index_coord = []
boardState = [[(400, 200), 1],
              [(200, 334), -1], [(333, 333), -1], [(378, 331), 1], [(422, 334), 1], [(467, 333), -1], [(600, 333), -1],
              [(200, 400), -1], [(300, 400), -1], [(366, 400), -1], [(433, 400), -1], [(500, 400), -1], [(600, 400), -1],
              [(200, 468), -1], [(266, 466), -1], [(356, 467), -1], [(443, 467), -1], [(534, 466), -1], [(600, 466), -1],
              [(200, 600), -1], [(333, 600), -1], [(467, 600), -1], [(600, 600), -1]]

neighbours = [[2, 3, 4, 5], [7, 2], [0, 1, 3, 8], [0, 2, 4, 9], [0, 3, 5, 10], [0, 4, 6, 11], [5, 12],
              [1, 8, 13], [2, 7, 9, 14], [3, 8, 10, 15], [4, 9, 11, 16], [5, 10, 12, 17], [6, 11, 18],
              [7, 14], [8, 13, 15, 19], [9, 14, 16, 20], [10, 15, 17, 21], [11, 16, 18, 22], [12, 17]]

tigerJumps = [[8, 9, 10, 11], [13, 3], [14, 4], [1, 5, 15], [2, 6, 16], [3, 17], [4, 18],
              [9], [0, 19, 10], [0, 7, 11, 20], [0, 8, 12, 21], [0, 9, 22], [10],
              [1, 15], [2, 16], [3, 13, 17], [4, 14, 18], [5, 15], [6, 16],
              [8, 21], [9, 22], [10, 19], [11, 20]]

class GamePlay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.tigersCornered = 0
        self.goatsLeft = 15
        self.goatsCaptured = 0
        self.v = 1
        self.phase1 = True
        self.goatOn = -1
        self.goatOffx = 150
        self.goatOffy = 100

        pygame.display.set_caption("Goats and Tiger")

    def gameBoard(self):
        
        pygame.draw.rect(self.screen,COLOR,(180,180,440,440))
        self.brown = (139, 69, 19)
        self.chestnut = (221, 173, 175)

        pygame.draw.polygon(self.screen, BLACK, [[200, 600], [600, 600], [400, 200]],5)
        pygame.draw.lines(self.screen, BLACK, True, [[200, 333.3], [600, 333.3], [600, 466.6], [200, 466.6]], 5)
        pygame.draw.line(self.screen, BLACK, (200, 399.9), (600, 399.9), 5)
        pygame.draw.lines(self.screen, BLACK, False, [[333, 600], [400, 200], [466, 600]],5)

        self.boardPositions = [(400, 200),
                      (200, 334), (333, 333), (378, 331), (422, 334), (467, 333), (600, 333),
                      (200, 400), (300, 400), (366, 400), (433, 400), (500, 400), (600, 400),
                      (200, 468), (266, 466), (356, 467), (443, 467), (534, 466), (600, 466),
                      (200, 600), (333, 600), (467, 600), (600, 600)]

        for i, point in enumerate(self.boardPositions):
            index_coord.append((point,i))
            pygame.draw.circle(self.screen, self.brown, point, 10)
            fontnum = pygame.font.SysFont("monospace", 15, True)
           
            text = fontnum.render(str(i), True, self.chestnut)
            
            textRect = text.get_rect()
            textRect.center = point
            self.screen.blit(text, textRect)
        


    def user_input(self):
        # input the text
        base_font = pygame.font.Font(None, 32) # text to be added
        text = base_font.render(user_text, True, BLACK)
        pygame.draw.rect(screen,(255,255,255),(804, 604, 200, 50))
        pygame.draw.rect(self.screen, BLACK, input_rect, 5)
        self.screen.blit(text, pygame.Rect(804, 604, 200, 50))
        

    def scoreBoard(self):
       
        BLACK = (0, 0, 0)
        # font for Title
        fontT = pygame.font.SysFont("forte", 47)
        text = fontT.render("Score Board", True, (230,62,13))
        self.screen.blit(text, (820, 70))
        font = pygame.font.SysFont("forte", 28)
        text1 = font.render("Goats Left  ", True, BLACK)
        goatsLeft = font.render(str(self.goatsLeft), True, (137,9,9))
        self.screen.blit(text1, (750, 150))
        pygame.draw.rect(self.screen,COLOR,(1050,150,goatsLeft.get_width()+10,goatsLeft.get_height()))
        self.screen.blit(goatsLeft, (1050, 150))
        text2 = font.render("Goats Captured  ", True, BLACK)
        
        goatsCaught = font.render(str(self.goatsCaptured), True,(137,9,9))
        self.screen.blit(text2, (750, 200))
        pygame.draw.rect(self.screen,COLOR,(1050,200,goatsCaught.get_width()+10,goatsCaught.get_height()))

        self.screen.blit(goatsCaught, (1050, 200))
        text3 = font.render("Tigers Cornered  ", True, BLACK)
        tigersCornered = font.render(str(self.tigersCornered), True, (137,9,9))
        self.screen.blit(text3, (750, 250))
        pygame.draw.rect(self.screen,COLOR,(1050,250,tigersCornered.get_width()+10,tigersCornered.get_height()))

        self.screen.blit(tigersCornered, (1050, 250))
        # Grid for scoreboard
       # pygame.draw.line(self.screen, (77, 25, 0), (740, 90), (740, 450), 5)
        #pygame.draw.line(self.screen, (77, 25, 0), (740, 150), (1150, 150), 5)
        #pygame.draw.line(self.screen, (77, 25, 0), (740, 250), (1150, 250), 5)
        #pygame.draw.line(self.screen, (77, 25, 0), (740, 350), (1150, 350), 5)
        #pygame.draw.line(self.screen, (77, 25, 0), (740, 450), (1150, 450), 5)
        #pygame.draw.line(self.screen, (77, 25, 0), (1150, 90), (1150, 450), 5)
        #pygame.draw.line(self.screen, (77, 25, 0), (740, 90), (1150, 90), 5)
        # pygame.draw.line(self.screen, (77, 25, 0), (980, 150), (980, 280), 5)


    def drawTiger(self, coord):
        tiger = pygame.image.load(os.path.join('Tiger_goat_game','tiger.png'))
        tiger = pygame.transform.scale(tiger, (40, 40))
        rect = tiger.get_rect()
        rect.center = (coord[0], coord[1])
        self.screen.blit(tiger, rect)
        return rect
        
        

    def drawGoat(self, coord):
        goat = pygame.image.load(os.path.join('Tiger_goat_game','goat.png'))
        goat = pygame.transform.scale(goat, (40, 40))
        rect = goat.get_rect()
        rect.center = (coord[0], coord[1])
        self.screen.blit(goat, rect)
        return rect

    def display(self, move):
        font2 = pygame.font.SysFont("comicsansms", 35,True)
        font3 = pygame.font.SysFont("comicsansms", 30,True)
        gTurn = font2.render("Goat's Turn", True, (20,37,107))
        tTurn = font2.render("Tiger's Turn", True,(20,37,107) )
        Text = font3.render("Enter the position (From, To)", True, (20,37,107))
        gText = font3.render("Enter the position", True, (20,37,107))
        
        
        if moves % 2 == 0 :
            
            if moves < 31  :
               return gTurn,gText
            else:
                return gTurn,Text

        else:
            return tTurn,Text 

        

    def whichPiece(self, pos):
        if boardState[pos][1] == 1:
            for i in range(3):
                if tigerVect[i].center == boardState[pos][0]:
                    return i
        elif boardState[pos][1] == 0:
            for j in range(15):
                if goatsVect[j].center == boardState[pos][0]:
                    return j

    def invalid(self):
        
        fontIn = pygame.font.SysFont("comicsansms", 45)
        text = fontIn.render("Invalid Move", True, RED)
        self.screen.blit(text, (780, 660))
        
    def isValid(self, inp):
        self.v = 1
        if ',' in inp:
            [curr, des] = list(map(int, inp.strip().split(',')))
            if curr <23 and des <23:
                if boardState[curr][1] == 1 and boardState[des][1] != -1:
                    self.v = 0
                    
                    return False
                elif boardState[curr][1] == -1 :
                    self.v = 0
                    
                    return False
                elif boardState[curr][1] == 0 and boardState[des][1] != -1:
                    self.v = 0
                   
                    return False
                return True
        else:
            if (int(inp) <23):
                if boardState[int(inp)][1] == -1:
                    return True
                
            self.v = 0
           
            return False

    

    def movePiece(self, inp):
        global moves 
        self.v = 1
        if not self.isValid(inp):
            # coin_sound.play() 
            return 

        if moves == 29:
            self.phase1 = False

        if moves % 2 == 0 and self.phase1:
                self.goatMove1(inp)
                moves = moves+1

        elif moves%2 ==0 and self.phase1 == False:
            text = inp.strip().split(',')
            curr, des = int(text[0]), int(text[1])
            if des in neighbours[curr]:
                moves = moves+1
                whichG = self.whichPiece(curr)
                self.goatMove(curr, des, whichG)
            else:
                self.v = 0
               

        else:
            text = inp.strip().split(',')
            curr, des = int(text[0]), int(text[1])
            
            whichT = self.whichPiece(curr)
            if des in tigerJumps[curr] or des in neighbours[curr]:
                    moves = moves+1
                    self.tigerMove(curr, des, whichT)
                
            else:
                self.v = 0
                self.invalid()

    def checkGoat(self, checkPos):
        if boardState[checkPos][1] == 0:
            for i in range(15):
                if goatsVect[i].center == self.boardPositions[checkPos]:
                    goatPositions[i] = (self.goatOffx, self.goatOffy)
                    self.goatOffx += 30
                    return True

    def goatKilled(self, curr, des):
        if (curr == 0 and des >= 2) or (curr >= 2 and des == 0):
            return self.verticalMove(curr, des)
        elif abs(curr - des) > 2:
            return self.verticalMove(curr, des)
        else:
            return self.horizontalMove(curr, des)

    def horizontalMove(self, curr, des):
        if abs(curr - des) == 1:
            return False
        else:
            checkPos = min(curr, des) + 1
            if self.checkGoat(checkPos):
                boardState[checkPos][1] = -1
                return True
            return False

    def verticalMove(self, curr, des):
        if curr != 0 and des != 0:
            checkPos = min(curr, des) + 6
            if self.checkGoat(checkPos):
                boardState[checkPos][1] = -1
                return True
            return False

        else:
            checkPos = max(curr, des) - 6
            if checkPos < 0:
                return False
            if self.checkGoat(checkPos):
                boardState[checkPos][1] = -1
                return True
            return False

    def tigerMove(self, curr, des, whichT):
        if self.goatKilled(curr, des):
           tiger_noise.play()
           self.goatsCaptured += 1
           self.goatsLeft -= 1
           
        tigerPositions[whichT] = boardState[des][0]
        boardState[curr][1] = -1
        boardState[des][1] = 1

        
    def goatMove(self, curr, des, whichG):
        goatPositions[whichG] = boardState[des][0]
        boardState[curr][1] = -1
        boardState[des][1] = 0
        self.isTigerCornered()

    def goatMove1(self, inp):
        self.goatOn += 1
       
        goatPositions[self.goatOn] = boardState[int(inp)][0]
        boardState[int(inp)][1] = 0
        self.isTigerCornered()

    def isTigerCornered(self):
        tc = 0
        for i in range(3):
            ind = boardState.index([tigerVect[i].center, 1])
            if self.checkNeighbours(ind) and self.checkTigerJump(ind):
                tc += 1
                #goat_noise.play()
        self.tigersCornered = tc

    def goatsWon(self):
        fontW = pygame.font.SysFont("serif", 50)
        text = fontW.render("Goats Won!", True, BLACK)
        trect = text.get_rect()
        trect.center = (100, 400)
        self.screen.blit(text, trect)

    def tigerWon(self):
        fontW = pygame.font.SysFont("serif", 50)
        text = fontW.render("Tigers Won!", True, WHITE, BLACK)
        trect = text.get_rect()
        trect.center = (400, 400)
        self.screen.blit(text, trect)

    def checkNeighbours(self, pos):
        count = 0
        for n in neighbours[pos]:
            if boardState[n][1] != -1:
                count += 1
        return count == len(neighbours[pos])

    def checkTigerJump(self, pos):
        count = 0
        for n in tigerJumps[pos]:
            if boardState[n][1] != -1:
                count += 1
        return count == len(tigerJumps[pos])

    def textButton(self, text, color, x, y, width, height):
        if text == text1:
            text = pygame.font.SysFont("comicsansms", 30)
            textB = text.render(text1, True, color)
            rect = textB.get_rect()
            rect.center = ((x + (width / 2)), (y + (height / 2)))
            screen.blit(textB, rect)

        elif text == text2:
            text = pygame.font.SysFont("comicsansms", 30)
            textB1 = text.render(text2, True, color)
            rect = textB1.get_rect()
            rect.center = ((x + (width / 2)), (y + (height / 2)))
            screen.blit(textB1, rect)

    def buttons(self, text, x, y, width, height, color1, color2, action=None):
        current = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > current[0] > x and y + height > current[1] > y:
            rects = pygame.draw.ellipse(screen, color1, (x, y, width, height))
            if click[0] == 1 and action != None:
                if action == "Quit":
                    pygame.quit()
                    quit()
        else:
            rects = pygame.draw.ellipse(screen, color2, (x, y, width, height))
        return rects

game = GamePlay(1200, 800)

menu = True
running = True

tigerPositions = [(400, 200), (378, 331), (422, 334)]
goatPositions = []

user_text = ''

show_start_button = True
show_quit_button = True
is_options_screen = True
text_box_active = False

back = pygame.image.load(os.path.join('Tiger_goat_game','ashwitha.png'))
gameback = pygame.transform.scale(back,(1400,800))
bgimage = pygame.image.load(os.path.join('Tiger_goat_game','firstpage.png'))
picture = pygame.transform.scale(bgimage, (1200, 800))


turn = "Goats"
while running:

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                
                if show_start_button and start_button_elli.collidepoint(event.pos):
                    show_quit_button = False
                    show_start_button = False
                    is_options_screen = False
                    menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu = True

        screen.fill((0, 0, 0))
        if is_options_screen:
            screen.blit(picture, (0, 0))
        else:
             screen.blit(gameback,(0,0))

        if show_start_button:
           
            start_button_elli =game.buttons("Start Game", 500, 200, 168, 50, GREEN,GOLD,action="Play")
            game.textButton(text1, BLACK, 550, 200, 70, 50)
        if show_quit_button:
            
            quit_button_elli =game.buttons("Quit", 520, 280, 130, 50,  RED,GOLD, action="Quit")
            game.textButton(text2, BLACK, 550, 280, 70, 50)
        
        
        pygame.display.update()
    
            
    game.gameBoard()
    game.scoreBoard()
    game.user_input()

    tiger0 = game.drawTiger(tigerPositions[0])
    tiger1 = game.drawTiger(tigerPositions[1])
    tiger2 = game.drawTiger(tigerPositions[2])

    tigerVect = [tiger0, tiger1, tiger2]
    goatsVect = []

    for i in range(300, 600, 20):
        goatPositions.append((100, i))

    for j in range(game.goatsLeft):
        goatsVect.append(game.drawGoat(goatPositions[j]))

    
    text1,text2 = game.display(moves)
    
    
    pygame.draw.rect(screen,COLOR,(770,500,text2.get_width()+50,text2.get_height()+text1.get_height()))
    screen.blit(text1, (800, 500))
    
    screen.blit(text2, (770, 550))
    
   
    
    if  (game.v==0):
        game.invalid()
        

    if game.tigersCornered == 3:
        game.goatsWon()
        

    if game.goatsCaptured == 5:
        game.tigerWon()
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                text_box_active = True
            else:
                text_box_active = False
        if event.type == pygame.KEYDOWN and text_box_active:
            
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:
                game.movePiece(user_text)
                user_text = ""
                pygame.draw.rect(screen,COLOR,(770,500,text2.get_width()+50,text2.get_height()+text1.get_height()))
                pygame.draw.rect(screen,COLOR,(780,660,300,70))
                pygame.draw.rect(screen,(255,255,255),(804, 604, 200, 50))
            else:
                user_text += event.unicode

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
