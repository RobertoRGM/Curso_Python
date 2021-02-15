#MP3 Player
import pygame
pygame.init() #iniciando o módulo pygame
pygame.mixer.music.load('') #Carregando o arquivo que ja deve estar salvo dentro do pycharm inserir o nome do arquivo ('')
pygame.mixer.music.play() #Inicia a musica
pygame.event.wait() #Espera o evento terminar para encerrar o programa