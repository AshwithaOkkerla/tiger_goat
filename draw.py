import pygame
from shapely.geometry import Polygon
from pygame.math import Vector2
from pygame.locals import *

import os,sys

pygame.init()
BACKGROUND_color = (255,255,255)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tiger Goat Game")
screen.fill(BACKGROUND_color)

triangle_vertices = [(400,100),(200,500),(600,500)]

triangle_color = (255,248,51)

pygame.draw.polygon(screen,triangle_color,triangle_vertices,8)
black = (0,0,0)
green = (0,255,64)
#rectangle over triangle
# rect_x = 170
# rect_y = 200
# rect_width = 500
# rect_height = 200

# rect_color = (255,248,51)
# pygame.draw.rect(screen,rect_color,(rect_x,rect_y,rect_width,rect_height),8)


#parallelogram
parallelogram_vertices = [(150,200),(680,200),(640,400),(110,400)]
pygame.draw.polygon(screen,(255,248,51),parallelogram_vertices,8)
#line
line_color = (255,248,51)
pygame.draw.line(screen,line_color,triangle_vertices[0],(310,500),8)
pygame.draw.line(screen,line_color,triangle_vertices[0],(490,500),8)
pygame.draw.line(screen,line_color,(130,300),(660,300),8)

#intersecting points
points_lst = [(400,100),
              (150,200),(350,200),(755/2,200),(845/2,200),(450,200),(680,200),
              (130,300),(300,300),(355,300),(445,300),(500,300),(660,300),
              (110,400),(250,400),(665/2,400),(935/2,400),(550,400),(640,400),
              (200,500),(310,500),(490,500),(600,500)]

positions = {1:(400,100),2:(150,200),3:(350,200),4:(755/2,200),5:(845/2,200),6:(450,200),7:(680,200),
             8:(130,300),9:(300,300),10:(355,300),11:(445,300),12:(500,300),13:(660,300),
              14:(110,400),15:(250,400),16:(665/2,400),17:(935/2,400),18:(550,400),19:(640,400),
              20:(200,500),21:(310,500),22:(490,500),23:(600,500)}


#numbering the veritces

playergoat = pygame.image.load(os.path.join('Tiger_goat_game','goat.png'))
playergoat = pygame.transform.scale(playergoat,(100,100))

playertiger = pygame.image.load(os.path.join('Tiger_goat_game','tiger.png'))
playertiger = pygame.transform.scale(playertiger,(100,100))

screen.blit(playergoat,(50,500)) # 50,500
screen.blit(playertiger,(700,500))


#vertex color
vertex_color = (255,0,0)
for vertex in points_lst:
    pygame.draw.circle(screen,vertex_color,vertex,5)


#code
board = [['*'],['*','*','*','*','*','*'],['*','*','*','*','*','*'],
				['*','*','*','*','*','*'],['*','*','*','*']]
# goat_count = 0
# tiger_count = 0

# turn = 'goat'
# selected_piece = None

# def draw_piece(piece,x,y):
#     if piece == 'g':
#         color = black
#     else:
#         color = green
#     pygame.draw.circle(screen,color,(x,y),25)

# def is_valid_move(x1,y1,x2,y2):
#     if x2<110 or x2>660 or y2<100 or y2>500:
#         return False 
    # (x2,y2) - check whether it is '*'
# draw_tigers()
pygame.display.update()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

tiger_positions = [(400,100),(755/2,200),(845/2,200)]
goat_positions = []
def draw_tigers():
    for pos in tiger_positions:
        i,j = pos
        pygame.draw.circle(screen,(0,0,0),(i,j),10)

def draw_goats():
    for pos in goat_positions:
        i,j = pos
        pygame.draw.circle(screen,green,(i,j),10)


while len(goat_positions)<15:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if ((x,y) in points_lst) and ((x,y) not in tiger_positions) and ((x,y) not in goat_positions) :   
                goat_positions.append((x,y))
                print(goat_positions)
                if len(goat_positions) == 15:
                    break
    draw_tigers()
    draw_goats()
    pygame.display.update()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                


