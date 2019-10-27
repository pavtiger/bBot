import datetime
import requests
import vk_api
from bs4 import BeautifulSoup
from random import randint
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
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
        
        
        
        if Exit == True or event.text in greetings or event.text == 'start' or event.text == 'пока' or event.text == 'спасибо' or event.text == 'начать' or event.text == 'начало' or event.text == 'все мероприятия' or event.text == 'бесплатное мероприятие' or event.text == 'поменять настройки': # Первый раз
            event.text=event.text.lower()
            if event.text in greetings:
                
                vk = vk_session.get_api()
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('Поменять Настройки', color=VkKeyboardColor.NEGATIVE)
                StartKeyboard.add_button('Хочу погулять', color=VkKeyboardColor.POSITIVE)
                send('Привет''&#128075;')
            elif event.text == 'пока':
                send('Пока''&#128533;')
            elif event.text == 'спасибо':
                send('Обращайся''&#128519;')
            elif event.text == 'начать' or event.text == 'начало' or event.text == 'поменять настройки':
                if event.text == 'начать'or event.text == 'начало':
                    user_old[event.user_id] = []
                vk = vk_session.get_api()
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('Москва', color=VkKeyboardColor.PRIMARY)
                StartKeyboard.add_button('Санкт-Петербург', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Казань', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Новосибирск', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Екатеринбург', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Нижний Новгород', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Самара', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Красноярск', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('Краснодар', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_button('Сочи', color=VkKeyboardColor.DEFAULT)
                send('Выберете город:')
