import vk_api
import random
import os
import time

import requests
import json
from vk_api import VkApi
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotEventType

print('bot activated...')
session = requests.Session()
vk_session = vk_api.VkApi(token="22842069")


def activation_func(x):
    if x >= 1:
        mess_send('скорей всего дождик будет')
    if x>=0.8 and x<=0.9999:
        mess_send('Возможно.. Но шансы малы')

    elif x<0.8 :
        mess_send('скорей всего дождика не будет')

    return x

def formula(cloud, winter, temptr):
    x = (synap_inp[0] * int(cloud)) + (synap_inp[1] * int(winter)) + (synap_inp[2] * int(temptr))
    return x
def stick_send(sti):
    vk.messages.send(
        random_id=event.random_id,
        user_id=event.user_id,
        sticker_id=sti
    )
def mess_send(txt):
    vk.messages.send(
        random_id=event.random_id,
        user_id=event.user_id,
        message=txt
    )
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
    #Слушаем longpoll, если пришло сообщение то:
        print(event.text)

        if event.text.lower() == 'rain':
                vk.messages.send(
                    random_id=event.random_id,
                    user_id=event.user_id,
                    sticker_id='12896'
                )
                print(event)
                for events in longpoll.listen():
                        if events.type == VkEventType.MESSAGE_NEW and events.text:
                            print(events.text)
                            quest = events.text
                            a = list(quest)
                            print(a)

                            cloud = a[0]
                            winter = a[1]
                            temptr = a[2]
                            with open('massa.bin', 'r') as filehandle:
                                bas = json.load(filehandle)

                            synap_inp = [bas[0], bas[1], bas[2]]
                            x = formula(cloud, winter, temptr)
                            mess_send(x)
                            activation_func(x)
                            break


