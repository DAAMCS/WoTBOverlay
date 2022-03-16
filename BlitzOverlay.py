from ast import While
from pydoc import importfile
import json
from tkinter.tix import Tree
from turtle import st
import requests
from requests import get
from requests import post
import os
from time import sleep
from tkinter import *
import tkinter

def cls():
    os.system('cls||clear')

def get_id(nickname):
    data = {
        'search' : nickname,
        'type' : "exact"
    }
    try:
        id = get("https://api.wotblitz.ru/wotb/account/list/?application_id=826f55727d94558a8f8ced07170a6aab", params=data).json()['data'][0]['account_id']
    except IndexError:
        cls()
        print("Аккаунт не найден, попробуйте снова ")
        id = get_id(input("Введите свой никнейм: "))
    except KeyError:
        cls()
        print("Ошибка ввода, попробуйте снова ")
        id = get_id(input("Введите свой никнейм: "))
        
    return id

id = get_id(input("Введите свой никнейм: "))

def allstats(id):
    data = {
        "account_id": id
    }
    wins = get("https://api.wotblitz.ru/wotb/account/info/?application_id=a022362c5057adcfa80ed59cbd284584", params=data).json()['data'][str(id)]['statistics']['all']['wins']
    losses = get("https://api.wotblitz.ru/wotb/account/info/?application_id=a022362c5057adcfa80ed59cbd284584", params=data).json()['data'][str(id)]['statistics']['all']['losses']
    battles = get("https://api.wotblitz.ru/wotb/account/info/?application_id=a022362c5057adcfa80ed59cbd284584", params=data).json()['data'][str(id)]['statistics']['all']['battles']
    return wins, losses, battles

def req():
    stats = allstats(id)
    wins = int(stats[0])
    losses = int(stats[1])
    battles = int(stats[2])
    winrate = round((wins/battles)*100, 2)
    return winrate

WoTBO = Tk()
WoTBO.title("WoT Blitz Overlay by DAAMCS & UltStubs Community")
WoTBO.geometry('720x100')
lbl = Label()
lbl.grid(column=0, row=0)  

def overlay():
    global refresh
    if req() > 49 and req() < 51: fgc = '#ADFF2F'
    elif req() > 51 and req() < 53: fgc = '#32CD32'
    elif req() > 53 and req() < 56: fgc = '#7FFFD4'
    elif req() > 56 and req() < 60: fgc = '#00FFFF'
    elif req() > 60 and req() < 64: fgc = '#7B68EE'
    elif req() > 64: fgc = '#8B008B'
    elif req() > 48 and req() < 49: fgc = '#FFFF00'
    elif req() > 47 and req() < 48: fgc = '#FFD700'
    elif req() > 46 and req() < 47: fgc = '#FFA500'
    elif req() > 45 and req() < 46: fgc = '#FF8C00'
    elif req() > 44 and req() < 45: fgc = '#FF4500'
    elif req() > 43 and req() < 44: fgc = '#DC143C'
    elif req() > 42 and req() < 43: fgc = '#FF0000' 
    elif req() < 42: fgc = '#8B0000'

    lbl.configure(text=f'Процент побед: {req()}%', font=("Impact", 50), fg=fgc)
    if True:
        WoTBO.after(refresh, overlay)

refresh = int(input("Введите время обновления статистики (в секундах): "))*1000
overlay()
WoTBO.mainloop()
