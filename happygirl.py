import pygame
import math
import random
from tkinter import *
from tkinter import messagebox

name = input("Enter your name: ")
m1 = name + ", You Won!"
m2 = name + ", You Lost :( "

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
messagebox.showinfo('Welcome!', 'Bored of playing Hangman? Then play my game Happygirl! It is very simple. Guess the word by clicking on the letters, but do not let the Happygirl disappear! ')            

window.deiconify()
window.destroy()
window.quit()

pygame.init()
width, height = 1100, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome to the Happygirl Game!")


radius = 20
gap = 15
letters = []
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i//13) * (gap + radius * 2))
    ltr = chr(A + i)
    letters.append([x , y , ltr, True])


letter_font = pygame.font.SysFont("comicsans", 30)
word_font = pygame.font.SysFont("comicsans", 50)
title_font = pygame.font.SysFont("comicsans", 60)


images = [pygame.image.load("happygirl0.png"),
pygame.image.load("happygirl1.png"), pygame.image.load("happygirl2.png"),
pygame.image.load("happygirl3.png"), pygame.image.load("happygirl4.png"),
pygame.image.load("happygirl5.png"), pygame.image.load("happygirl6.png")]

happygirl_status = 0
words = ["MATH", "COMPUTER", "SCIENCE", "HINDI", "FRENCH"]
word = random.choice(words)
guessed = []

def draw():
    win.fill((255, 255, 255))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1, (1,2,3))        
    win.blit(text, (400, 200))         

    for letter in letters:
        x , y , ltr, visible = letter
        if visible:
            pygame.draw.circle(win, (0, 1, 2), (x , y), radius, 3)
            text = letter_font.render(ltr, 1, (1, 2, 3))
            win.blit(text, (x - text.get_width()/2, y - text.get_width()/2))

    win.blit(images[happygirl_status], (140, 80))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill((255, 255, 255))
    text = word_font.render(message, 1, (1, 2, 3))
    win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
def main():
    global happygirl_status

    fps = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr , visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if  dis < radius:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                happygirl_status += 1
        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
       
 
        if won:
            display_message(str(m1))
            break

        if happygirl_status == 6:
            display_message(str(m2))
            break

while True:
    main()
    break
    
pygame.quit()














