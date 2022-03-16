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
from random import randint as rint
a = 15

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
    lbl.configure(text=f'Процент побед: {req()}%', font=("Impact", 50), fg='#008080')
    if True:
        WoTBO.after(120000, overlay)

overlay()
WoTBO.mainloop()
