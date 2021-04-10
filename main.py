import re
import dop
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
def msg(x):
    vk.messages.send(  # Отправляем сообщение
        user_id=event.user_id,
        message=x,
        random_id=get_random_id()
    )
str=r'([п|П]ереведи число )(\w+)( из )(\d+)( системы счисления в )(\w+)'
vk_session = vk_api.VkApi(
        token="eec9495eafe4f742955f2bb8825bcbce7ecbb735c5dca33a4000fc1ea01d207db29cc0927c86ad030e045")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me :
            matchj=re.match(str,event.text)
            if matchj==None:
               msg("Введите команду типа:Переведи число (целое число,которое нужно перевести) из (начальная система счисления) системы счисления в (система в которую нужно перевести)")
            else:
                a=matchj.group(2)
                c = matchj.group(4)
                b = matchj.group(6)
                print(a,b,c)
                msg(dop.per(a, int(b), int(c)))


