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
def send(mess):
    vk.messages.send(
        user_id=event.user_id,
        keyboard=StartKeyboard.get_keyboard(),
        message=mess, random_id=randint(0, 214748647))



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        event.text = event.text.lower()
        if event.text == 'start' or event.text == 'начать' or event.text == 'начало':
            event.text=event.text.lower()
            vk = vk_session.get_api()
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('Поменять Настройки', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('Добавить ДЗ', color=VkKeyboardColor.POSITIVE)
            send('йоу')
        elif event.text == "Добавить ДЗ":
            send("<subject> txt")
        else:
            send("error")
