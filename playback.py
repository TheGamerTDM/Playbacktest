import pygame
import tkinter as tkr
import os

player = tkr.Tk()

player.title('Audio Player')
player.geometry('205x400')

os.chdir('where your folder is :D')
songlist = os.listdir()

playlist = tkr.Listbox(player, highlightcolor='blue', selectmode=tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()


def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def ExitPlayer():
    pygame.mixer.music.stop()


button1 = tkr.Button(player, width=5, hight=3, text='PLAY', command=Play)
button2 = tkr.Button(player, width=5, hight=3, text='STOP', command=ExitPlayer)

var = tkr.StringVar()
songlist = tkr.Label(player, textvariable=var)

songtitle.pack()
button1.pack(fill='x')
button2.pack(fill='x')

playlist.pack(fill='both', expand='yes')

player.mainloop()
