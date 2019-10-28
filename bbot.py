import datetime
import requests
import vk_api
from bs4 import BeautifulSoup
from random import randint
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import pandas as pd

vk_session = vk_api.VkApi(token='e77578a5c80bd6b4f8acfd48d877821dccc2443944942206420fcadc7bfb6c77744b5ebcde0cacf386fd3')
longpoll = VkLongPoll(vk_session)
p=1
Exit = False
City = ''
greetings = ['привет', 'ку', 'здорово', 'здравствуй']
user_old = dict()
inputt = 0
def send(mess):
    vk.messages.send(
        user_id=event.user_id,
        keyboard=StartKeyboard.get_keyboard(),
        message=mess, random_id=randint(0, 214748647))

hometask = {}
sub = ''
task = ''
date = ''

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        event.text = event.text.lower()
        if inputt == 1:
            inputt += 1
            sub = event.text
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('незадана)', color=VkKeyboardColor.POSITIVE)
            if sub == "русский":
                StartKeyboard.add_button('упр', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('правило', color=VkKeyboardColor.DEFAULT)
            send("<задание>")
        elif inputt == 2:
            inputt += 1
            task = event.text
            if task == 
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('сегодня(', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('завтра', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('послезавтра', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('другой', color=VkKeyboardColor.POSITIVE)
        elif inputt == 3:
            inputt = 0
            date = event.text
            # hometask
                
        elif event.text == 'start' or event.text == 'начать' or event.text == 'начало':
            event.text = event.text.lower()
            vk = vk_session.get_api()
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('посмотреть дз', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('добавить дз', color=VkKeyboardColor.DEFAULT)
            send('хей')
            
        elif event.text == "добавить дз":
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('русский', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('алгебра', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_line()
            StartKeyboard.add_button('геома', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('англ', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_line()
            StartKeyboard.add_button('доп. англ', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('другой вариант', color=VkKeyboardColor.DEFAULT)
            send("<предмет>")
            inputt = 1
            
        elif event.text == "посмотреть дз" or event.text == "hw":
            StartKeyboard = VkKeyboard(one_time=True)
            for key in hometask.keys():
                StartKeyboard.add_button(hometask[key], color=VkKeyboardColor.POSITIVE)
            send('вотъ')
            
        else:
            send("error")
