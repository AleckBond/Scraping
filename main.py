from telethon.sync import TelegramClient

from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
 
import os
from dotenv import load_dotenv

import csv
 
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE")
 
client = TelegramClient(phone, api_id, api_hash)
client.start()

chats = [] #empty lists
last_date = None
size_chats = 200
groups=[]

result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=size_chats,
            hash = 0
        ))
chats.extend(result.chats) #group lists

for chat in chats:
   try:
       if chat.megagroup== True:
           groups.append(chat)
   except:
       continue #Channel not chats
   
   print('Оберіть номер групи з переліку:')
i=0
for g in groups:
   print(str(i) + '- ' + g.title)
   i+=1

g_index = input("Вкажить цифру: ")
target_group=groups[int(g_index)]

print('Впізнаємо користувачів...')
all_participants = []
all_participants = client.get_participants(target_group)
 
print('Збережемо інфу у файл...')
with open("members.csv","w",encoding='UTF-8') as f:
   writer = csv.writer(f,delimiter=",",lineterminator="\n")
   writer.writerow(['username','name','group'])
   for user in all_participants:
       if user.username:
           username= user.username
       else:
           username= ""
       if user.first_name:
           first_name= user.first_name
       else:
           first_name= ""
       if user.last_name:
           last_name= user.last_name
       else:
           last_name= ""
       name= (first_name + ' ' + last_name).strip()
       writer.writerow([username,name,target_group.title])     
print('Парсинг успішно виконано.')

all_messages = [] #Empty List for message
offset_id = 0
limit = 100
total_messages = 0
total_count_limit = 0

while True:
   history = client(GetHistoryRequest(
       peer=target_group,
       offset_id=offset_id,
       offset_date=None,
       add_offset=0,
       limit=limit,
       max_id=0,
       min_id=0,
       hash=0
   ))
   if not history.messages:
       break
   messages = history.messages
   for message in messages:
       all_messages.append(message.message)  #to_dict()) NOt Only Message
   offset_id = messages[len(messages) - 1].id
   if total_count_limit != 0 and total_messages >= total_count_limit:
       break
   
   print("Зберігаємо компромат у файл...") #Start parsing
 
with open("chats.csv", "w", encoding="UTF-8") as f:
   writer = csv.writer(f, delimiter=",", lineterminator="\n")
   writer.writerow(["message"])
   for message in all_messages:
       writer.writerow([message])     
print("Парсинг завершено.")


