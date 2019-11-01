import datetime
import requests
import vk_api
from random import randint
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import pandas as pd

vk_session = vk_api.VkApi(token='')
longpoll = VkLongPoll(vk_session)
p=1
Exit = False
City = ''
user_old = dict()
inputt = 0
def send(mess):
    vk.messages.send(
        user_id=event.user_id,
        keyboard=StartKeyboard.get_keyboard(),
        message=mess, random_id=randint(0, 214748647))

ind = 0
sub = ''
task = ''
arr_task = ['0', '0', '0']
date = ''
df = pd.DataFrame(columns=['done', 'date', 'sub', 'task'])

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        event.text = event.text.lower()
        if arr_task == ['6', '6', '6']:
            send("вот это повезло")
                
        if inputt == 1: # урок
            inputt += 1
            sub = event.text
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('незадана)', color=VkKeyboardColor.POSITIVE)
            if sub == "русский":
                StartKeyboard.add_button('упр', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('правило', color=VkKeyboardColor.DEFAULT)
            StartKeyboard.add_button('другое', color=VkKeyboardColor.DEFAULT)
            send("<задание>")
            
        elif inputt == 2 or inputt == 3 or inputt == 4: # таск тремя цифрами
            task = event.text
            if task == "незадана)":
                send("повезло")
                inputt += 4
            else:
                if task == 'упр':
                    StartKeyboard = VkKeyboard(one_time=True)
                    StartKeyboard.add_button('1', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_button('2', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_button('3', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_line()
                    StartKeyboard.add_button('4', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_button('5', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_button('6', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_line()
                    StartKeyboard.add_button('7', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_button('8', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_button('9', color=VkKeyboardColor.POSITIVE)
                    StartKeyboard.add_line()
                    StartKeyboard.add_button('0', color=VkKeyboardColor. DEFAULT)
                    send("<номер>")
                    arr_task[inputt - 3] = str(event.text)
                    inputt += 1
                else:
                    send("<введи>")
                    inputt += 0
                
        elif inputt == 5: # послед. цифра
            if task == "упр":
                arr_task[inputt - 3] = str(event.text)
                task = int(''.join(arr_task))
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('сегодня(', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('завтра', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_line()
            StartKeyboard.add_button('послезавтра', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('другой', color=VkKeyboardColor.DEFAULT)
            send("<когда>")
            inputt += 1
            
        elif inputt == 6: # заполнение
            inputt = 0
            date = event.text
            # d = pd.DataFrame({'done': [0], 'date': [date], 'sub': [sub], 'task': [task]})
            df.loc[ind] = [0, date, sub, task]
            ind += 1
            print(df)
            
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('посмотреть дз', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('добавить дз', color=VkKeyboardColor.DEFAULT)
            send("готово")
            
            
            
        elif event.text == 'start' or event.text == 'начать' or event.text == 'начало':
            event.text = event.text.lower()
            vk = vk_session.get_api()
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('посмотреть дз', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('добавить дз', color=VkKeyboardColor.DEFAULT)
            send('хей')
            
        elif event.text == "добавить дз" or event.text == "add":
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
