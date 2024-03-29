import datetime
import requests
import vk_api
from random import randint
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import pandas as pd
from twilio.rest import Client
import json

words = [
    ['незадана)', 'no hometask'],
    ['сегодня(', 'today('],
    ['завтра', 'tomorrow'],
    ['послезавтра', 'day after tomorrow'],
    ['другой', 'another'],
    ['повезло', 'lucky'],
    ['упр', 'num'],
    ['<номер>', '<number>'],
    ['<введи>', '<input>'],
    ['посмотреть дз', 'get hometask'],
    ['добавить дз', 'add hometask'],
    ['готово', 'done'],
    ['<когда>', '<when>']
]
#['', '']
lan = 0


vk_session = vk_api.VkApi(token='1f21b45de665984483f3f48ea811cb27be1d330d1afdef5ce06e4246efcf46acff15f8b388807d6c29cbb')
longpoll = VkLongPoll(vk_session)
p = 1
Exit, text, s = False, False, False
City = ''
user_old = dict()
inputt = 0
account_sid = 'AC1defc3f87d049509c6cb352fdc8d9a9f'
auth_token = 'c2d965531c333e1d5ab984b0c79d4d1e'
client = Client(account_sid, auth_token)

def send(mess):
    vk.messages.send(
        user_id=event.user_id,
        keyboard=StartKeyboard.get_keyboard(),
        message=mess, random_id=randint(0, 214748647))


def add(df):
    Export = df.to_json(r'task_data.json')
    
    
def sms(text):
    message = client.messages \
        .create(
            body=str(text),
            from_='+12012672118',
            to='+79150599190'
        )

    print(f'sent message: {message.sid}')



ind = 0
sub = ''
task = ''
typee = ''
arr_task = ['0', '0', '0']
date = ''
df = pd.DataFrame(columns=['done', 'date', 'sub', 'task'])

#with open('task_data.json', 'r') as f_read:
    #dct = json.load(f_read)
df = pd.read_json('task_data.json', orient='index')
    
#pd.DataFrame.from_dict(dct)
print(df)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        event.text = event.text.lower()

        if text == True:
            sms(event.text)
            send(f'отправлено {event.text}')
            
        if inputt == 1: # урок
            inputt += 1
            sub = event.text
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button(words[0][lan], color=VkKeyboardColor.POSITIVE)
            if sub == 'русский':
                StartKeyboard.add_button('упр', color=VkKeyboardColor.DEFAULT)
                StartKeyboard.add_line()
                StartKeyboard.add_button('правило', color=VkKeyboardColor.DEFAULT)
            StartKeyboard.add_button('другое', color=VkKeyboardColor.DEFAULT)
            send('<задание>')
            
        elif inputt == 2 or inputt == 3 or inputt == 4: # таск тремя цифрами
            task = event.text
            if inputt == 2:
                typee = task
                
            if task == words[0][lan]:
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('сегодня(', color=VkKeyboardColor.NEGATIVE)
                StartKeyboard.add_button('завтра', color=VkKeyboardColor.POSITIVE)
                StartKeyboard.add_line()
                StartKeyboard.add_button('послезавтра', color=VkKeyboardColor.POSITIVE)
                StartKeyboard.add_button('другой', color=VkKeyboardColor.DEFAULT)
                send('повезло')
                inputt += 3
            else:
                if typee == 'упр':
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
                    send('<номер>')
                    arr_task[inputt - 3] = str(task)
                    inputt += 1
                else:
                    send('<введи>')
                    inputt += 3
                
        elif inputt == 5: # послед. цифра
            if typee == 'упр':
                arr_task[inputt - 3] = str(event.text)
                task = int(''.join(arr_task))
                
            if typee == words[0][lan]:
                inputt = 0
                date = event.text
                df.loc[ind] = [0, date, sub, task]
                ind += 1
                print(df)
                print('')
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('посмотреть дз', color=VkKeyboardColor.POSITIVE)
                StartKeyboard.add_button('добавить дз', color=VkKeyboardColor.DEFAULT)
                send('готово')
            else:
                StartKeyboard = VkKeyboard(one_time=True)
                StartKeyboard.add_button('сегодня(', color=VkKeyboardColor.NEGATIVE)
                StartKeyboard.add_button('завтра', color=VkKeyboardColor.POSITIVE)
                StartKeyboard.add_line()
                StartKeyboard.add_button('послезавтра', color=VkKeyboardColor.POSITIVE)
                StartKeyboard.add_button('другой', color=VkKeyboardColor.DEFAULT)
                send('<когда>')
                inputt += 1
            
        elif inputt == 6: # заполнение
            inputt = 0
            date = event.text
            df.loc[ind] = [0, date, sub, task]
            ind += 1
            print(df)
            print('')
            add(df)
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('посмотреть дз', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('добавить дз', color=VkKeyboardColor.DEFAULT)
            send('готово')
            
            
            
        elif event.text == 'start' or event.text == 'начать' or event.text == 'начало':
            event.text = event.text.lower()
            vk = vk_session.get_api()
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('посмотреть дз', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('добавить дз', color=VkKeyboardColor.DEFAULT)
            send('хей')
            
        elif event.text == 'добавить дз' or event.text == 'add':
            StartKeyboard = VkKeyboard(one_time=True)
            StartKeyboard.add_button('русский', color=VkKeyboardColor.NEGATIVE)
            StartKeyboard.add_button('алгебра', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_line()
            StartKeyboard.add_button('геома', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('англ', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_line()
            StartKeyboard.add_button('доп. англ', color=VkKeyboardColor.POSITIVE)
            StartKeyboard.add_button('другой вариант', color=VkKeyboardColor.DEFAULT)
            send('<предмет>')
            inputt = 1
            
            
            
        elif event.text == 'посмотреть дз' or event.text == 'hw':
            StartKeyboard = VkKeyboard(one_time=True)
            for key in hometask.keys():
                StartKeyboard.add_button(hometask[key], color=VkKeyboardColor.POSITIVE)
            send('вотъ')
            
        elif event.text == 'python' or s == True:
            if s:
                s = False
                sms(event.text)
            else:
                send('<text>')
                sms('python')
                s = True
            
        elif event.text == 'send':
            text = True
            
        elif event.text == 'sound':
            sms('sound')
            
        else:
            send('error')
