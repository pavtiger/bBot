import datetime
import requests
import vk_api
from bs4 import BeautifulSoup
from random import randint
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import pandas as pd

vk_session = vk_api.VkApi(token='')
longpoll = VkLongPoll(vk_session)
p=1
Exit = False
City = ''
greetings = ['привет', 'ку', 'здорово', 'здравствуй']
user_old = dict()
read = False
def send(mess):
    vk.messages.send(
        user_id=event.user_id,
        keyboard=StartKeyboard.get_keyboard(),
        message=mess, random_id=randint(0, 214748647))

hometask = {}
sub = ''

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        event.text = event.text.lower()
        if read == True:
            sub = event.text  hometask[text[0]] = text[1]
            if sub = 
            
        elif event.text == 'start' or event.text == 'начать' or event.text == 'начало':
            read = False
            event.text=event.text.lower()
            vk = vk_session.get_api()
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('посмотреть дз', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('добавить дз', color=VkKeyboardColor.POSITIVE)
            send('хей')
            
        elif event.text == "добавить дз":
            StartKeyboard.add_button('русский', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('алгебра', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('другой вариант', color=VkKeyboardColor.NEGATIVE)
            send("<предмет>")
            read = True
            
        elif event.text == "посмотреть дз" or event.text == "hw":
            StartKeyboard = VkKeyboard(one_time=True)
            for key in hometask.keys():
                StartKeyboard.add_button(hometask[key], color=VkKeyboardColor.POSITIVE)
            send('вотъ')
            
        else:
            send("errorr")
