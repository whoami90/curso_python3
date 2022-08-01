'''
Faça um programa em python que abra e reproduza o áudio em MP3.

irei utilizar o pygame, o tutorial do curso está desatualizado e não está mais funcionando. 

'''
import pygame
#iniciando o pygame
pygame.init()
#importando o arquivo mp3
pygame.mixer.music.load('heaven.mp3')
# colocar o arquivo mp3 para tocar
pygame.mixer.music.play()
input()
pygame.event.wait()




