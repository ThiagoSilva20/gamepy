import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('musicadefundo.mp3')
pygame.mixer.music.play(-1) #-1 para repetir a musica

barulho_colisao = pygame.mixer.Sound('colisao.wav')


largura = 700
altura = 540

y = altura / 2 - 50/2
x = largura/2 - 40/2

x_azul = randint(40, 660)
y_azul = randint(50, 490)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:

    relogio.tick(60)
    
    tela.fill((0,0,0))
    
    mensagem = f'Pontos: {pontos}'

    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''
        
    if pygame.key.get_pressed()[K_a]:
        x = x - 4
    if pygame.key.get_pressed()[K_d]:
        x = x + 4
    if pygame.key.get_pressed()[K_w]:
        y = y - 4
    if pygame.key.get_pressed()[K_s]:
        y = y + 4

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))
   
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 660)
        y_azul = randint(50, 500)
        pontos = pontos + 1
        barulho_colisao.play()

    tela.blit(texto_formatado, (490, 5))
    
    pygame.display.update()